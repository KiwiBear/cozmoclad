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
Source: clad/audio/audioCallbackMessage.clad
Full command line: ../tools/message-buffers/emitters/Python_emitter.py -C ./src/ -I ../robot/clad/src/ ../coretech/vision/clad/src/ ../coretech/common/clad/src/ ../lib/util/source/anki/clad -o ../generated/cladPython// clad/audio/audioCallbackMessage.clad
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
Anki.AudioEngine = msgbuffers.Namespace()
Anki.AudioEngine.Multiplexer = msgbuffers.Namespace()
Anki.AudioMetaData = msgbuffers.Namespace()
Anki.AudioMetaData.GameEvent = msgbuffers.Namespace()

from clad.audio.audioEventTypes import Anki as _Anki
Anki.update(_Anki.deep_clone())

class AudioCallbackDuration(object):
  "Generated message-passing structure."

  __slots__ = (
    '_duration',          # float_32
    '_estimatedDuration', # float_32
    '_audioNodeId',       # uint_32
    '_isStreaming',       # bool
  )

  @property
  def duration(self):
    "float_32 duration struct property."
    return self._duration

  @duration.setter
  def duration(self, value):
    self._duration = msgbuffers.validate_float(
      'AudioCallbackDuration.duration', value, 'f')

  @property
  def estimatedDuration(self):
    "float_32 estimatedDuration struct property."
    return self._estimatedDuration

  @estimatedDuration.setter
  def estimatedDuration(self, value):
    self._estimatedDuration = msgbuffers.validate_float(
      'AudioCallbackDuration.estimatedDuration', value, 'f')

  @property
  def audioNodeId(self):
    "uint_32 audioNodeId struct property."
    return self._audioNodeId

  @audioNodeId.setter
  def audioNodeId(self, value):
    self._audioNodeId = msgbuffers.validate_integer(
      'AudioCallbackDuration.audioNodeId', value, 0, 4294967295)

  @property
  def isStreaming(self):
    "bool isStreaming struct property."
    return self._isStreaming

  @isStreaming.setter
  def isStreaming(self, value):
    self._isStreaming = msgbuffers.validate_bool(
      'AudioCallbackDuration.isStreaming', value)

  def __init__(self, duration=0.0, estimatedDuration=0.0, audioNodeId=0, isStreaming=False):
    self.duration = duration
    self.estimatedDuration = estimatedDuration
    self.audioNodeId = audioNodeId
    self.isStreaming = isStreaming

  @classmethod
  def unpack(cls, buffer):
    "Reads a new AudioCallbackDuration from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('AudioCallbackDuration.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new AudioCallbackDuration from the given BinaryReader."
    _duration = reader.read('f')
    _estimatedDuration = reader.read('f')
    _audioNodeId = reader.read('I')
    _isStreaming = bool(reader.read('b'))
    return cls(_duration, _estimatedDuration, _audioNodeId, _isStreaming)

  def pack(self):
    "Writes the current AudioCallbackDuration, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current AudioCallbackDuration to the given BinaryWriter."
    writer.write(self._duration, 'f')
    writer.write(self._estimatedDuration, 'f')
    writer.write(self._audioNodeId, 'I')
    writer.write(int(self._isStreaming), 'b')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._duration == other._duration and
        self._estimatedDuration == other._estimatedDuration and
        self._audioNodeId == other._audioNodeId and
        self._isStreaming == other._isStreaming)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._duration, 'f') +
      msgbuffers.size(self._estimatedDuration, 'f') +
      msgbuffers.size(self._audioNodeId, 'I') +
      msgbuffers.size(self._isStreaming, 'b'))

  def __str__(self):
    return '{type}(duration={duration}, estimatedDuration={estimatedDuration}, audioNodeId={audioNodeId}, isStreaming={isStreaming})'.format(
      type=type(self).__name__,
      duration=self._duration,
      estimatedDuration=self._estimatedDuration,
      audioNodeId=self._audioNodeId,
      isStreaming=self._isStreaming)

  def __repr__(self):
    return '{type}(duration={duration}, estimatedDuration={estimatedDuration}, audioNodeId={audioNodeId}, isStreaming={isStreaming})'.format(
      type=type(self).__name__,
      duration=repr(self._duration),
      estimatedDuration=repr(self._estimatedDuration),
      audioNodeId=repr(self._audioNodeId),
      isStreaming=repr(self._isStreaming))

