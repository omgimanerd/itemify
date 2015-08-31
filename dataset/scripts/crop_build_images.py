#!/usr/bin/python
# This script takes all the images in /dataset/build_images and crops the item
# build out of them and renames them to the champion to which they correspond
# to.
# This script should only be run under the assumption that the images in the
# direction were freshly loaded from the League of Legends Screenshot directory,
# with one image for each champion build prenamed in numerical order corresponding
# to the champions' alphabetical order.
# Author: Alvin Lin (alvin.lin@stuypulse.com)

from PIL import Image
