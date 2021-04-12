#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Copyright (C) 2015 David Pinto <david.pinto@bioch.ox.ac.uk>
##
## This file is part of microscoPi.
##
## microscoPi is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
##
## microscoPi is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, see <http://www.gnu.org/licenses/>.

"""Stitch multiple images together.

Here's a short demo:

    import scipy.ndimage
    import numpy
    import scipy.misc
    import stitching

    im = stitching.rgb2gray (scipy.ndimage.imread (your_image_path))
    offsets = [[400, 400], [100.0, 56.0], [-89.0, 93.0], [-90.0, 0.0],
               [0.0, 100.0], [98.0, 0.0]]

    images = list ()
    starts = numpy.array (offsets).cumsum (axis = 0)
    for s, e in zip (starts, starts + 128):
      images.append (stitching.addnoise (im[s[0]:e[0],s[1]:e[1]].copy ()))

    fixed_offsets = list ([[0, 0]])
    for ind in range (1, len (images)):
      fixed_offsets.append (stitching.find_offsets (images[ind-1], images[ind],
                            offsets[ind]))

    local_offsets = stitching.local_2_global_offsets (fixed_offsets)
    stitched = stitching.stitch_image (images, local_offsets)

    scipy.misc.toimage (stitched).show ()

Can also be used as an application in which case must be called 

    $ stitching.py path/to/im1 xoffset,yoofset path/to/im2 patch/to/output

Can also be called with multiple images, but the initial offset is always
interleaved with the path for multiple images

    $ stitching.py path/to/im1 xoffset1,yoofset1 path/to/im2 \
      xoffset2,yoofset2 path/to/im3 path/to/output

TODOS
  * acccept multipage tiff as input images with offsets as metadata
  * stitching with no initial guess
  * optimize by perfoming correlations by convolutions with inverted
    kernels on fourier space
  * optimize the adjust of offset coordinates by searching for the
    template in a smaller region

"""

import sys
import operator

import numpy
import numpy.random
import scipy.ndimage
import scipy.signal

def rgb2gray (im):
  """Convert RGB image into grayscale.

  Conversion is done by a weighted mean of each RGB channel.  The weights
  for each channel are the luminance factors as defined by ITU-R BT.1700,
  i.e.:

      0.29894 * E'r + 0.58704 * R'g + 0.11402 * E'b

  where E'r, E'g, and E'b are gamma-pre-corrected primary signals.

  Notes:
    * if image is already grayscale, returns a copy of the input image
    * class is conserved but considering the nature of the operations, it
      probably makes more sense to use a floating point class
  """
  c = im.shape[2]
  if c == 1:
    return im.copy()
  elif c == 3:
    return (im * numpy.array ([[[0.29894, 0.58704, 0.11402]]])).sum (axis = 2)
  else:
    raise "Not a grayscale or RGB image"

def xcorr_coeff_nd (a, b, mode = "valid"):
  """Calculate the cross correlation coefficient of n dimensional signal.
  """
  if not numpy.issubdtype (a.dtype, numpy.float):
    a = a.astype ("single")
  if not numpy.issubdtype (b.dtype, numpy.float):
    b = b.astype ("single")

  a_pow = scipy.signal.correlate (a**2, numpy.ones (b.shape), mode = "valid")
  return (scipy.signal.correlate (a, b, mode = "valid")
          / numpy.sqrt (a_pow * numpy.sum (b ** 2)))