Anki.AudioEngine.Multiplexer.AudioCallbackDuration = AudioCallbackDuration
del AudioCallbackDuration


class AudioCallbackMarker(object):
  "Generated message-passing structure."

  __slots__ = (
    '_identifier', # uint_32
    '_position',   # uint_32
    '_labelTitle', # string[uint_8]
  )

  @property
  def identifier(self):
    "uint_32 identifier struct property."
    return self._identifier

  @identifier.setter
  def identifier(self, value):
    self._identifier = msgbuffers.validate_integer(
      'AudioCallbackMarker.identifier', value, 0, 4294967295)

  @property
  def position(self):
    "uint_32 position struct property."
    return self._position

  @position.setter
  def position(self, value):
    self._position = msgbuffers.validate_integer(
      'AudioCallbackMarker.position', value, 0, 4294967295)

  @property
  def labelTitle(self):
    "string[uint_8] labelTitle struct property."
    return self._labelTitle

  @labelTitle.setter
  def labelTitle(self, value):
    self._labelTitle = msgbuffers.validate_string(
      'AudioCallbackMarker.labelTitle', value, 255)

  def __init__(self, identifier=0, position=0, labelTitle=''):
    self.identifier = identifier
    self.position = position
    self.labelTitle = labelTitle

  @classmethod
  def unpack(cls, buffer):
    "Reads a new AudioCallbackMarker from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('AudioCallbackMarker.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new AudioCallbackMarker from the given BinaryReader."
    _identifier = reader.read('I')
    _position = reader.read('I')
    _labelTitle = reader.read_string('B')
    return cls(_identifier, _position, _labelTitle)

  def pack(self):
    "Writes the current AudioCallbackMarker, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current AudioCallbackMarker to the given BinaryWriter."
    writer.write(self._identifier, 'I')
    writer.write(self._position, 'I')
    writer.write_string(self._labelTitle, 'B')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._identifier == other._identifier and
        self._position == other._position and
        self._labelTitle == other._labelTitle)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._identifier, 'I') +
      msgbuffers.size(self._position, 'I') +
      msgbuffers.size_string(self._labelTitle, 'B'))

  def __str__(self):
    return '{type}(identifier={identifier}, position={position}, labelTitle={labelTitle})'.format(
      type=type(self).__name__,
      identifier=self._identifier,
      position=self._position,
      labelTitle=msgbuffers.shorten_string(self._labelTitle))

  def __repr__(self):
    return '{type}(identifier={identifier}, position={position}, labelTitle={labelTitle})'.format(
      type=type(self).__name__,
      identifier=repr(self._identifier),
      position=repr(self._position),
      labelTitle=repr(self._labelTitle))

Anki.AudioEngine.Multiplexer.AudioCallbackMarker = AudioCallbackMarker
del AudioCallbackMarker


class AudioCallbackComplete(object):
  "Generated message-passing structure."

  __slots__ = (
    '_eventType', # Anki.AudioMetaData.GameEvent.GenericEvent
  )

  @property
  def eventType(self):
    "Anki.AudioMetaData.GameEvent.GenericEvent eventType struct property."
    return self._eventType

  @eventType.setter
  def eventType(self, value):
    self._eventType = msgbuffers.validate_integer(
      'AudioCallbackComplete.eventType', value, 0, 4294967295)

  def __init__(self, eventType=Anki.AudioMetaData.GameEvent.GenericEvent.Invalid):
    self.eventType = eventType

  @classmethod
  def unpack(cls, buffer):
    "Reads a new AudioCallbackComplete from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('AudioCallbackComplete.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new AudioCallbackComplete from the given BinaryReader."
    _eventType = reader.read('I')
    return cls(_eventType)

  def pack(self):
    "Writes the current AudioCallbackComplete, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current AudioCallbackComplete to the given BinaryWriter."
    writer.write(self._eventType, 'I')

  def __eq__(self, other):
    if type(self) is type(other):
      return self._eventType == other._eventType
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._eventType, 'I'))

  def __str__(self):
    return '{type}(eventType={eventType})'.format(
      type=type(self).__name__,
      eventType=self._eventType)

  def __repr__(self):
    return '{type}(eventType={eventType})'.format(
      type=type(self).__name__,
      eventType=repr(self._eventType))

