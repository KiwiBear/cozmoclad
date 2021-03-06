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
Source: clad/types/ledTypes.clad
Full command line: ../tools/message-buffers/emitters/Python_emitter.py -C ../robot/clad/src/ -o ../generated/cladPython// clad/types/ledTypes.clad
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

class BackpackLayer(object):
  "Automatically-generated uint_8 enumeration."
  BPL_USER        = 0
  BPL_ANIMATION   = 1
  BPL_IMPULSE     = 2
  BACKPACK_LAYERS = 3

Anki.Cozmo.BackpackLayer = BackpackLayer
del BackpackLayer


class LEDId(object):
  "Automatically-generated uint_8 enumeration."
  LED_BACKPACK_LEFT   = 0
  LED_BACKPACK_FRONT  = 1
  LED_BACKPACK_MIDDLE = 2
  LED_BACKPACK_BACK   = 3
  LED_BACKPACK_RIGHT  = 4
  NUM_BACKPACK_LEDS   = 5

Anki.Cozmo.LEDId = LEDId
del LEDId


class LEDColor(object):
  "Automatically-generated uint_32 enumeration."
  LED_CURRENT_COLOR = 0xffffffff
  LED_OFF           = 0x0
  LED_RED           = 0xff0000
  LED_GREEN         = 0xff00
  LED_YELLOW        = 0xffff00
  LED_BLUE          = 0xff
  LED_PURPLE        = 0xff00ff
  LED_CYAN          = 0xffff
  LED_WHITE         = 0xffffff
  LED_IR            = 0xff000000

Anki.Cozmo.LEDColor = LEDColor
del LEDColor


class LEDColorEncoded(object):
  "Automatically-generated uint_16 enumeration."
  LED_ENC_OFF    = 0x0
  LED_ENC_RED    = 0x7c00
  LED_ENC_GRN    = 0x3e0
  LED_ENC_BLU    = 0x1f
  LED_ENC_YELLOW = 0x7fe0
  LED_ENC_PURPLE = 0x7c1f
  LED_ENC_CYAN   = 0x3ff
  LED_ENC_WHITE  = 0x7fff
  LED_ENC_IR     = 0x8000

Anki.Cozmo.LEDColorEncoded = LEDColorEncoded
del LEDColorEncoded


class LEDColorEncodedShifts(object):
  "Automatically-generated uint_16 enumeration."
  LED_ENC_RED_SHIFT = 10
  LED_ENC_GRN_SHIFT = 5
  LED_ENC_BLU_SHIFT = 0
  LED_ENC_IR_SHIFT  = 15

Anki.Cozmo.LEDColorEncodedShifts = LEDColorEncodedShifts
del LEDColorEncodedShifts