def find_offsets (im1, im2, init_guess, confidence = 0.9):
  """
  Start with offset between the top left corners of the two images.
  """
  ## step 1: find the part of im2 that supposedly overlaps with im1 to
  ## use as template on the matching.  Cases to take into account (in 1D)
  ## are:
  ##
  ##  * typical case, im1 and im2 of same size, im2 starting at the end of im1
  ##    im1.shape = 128, im2.shape = 128, init_guess = 100
  ##  |----------|
  ##       1
  ##          |----------|
  ##                2
  ##
  ##  * opposite of typical case, im1 and im2 of same size, im2 ending at the
  ##    start of im1
  ##    im1.shape = 128, im2.shape = 128, init_guess = -100
  ##          |----------|
  ##                1
  ##  |----------|
  ##       2
  ##
  ##  * im1 much larger than im2 with im2 completely inside im1
  ##    im1.shape = 512, im2.shape = 128, init_guess = 100
  ##  |----------------------|
  ##          1
  ##          |----------|
  ##                2
  ##
  ##  * opposite, im2 much larger than im1 and enclosing im1
  ##    im1.shape = 128, im2.shape = 512, init_guess = -300
  ##          |----------|
  ##                1
  ##  |----------------------|
  ##          2
  ##
  ##  * im1 and im2 being of same size with no change of position
  ##    im1.shape = 128, im2.shape = 128, init_guess = 0
  ##  |----------|
  ##       1
  ##  |----------|
  ##       2
  ##
  ## All this weird cases make the function more useful. The offset may used
  ## to overlap images, not only copy and paste on top of each other.

  inds = list ()
  for guess, s1, s2 in zip (init_guess, im1.shape, im2.shape):
    s = slice (round (max (- guess + ((s2 + guess) * (1 - confidence)), 0)),
               round (min ((s1 - guess) * confidence, s2)))
    inds.append (s)

  template = im2[inds]

  ## step 2: do the registration of the template
  c = xcorr_coeff_nd (im1, template)
  template_offset = numpy.unravel_index (c.argmax (), c.shape)

  ## step 3: adjust registration coordinates to the whole im2 image
  im2_offset = list ()
  for offset, ind in zip (template_offset, inds):
    im2_offset.append (offset - ind.start)

  return im2_offset

def local_2_global_offsets (local_offsets):
  """Convert offset of each image (to the previous on the list), into offset
  to a global position (0, 0, 0, ...) defined as the top left corner of the
  first image in the tuple.
  """
  return numpy.array (local_offsets).cumsum (axis = 0)

def stitch_image (images, global_offsets):
  """Create the stitched image from multiple images and corresponding offsets
  to a global position (0, 0, 0, ...).
  """
  global_offsets = numpy.array (global_offsets)
  shapes = map (numpy.shape, images)

  ## compute the start and end coordinates of each image relative to the
  ## global coordinate system
  starts  = global_offsets.min (axis = 0)
  ends    = (global_offsets + shapes).max (axis = 0)

  ## create a "blank" canvas where to paint the images, and remap each
  ## image coordinates to this canvas
  stitched = numpy.zeros (tuple (ends - starts), dtype = images[0].dtype)
  stitched_starts = global_offsets - starts
  stitched_ends   = stitched_starts + shapes

  ## paint
  for im, start, end in zip (images, stitched_starts, stitched_ends):
    s = [slice (ss, se) for ss, se in zip (start, end)]
    stitched[s] = im

  return stitched

def addnoise (im):
  """Add gaussian and poisson noise to image.

  Only useful for testing purposes really.
  """
  im += (numpy.random.normal (0, 20, im.shape)
         + numpy.random.poisson (im, im.shape))
  im[im < 0] = 0
  return im

if __name__ == "__main__":
  ## If we are being called as application, expect input argv to be:
  ## argv = [script_path, im1_path, offset1, im2_path, offset2, im3_path, save_path]
  argn = len (sys.argv) -2
  if argn < 3:
    print "Not enough input arguments.  Needs at least 3, IM1 OFFSET IM"
    sys.exit (1)
  elif (argn -3) % 2 != 0:
    print "Input must be 3 plus multiples of 2"
    sys.exit (1)

  images  = list ()
  for fpath in argn[1::2]:
    images.append (scipy.ndimage.imread (fpath))
  offsets = list ()
  for offset in argn[2:-1:2]:
    offsets.append (map (float, (offset.split (","))))

  fixed_offsets = list ([[0] * images[0].ndim])
  for ind in range (0, len (images) -1):
    fixed_offsets.append (find_offsets (images[ind], images[ind+1],
                          offsets[ind]))

  stitched = stitch_image (images, local_2_global_offsets (fixed_offsets))
  scipy.misc.imsave (sys.argv[-1], stitched)