Anki.AudioEngine.Multiplexer.AudioCallbackComplete = AudioCallbackComplete
del AudioCallbackComplete


class CallbackErrorType(object):
  "Automatically-generated uint_8 enumeration."
  Invalid     = 0
  EventFailed = 1
  Starvation  = 2

Anki.AudioEngine.Multiplexer.CallbackErrorType = CallbackErrorType
del CallbackErrorType


class AudioCallbackError(object):
  "Generated message-passing structure."

  __slots__ = (
    '_callbackError', # Anki.AudioEngine.Multiplexer.CallbackErrorType
  )

  @property
  def callbackError(self):
    "Anki.AudioEngine.Multiplexer.CallbackErrorType callbackError struct property."
    return self._callbackError

  @callbackError.setter
  def callbackError(self, value):
    self._callbackError = msgbuffers.validate_integer(
      'AudioCallbackError.callbackError', value, 0, 255)

  def __init__(self, callbackError=Anki.AudioEngine.Multiplexer.CallbackErrorType.Invalid):
    self.callbackError = callbackError

  @classmethod
  def unpack(cls, buffer):
    "Reads a new AudioCallbackError from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('AudioCallbackError.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new AudioCallbackError from the given BinaryReader."
    _callbackError = reader.read('B')
    return cls(_callbackError)

  def pack(self):
    "Writes the current AudioCallbackError, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current AudioCallbackError to the given BinaryWriter."
    writer.write(self._callbackError, 'B')

  def __eq__(self, other):
    if type(self) is type(other):
      return self._callbackError == other._callbackError
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._callbackError, 'B'))

  def __str__(self):
    return '{type}(callbackError={callbackError})'.format(
      type=type(self).__name__,
      callbackError=self._callbackError)

  def __repr__(self):
    return '{type}(callbackError={callbackError})'.format(
      type=type(self).__name__,
      callbackError=repr(self._callbackError))

Anki.AudioEngine.Multiplexer.AudioCallbackError = AudioCallbackError
del AudioCallbackError