class LightState(object):
  "Generated message-passing structure."

  __slots__ = (
    '_onColor',             # uint_16
    '_offColor',            # uint_16
    '_onFrames',            # uint_8
    '_offFrames',           # uint_8
    '_transitionOnFrames',  # uint_8
    '_transitionOffFrames', # uint_8
    '_offset',              # int_16
  )

  @property
  def onColor(self):
    "uint_16 onColor struct property."
    return self._onColor

  @onColor.setter
  def onColor(self, value):
    self._onColor = msgbuffers.validate_integer(
      'LightState.onColor', value, 0, 65535)

  @property
  def offColor(self):
    "uint_16 offColor struct property."
    return self._offColor

  @offColor.setter
  def offColor(self, value):
    self._offColor = msgbuffers.validate_integer(
      'LightState.offColor', value, 0, 65535)

  @property
  def onFrames(self):
    "uint_8 onFrames struct property."
    return self._onFrames

  @onFrames.setter
  def onFrames(self, value):
    self._onFrames = msgbuffers.validate_integer(
      'LightState.onFrames', value, 0, 255)

  @property
  def offFrames(self):
    "uint_8 offFrames struct property."
    return self._offFrames

  @offFrames.setter
  def offFrames(self, value):
    self._offFrames = msgbuffers.validate_integer(
      'LightState.offFrames', value, 0, 255)

  @property
  def transitionOnFrames(self):
    "uint_8 transitionOnFrames struct property."
    return self._transitionOnFrames

  @transitionOnFrames.setter
  def transitionOnFrames(self, value):
    self._transitionOnFrames = msgbuffers.validate_integer(
      'LightState.transitionOnFrames', value, 0, 255)

  @property
  def transitionOffFrames(self):
    "uint_8 transitionOffFrames struct property."
    return self._transitionOffFrames

  @transitionOffFrames.setter
  def transitionOffFrames(self, value):
    self._transitionOffFrames = msgbuffers.validate_integer(
      'LightState.transitionOffFrames', value, 0, 255)

  @property
  def offset(self):
    "int_16 offset struct property."
    return self._offset

  @offset.setter
  def offset(self, value):
    self._offset = msgbuffers.validate_integer(
      'LightState.offset', value, -32768, 32767)

  def __init__(self, onColor=0, offColor=0, onFrames=0, offFrames=0, transitionOnFrames=0, transitionOffFrames=0, offset=0):
    self.onColor = onColor
    self.offColor = offColor
    self.onFrames = onFrames
    self.offFrames = offFrames
    self.transitionOnFrames = transitionOnFrames
    self.transitionOffFrames = transitionOffFrames
    self.offset = offset

  @classmethod
  def unpack(cls, buffer):
    "Reads a new LightState from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('LightState.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new LightState from the given BinaryReader."
    _onColor = reader.read('H')
    _offColor = reader.read('H')
    _onFrames = reader.read('B')
    _offFrames = reader.read('B')
    _transitionOnFrames = reader.read('B')
    _transitionOffFrames = reader.read('B')
    _offset = reader.read('h')
    return cls(_onColor, _offColor, _onFrames, _offFrames, _transitionOnFrames, _transitionOffFrames, _offset)

  def pack(self):
    "Writes the current LightState, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current LightState to the given BinaryWriter."
    writer.write(self._onColor, 'H')
    writer.write(self._offColor, 'H')
    writer.write(self._onFrames, 'B')
    writer.write(self._offFrames, 'B')
    writer.write(self._transitionOnFrames, 'B')
    writer.write(self._transitionOffFrames, 'B')
    writer.write(self._offset, 'h')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._onColor == other._onColor and
        self._offColor == other._offColor and
        self._onFrames == other._onFrames and
        self._offFrames == other._offFrames and
        self._transitionOnFrames == other._transitionOnFrames and
        self._transitionOffFrames == other._transitionOffFrames and
        self._offset == other._offset)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._onColor, 'H') +
      msgbuffers.size(self._offColor, 'H') +
      msgbuffers.size(self._onFrames, 'B') +
      msgbuffers.size(self._offFrames, 'B') +
      msgbuffers.size(self._transitionOnFrames, 'B') +
      msgbuffers.size(self._transitionOffFrames, 'B') +
      msgbuffers.size(self._offset, 'h'))

  def __str__(self):
    return '{type}(onColor={onColor}, offColor={offColor}, onFrames={onFrames}, offFrames={offFrames}, transitionOnFrames={transitionOnFrames}, transitionOffFrames={transitionOffFrames}, offset={offset})'.format(
      type=type(self).__name__,
      onColor=self._onColor,
      offColor=self._offColor,
      onFrames=self._onFrames,
      offFrames=self._offFrames,
      transitionOnFrames=self._transitionOnFrames,
      transitionOffFrames=self._transitionOffFrames,
      offset=self._offset)

  def __repr__(self):
    return '{type}(onColor={onColor}, offColor={offColor}, onFrames={onFrames}, offFrames={offFrames}, transitionOnFrames={transitionOnFrames}, transitionOffFrames={transitionOffFrames}, offset={offset})'.format(
      type=type(self).__name__,
      onColor=repr(self._onColor),
      offColor=repr(self._offColor),
      onFrames=repr(self._onFrames),
      offFrames=repr(self._offFrames),
      transitionOnFrames=repr(self._transitionOnFrames),
      transitionOffFrames=repr(self._transitionOffFrames),
      offset=repr(self._offset))

Anki.Cozmo.LightState = LightState
del LightState


class WhichCubeLEDs(object):
  "Automatically-generated uint_8 enumeration."
  NONE           = 0x0
  ALL            = 0xff
  BACK           = 0x1
  LEFT           = 0x2
  FRONT          = 0x4
  RIGHT          = 0x8
  FRONT_LEFT     = 0x6
  FRONT_RIGHT    = 0xc
  BACK_LEFT      = 0x3
  BACK_RIGHT     = 0x9
  CHARGER_BACK   = 0x1
  CHARGER_MIDDLE = 0x2
  CHARGER_FRONT  = 0x4

Anki.Cozmo.WhichCubeLEDs = WhichCubeLEDs
del WhichCubeLEDs


class MakeRelativeMode(object):
  "Automatically-generated uint_8 enumeration."
  RELATIVE_LED_MODE_OFF       = 0
  RELATIVE_LED_MODE_BY_CORNER = 1
  RELATIVE_LED_MODE_BY_SIDE   = 2

Anki.Cozmo.MakeRelativeMode = MakeRelativeMode
del MakeRelativeMode


