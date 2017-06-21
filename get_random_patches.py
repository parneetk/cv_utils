#############################################################################
# usage: get_random_patches.py [-h] -in_dir IN_DIR -out_dir OUT_DIR [-n N]
#                              [-sz SZ]
# arguments:
#   -h, --help        show this help message and exit
#   -in_dir IN_DIR    Input directory
#   -out_dir OUT_DIR  Output directory
#   -n N              Number of patches per image
#   -sz SZ            Patch size
#
# written by: Parneet Kaur 
#############################################################################

from scipy import misc
from os import makedirs, listdir
from os.path import exists, join, isfile
import numpy as np
import sys
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("-in_dir", required=True, help="Input directory")
parser.add_argument("-out_dir", required=True, help="Output directory")
parser.add_argument("-n", type=int, default=100, help="Number of patches per image")
parser.add_argument("-sz", type=int, default=100, help="Patch size") #in pixels
args = parser.parse_args()

if not exists(args.out_dir):
    makedirs(args.out_dir)

if not exists(args.in_dir):
    sys.exit("Input directory "+args.in_dir+" does not exist.")

count = 1
for f in listdir(args.in_dir):
    impath = join(args.in_dir,impath)
    if not isfile(impath):
        continue
    im = misc.imread(impath)
    w,h,_ = im.shape
    print("Processing image: "+impath)
    if not (w-args.sz>0 or h-args.sz>0):
        print("Patch size should not be geater than image size.")
        continue
    randX = np.random.randint(w-args.sz,size=args.n)
    randY = np.random.randint(h-args.sz,size=args.n)   
    for i in range(args.n):
        x = randX[i]
        y = randY[i]
        patch = im[y:y+args.sz,x:x+args.sz,:]
        misc.imsave(join(args.out_dir,str(count))+'.png',patch)
        count = count+1  
