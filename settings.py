# microscoPi, Raspberry Pi based microscope platform
# Copyright (C) 2014 Ilan Davis, Mick Phillips & Douglas Russell
# University of Oxford, Oxford, United Kingdom
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

CAMERA_RESOLUTION = (2592, 1944)
PREVIEW_LAYOUT = (0, 0, 800, 600)
WINDOW_SIZE = (800, 600)
MAX_FPS = 20
# The timelapse interval can be set to any value
# in milliseconds, but if the capture time exceeds
# this time, then that dictates the pace and will
# make it difficult to trigger input events
TIMELAPSE_INTERVAL = 5000

STORAGE_DIR = '~'