class AudioCallbackInfo(object):
  "Generated message-passing union."

  __slots__ = ('_tag', '_data')

  class Tag(object):
    "The type indicator for this union."
    callbackDuration = 0 # Anki.AudioEngine.Multiplexer.AudioCallbackDuration
    callbackMarker   = 1 # Anki.AudioEngine.Multiplexer.AudioCallbackMarker
    callbackComplete = 2 # Anki.AudioEngine.Multiplexer.AudioCallbackComplete
    callbackError    = 3 # Anki.AudioEngine.Multiplexer.AudioCallbackError

  @property
  def tag(self):
    "The current tag for this union."
    return self._tag

  @property
  def tag_name(self):
    "The name of the current tag for this union."
    if self._tag in self._tags_by_value:
      return self._tags_by_value[self._tag]
    else:
      return None

  @property
  def data(self):
    "The data held by this union. None if no data is set."
    return self._data

  @property
  def callbackDuration(self):
    "Anki.AudioEngine.Multiplexer.AudioCallbackDuration callbackDuration union property."
    msgbuffers.safety_check_tag('callbackDuration', self._tag, self.Tag.callbackDuration, self._tags_by_value)
    return self._data

  @callbackDuration.setter
  def callbackDuration(self, value):
    self._data = msgbuffers.validate_object(
      'AudioCallbackInfo.callbackDuration', value, Anki.AudioEngine.Multiplexer.AudioCallbackDuration)
    self._tag = self.Tag.callbackDuration

  @property
  def callbackMarker(self):
    "Anki.AudioEngine.Multiplexer.AudioCallbackMarker callbackMarker union property."
    msgbuffers.safety_check_tag('callbackMarker', self._tag, self.Tag.callbackMarker, self._tags_by_value)
    return self._data

  @callbackMarker.setter
  def callbackMarker(self, value):
    self._data = msgbuffers.validate_object(
      'AudioCallbackInfo.callbackMarker', value, Anki.AudioEngine.Multiplexer.AudioCallbackMarker)
    self._tag = self.Tag.callbackMarker

  @property
  def callbackComplete(self):
    "Anki.AudioEngine.Multiplexer.AudioCallbackComplete callbackComplete union property."
    msgbuffers.safety_check_tag('callbackComplete', self._tag, self.Tag.callbackComplete, self._tags_by_value)
    return self._data

  @callbackComplete.setter
  def callbackComplete(self, value):
    self._data = msgbuffers.validate_object(
      'AudioCallbackInfo.callbackComplete', value, Anki.AudioEngine.Multiplexer.AudioCallbackComplete)
    self._tag = self.Tag.callbackComplete

  @property
  def callbackError(self):
    "Anki.AudioEngine.Multiplexer.AudioCallbackError callbackError union property."
    msgbuffers.safety_check_tag('callbackError', self._tag, self.Tag.callbackError, self._tags_by_value)
    return self._data

  @callbackError.setter
  def callbackError(self, value):
    self._data = msgbuffers.validate_object(
      'AudioCallbackInfo.callbackError', value, Anki.AudioEngine.Multiplexer.AudioCallbackError)
    self._tag = self.Tag.callbackError

  def __init__(self, **kwargs):
    if not kwargs:
      self._tag = None
      self._data = None

    elif len(kwargs) == 1:
      key, value = next(iter(kwargs.items()))
      if key not in self._tags_by_name:
        raise TypeError("'{argument}' is an invalid keyword argument for this method.".format(argument=key))
      # calls the correct property
      setattr(self, key, value)

    else:
      raise TypeError('This method only accepts up to one keyword argument.')

  @classmethod
  def unpack(cls, buffer):
    "Reads a new AudioCallbackInfo from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('AudioCallbackInfo.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new AudioCallbackInfo from the given BinaryReader."
    tag = reader.read('B')
    if tag in cls._tags_by_value:
      value = cls()
      setattr(value, cls._tags_by_value[tag], cls._tag_unpack_methods[tag](reader))
      return value
    else:
      raise ValueError('AudioCallbackInfo attempted to unpack unknown tag {tag}.'.format(tag=tag))

  def pack(self):
    "Writes the current AudioCallbackInfo, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current SampleUnion to the given BinaryWriter."
    if self._tag in self._tags_by_value:
      writer.write(self._tag, 'B')
      self._tag_pack_methods[self._tag](writer, self._data)
    else:
      raise ValueError('Cannot pack an empty AudioCallbackInfo.')

  def clear(self):
    self._tag = None
    self._data = None

  @classmethod
  def typeByTag(cls, tag):
    return cls._type_by_tag_value[tag]()

  def __eq__(self, other):
    if type(self) is type(other):
      return self._tag == other._tag and self._data == other._data
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    if 0 <= self._tag < 4:
      return self._tag_size_methods[self._tag](self._data)
    else:
      return 1

  def __str__(self):
    if 0 <= self._tag < 4:
      return '{type}({name}={value})'.format(
        type=type(self).__name__,
        name=self.tag_name,
        value=self._data)
    else:
      return '{type}()'.format(
        type=type(self).__name__)

  def __repr__(self):
    if 0 <= self._tag < 4:
      return '{type}({name}={value})'.format(
        type=type(self).__name__,
        name=self.tag_name,
        value=repr(self._data))
    else:
      return '{type}()'.format(
        type=type(self).__name__)

  _tags_by_name = dict(
    callbackDuration=0,
    callbackMarker=1,
    callbackComplete=2,
    callbackError=3,
  )

  _tags_by_value = dict()
  _tags_by_value[0] = 'callbackDuration'
  _tags_by_value[1] = 'callbackMarker'
  _tags_by_value[2] = 'callbackComplete'
  _tags_by_value[3] = 'callbackError'
  

  _tag_unpack_methods = dict()
  _tag_unpack_methods[0] = lambda reader: reader.read_object(Anki.AudioEngine.Multiplexer.AudioCallbackDuration.unpack_from)
  _tag_unpack_methods[1] = lambda reader: reader.read_object(Anki.AudioEngine.Multiplexer.AudioCallbackMarker.unpack_from)
  _tag_unpack_methods[2] = lambda reader: reader.read_object(Anki.AudioEngine.Multiplexer.AudioCallbackComplete.unpack_from)
  _tag_unpack_methods[3] = lambda reader: reader.read_object(Anki.AudioEngine.Multiplexer.AudioCallbackError.unpack_from)
  

  _tag_pack_methods = dict()
  _tag_pack_methods[0] = lambda writer, value: writer.write_object(value)
  _tag_pack_methods[1] = lambda writer, value: writer.write_object(value)
  _tag_pack_methods[2] = lambda writer, value: writer.write_object(value)
  _tag_pack_methods[3] = lambda writer, value: writer.write_object(value)
  

  _tag_size_methods = dict()
  _tag_size_methods[0] = lambda value: msgbuffers.size_object(value)
  _tag_size_methods[1] = lambda value: msgbuffers.size_object(value)
  _tag_size_methods[2] = lambda value: msgbuffers.size_object(value)
  _tag_size_methods[3] = lambda value: msgbuffers.size_object(value)
  

  _type_by_tag_value = dict()
  _type_by_tag_value[0] = lambda : Anki.AudioEngine.Multiplexer.AudioCallbackDuration
  _type_by_tag_value[1] = lambda : Anki.AudioEngine.Multiplexer.AudioCallbackMarker
  _type_by_tag_value[2] = lambda : Anki.AudioEngine.Multiplexer.AudioCallbackComplete
  _type_by_tag_value[3] = lambda : Anki.AudioEngine.Multiplexer.AudioCallbackError
  

