#############################################################################
# usage: manual_crop.py [-h] -in_dir IN_DIR -out_dir OUT_DIR
# arguments:
#   -h, --help        show this help message and exit
#   -in_dir IN_DIR    Input directory
#   -out_dir OUT_DIR  Output directory
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
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("-in_dir", required=True, help="Input directory")
parser.add_argument("-out_dir", required=True, help="Output directory")
args = parser.parse_args()

if not exists(args.in_dir):
    sys.exit("Input directory "+args.in_dir+" does not exist.")
if not exists(args.out_dir):
    makedirs(args.out_dir)

for f in listdir(args.in_dir):
    impath = join(args.in_dir,f)
    if not isfile(impath):
        continue
    im = misc.imread(impath)
    # top left corner
    plt.figure()
    plt.imshow(im)
    mgr = plt.get_current_fig_manager()
    mgr.full_screen_toggle()
    plt.title('Click top left and bottom right corners for cropped image')
    pts = plt.ginput(2,show_clicks='True')
    x1 = pts[0][0].astype(int)
    y1 = pts[0][1].astype(int)
    x2 = pts[1][0].astype(int)
    y2 = pts[1][1].astype(int)
    im_crop = im[y1:y2,x1:x2] # NOTE: im[y: y + h, x: x + w] 
    misc.imsave(join(args.out_dir,f),im_crop)
    cv2.rectangle(im,(x1,y1),(x2,y2),(0,255,0),1) 
    plt.imshow(im)
    plt.pause(1)
    plt.close()
