# Copyright (c) 2016-2017 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Autogenerated python message buffer code.
Source: clad/types/customObjectMarkers.clad
Full command line: ../tools/message-buffers/emitters/Python_emitter.py -C ./src/ -I ../robot/clad/src/ ../coretech/vision/clad/src/ ../coretech/common/clad/src/ ../lib/util/source/anki/clad -o ../generated/cladPython// clad/types/customObjectMarkers.clad
"""

from __future__ import absolute_import
from __future__ import print_function

def _modify_path():
  import inspect, os, sys
  search_paths = [
    '../..',
    '../../../../tools/message-buffers/support/python',
  ]
  currentpath = os.path.abspath(os.path.dirname(inspect.getfile(inspect.currentframe())))
  for search_path in search_paths:
    search_path = os.path.normpath(os.path.abspath(os.path.realpath(os.path.join(currentpath, search_path))))
    if search_path not in sys.path:
      sys.path.insert(0, search_path)
_modify_path()

import msgbuffers

Anki = msgbuffers.Namespace()
Anki.Cozmo = msgbuffers.Namespace()

class CustomObjectMarker(object):
  "Automatically-generated int_16 enumeration."
  Circles2   = 0
  Circles3   = 1
  Circles4   = 2
  Circles5   = 3
  Diamonds2  = 4
  Diamonds3  = 5
  Diamonds4  = 6
  Diamonds5  = 7
  Hexagons2  = 8
  Hexagons3  = 9
  Hexagons4  = 10
  Hexagons5  = 11
  Triangles2 = 12
  Triangles3 = 13
  Triangles4 = 14
  Triangles5 = 15
  Count      = 16

Anki.Cozmo.CustomObjectMarker = CustomObjectMarker
del CustomObjectMarker