Anki.AudioEngine.Multiplexer.AudioCallbackInfo = AudioCallbackInfo
del AudioCallbackInfo


class AudioCallback(object):
  "Generated message-passing message."

  __slots__ = (
    '_callbackId',   # uint_16
    '_callbackInfo', # Anki.AudioEngine.Multiplexer.AudioCallbackInfo
  )

  @property
  def callbackId(self):
    "uint_16 callbackId struct property."
    return self._callbackId

  @callbackId.setter
  def callbackId(self, value):
    self._callbackId = msgbuffers.validate_integer(
      'AudioCallback.callbackId', value, 0, 65535)

  @property
  def callbackInfo(self):
    "Anki.AudioEngine.Multiplexer.AudioCallbackInfo callbackInfo struct property."
    return self._callbackInfo

  @callbackInfo.setter
  def callbackInfo(self, value):
    self._callbackInfo = msgbuffers.validate_object(
      'AudioCallback.callbackInfo', value, Anki.AudioEngine.Multiplexer.AudioCallbackInfo)

  def __init__(self, callbackId=0, callbackInfo=Anki.AudioEngine.Multiplexer.AudioCallbackInfo()):
    self.callbackId = callbackId
    self.callbackInfo = callbackInfo

  @classmethod
  def unpack(cls, buffer):
    "Reads a new AudioCallback from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('AudioCallback.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new AudioCallback from the given BinaryReader."
    _callbackId = reader.read('H')
    _callbackInfo = reader.read_object(Anki.AudioEngine.Multiplexer.AudioCallbackInfo.unpack_from)
    return cls(_callbackId, _callbackInfo)

  def pack(self):
    "Writes the current AudioCallback, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current AudioCallback to the given BinaryWriter."
    writer.write(self._callbackId, 'H')
    writer.write_object(self._callbackInfo)

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._callbackId == other._callbackId and
        self._callbackInfo == other._callbackInfo)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._callbackId, 'H') +
      msgbuffers.size_object(self._callbackInfo))

  def __str__(self):
    return '{type}(callbackId={callbackId}, callbackInfo={callbackInfo})'.format(
      type=type(self).__name__,
      callbackId=self._callbackId,
      callbackInfo=self._callbackInfo)

  def __repr__(self):
    return '{type}(callbackId={callbackId}, callbackInfo={callbackInfo})'.format(
      type=type(self).__name__,
      callbackId=repr(self._callbackId),
      callbackInfo=repr(self._callbackInfo))

Anki.AudioEngine.Multiplexer.AudioCallback = AudioCallback
del AudioCallback

