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
Source: clad/types/engineState.clad
Full command line: ../tools/message-buffers/emitters/Python_emitter.py -C ./src/ -I ../robot/clad/src/ ../coretech/vision/clad/src/ ../coretech/common/clad/src/ ../lib/util/source/anki/clad -o ../generated/cladPython// clad/types/engineState.clad
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

class EngineState(object):
  "Automatically-generated uint_8 enumeration."
  Stopped             = 0
  WaitingForUIDevices = 1
  LoadingData         = 2
  Running             = 3
  UpdatingFirmware    = 4

Anki.Cozmo.EngineState = EngineState
del EngineState


class RobotConnectionResult(object):
  "Automatically-generated uint_8 enumeration."
  Success               = 0
  ConnectionFailure     = 1
  ConnectionRejected    = 2
  OutdatedFirmware      = 3
  OutdatedApp           = 4
  NeedsPin              = 5
  InvalidPin            = 6
  PinMaxAttemptsReached = 7

Anki.Cozmo.RobotConnectionResult = RobotConnectionResult
del RobotConnectionResult


class RobotDisconnectReason(object):
  "Automatically-generated uint_8 enumeration."
  Unknown                   = 0
  WifiTimeout               = 1
  SleepSettings             = 2
  SleepEraseCozmo           = 3
  SleepPlacedOnCharger      = 4
  SleepBackground           = 5
  ExitSDKMode               = 6
  OutdatedFirmware          = 7
  OutdatedApp               = 8
  DebugForceDisconnect      = 9
  DebugDataPersistenceReset = 10
  AppTerminated             = 11

Anki.Cozmo.RobotDisconnectReason = RobotDisconnectReason
del RobotDisconnectReason

