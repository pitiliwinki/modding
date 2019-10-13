# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:49:11 2019

@author: Gerald
"""

import numpy as np
import imageio
import argparse
import os

parser = argparse.ArgumentParser(description='Process file/files in folder and subfolders.')
parser.add_argument("path", help="The path to check and convert",
                    type=str)
args = parser.parse_args()
path= args.path
if path.endswith(".png"):
    files = [path]
elif os.path.isdir(path):
    files = [os.path.join(root, name) for root, dirs, files in os.walk(path) for name in files if name.endswith(".png")]
for fil in files:
    im = imageio.imread(fil)
    typ=np.obj2sctype(im)
    im=im*1.0
    maxim=np.amax(im[:,:,0:3],axis=2)
    factor=np.nan_to_num(1.0*np.minimum(im[:,:,3],maxim)/maxim)
    im[:,:,0:3]*=np.rollaxis(np.tile(factor,(3,1,1)),0,3)
    im=im.astype(typ)
    imageio.imsave(fil,im)