# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from robot_custom_msgs/dbRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class dbRequest(genpy.Message):
  _md5sum = "34ede85548daeef03201b4a532fb98e1"
  _type = "robot_custom_msgs/dbRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """#inputs
string start

"""
  __slots__ = ['start']
  _slot_types = ['string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       start

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(dbRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.start is None:
        self.start = ''
    else:
      self.start = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.start
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.start = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.start = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.start
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.start = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.start = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from robot_custom_msgs/dbResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class dbResponse(genpy.Message):
  _md5sum = "2d0e503dd50b9e8afd392ac3fc21b7af"
  _type = "robot_custom_msgs/dbResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """#output
int64 raw_id
int64 table_id
string order_time

float64 target_pick_position_x
float64 target_pick_position_y
float64 target_pick_position_z

float64 target_pick_orientation_x
float64 target_pick_orientation_y
float64 target_pick_orientation_z
float64 target_pick_orientation_w

float64 target_place_position_x
float64 target_place_position_y
float64 target_place_position_z

float64 target_place_orientation_x
float64 target_place_orientation_y
float64 target_place_orientation_z
float64 target_place_orientation_w

string validation_text



"""
  __slots__ = ['raw_id','table_id','order_time','target_pick_position_x','target_pick_position_y','target_pick_position_z','target_pick_orientation_x','target_pick_orientation_y','target_pick_orientation_z','target_pick_orientation_w','target_place_position_x','target_place_position_y','target_place_position_z','target_place_orientation_x','target_place_orientation_y','target_place_orientation_z','target_place_orientation_w','validation_text']
  _slot_types = ['int64','int64','string','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       raw_id,table_id,order_time,target_pick_position_x,target_pick_position_y,target_pick_position_z,target_pick_orientation_x,target_pick_orientation_y,target_pick_orientation_z,target_pick_orientation_w,target_place_position_x,target_place_position_y,target_place_position_z,target_place_orientation_x,target_place_orientation_y,target_place_orientation_z,target_place_orientation_w,validation_text

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(dbResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.raw_id is None:
        self.raw_id = 0
      if self.table_id is None:
        self.table_id = 0
      if self.order_time is None:
        self.order_time = ''
      if self.target_pick_position_x is None:
        self.target_pick_position_x = 0.
      if self.target_pick_position_y is None:
        self.target_pick_position_y = 0.
      if self.target_pick_position_z is None:
        self.target_pick_position_z = 0.
      if self.target_pick_orientation_x is None:
        self.target_pick_orientation_x = 0.
      if self.target_pick_orientation_y is None:
        self.target_pick_orientation_y = 0.
      if self.target_pick_orientation_z is None:
        self.target_pick_orientation_z = 0.
      if self.target_pick_orientation_w is None:
        self.target_pick_orientation_w = 0.
      if self.target_place_position_x is None:
        self.target_place_position_x = 0.
      if self.target_place_position_y is None:
        self.target_place_position_y = 0.
      if self.target_place_position_z is None:
        self.target_place_position_z = 0.
      if self.target_place_orientation_x is None:
        self.target_place_orientation_x = 0.
      if self.target_place_orientation_y is None:
        self.target_place_orientation_y = 0.
      if self.target_place_orientation_z is None:
        self.target_place_orientation_z = 0.
      if self.target_place_orientation_w is None:
        self.target_place_orientation_w = 0.
      if self.validation_text is None:
        self.validation_text = ''
    else:
      self.raw_id = 0
      self.table_id = 0
      self.order_time = ''
      self.target_pick_position_x = 0.
      self.target_pick_position_y = 0.
      self.target_pick_position_z = 0.
      self.target_pick_orientation_x = 0.
      self.target_pick_orientation_y = 0.
      self.target_pick_orientation_z = 0.
      self.target_pick_orientation_w = 0.
      self.target_place_position_x = 0.
      self.target_place_position_y = 0.
      self.target_place_position_z = 0.
      self.target_place_orientation_x = 0.
      self.target_place_orientation_y = 0.
      self.target_place_orientation_z = 0.
      self.target_place_orientation_w = 0.
      self.validation_text = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_2q().pack(_x.raw_id, _x.table_id))
      _x = self.order_time
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_14d().pack(_x.target_pick_position_x, _x.target_pick_position_y, _x.target_pick_position_z, _x.target_pick_orientation_x, _x.target_pick_orientation_y, _x.target_pick_orientation_z, _x.target_pick_orientation_w, _x.target_place_position_x, _x.target_place_position_y, _x.target_place_position_z, _x.target_place_orientation_x, _x.target_place_orientation_y, _x.target_place_orientation_z, _x.target_place_orientation_w))
      _x = self.validation_text
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 16
      (_x.raw_id, _x.table_id,) = _get_struct_2q().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.order_time = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.order_time = str[start:end]
      _x = self
      start = end
      end += 112
      (_x.target_pick_position_x, _x.target_pick_position_y, _x.target_pick_position_z, _x.target_pick_orientation_x, _x.target_pick_orientation_y, _x.target_pick_orientation_z, _x.target_pick_orientation_w, _x.target_place_position_x, _x.target_place_position_y, _x.target_place_position_z, _x.target_place_orientation_x, _x.target_place_orientation_y, _x.target_place_orientation_z, _x.target_place_orientation_w,) = _get_struct_14d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.validation_text = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.validation_text = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_2q().pack(_x.raw_id, _x.table_id))
      _x = self.order_time
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_14d().pack(_x.target_pick_position_x, _x.target_pick_position_y, _x.target_pick_position_z, _x.target_pick_orientation_x, _x.target_pick_orientation_y, _x.target_pick_orientation_z, _x.target_pick_orientation_w, _x.target_place_position_x, _x.target_place_position_y, _x.target_place_position_z, _x.target_place_orientation_x, _x.target_place_orientation_y, _x.target_place_orientation_z, _x.target_place_orientation_w))
      _x = self.validation_text
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 16
      (_x.raw_id, _x.table_id,) = _get_struct_2q().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.order_time = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.order_time = str[start:end]
      _x = self
      start = end
      end += 112
      (_x.target_pick_position_x, _x.target_pick_position_y, _x.target_pick_position_z, _x.target_pick_orientation_x, _x.target_pick_orientation_y, _x.target_pick_orientation_z, _x.target_pick_orientation_w, _x.target_place_position_x, _x.target_place_position_y, _x.target_place_position_z, _x.target_place_orientation_x, _x.target_place_orientation_y, _x.target_place_orientation_z, _x.target_place_orientation_w,) = _get_struct_14d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.validation_text = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.validation_text = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_14d = None
def _get_struct_14d():
    global _struct_14d
    if _struct_14d is None:
        _struct_14d = struct.Struct("<14d")
    return _struct_14d
_struct_2q = None
def _get_struct_2q():
    global _struct_2q
    if _struct_2q is None:
        _struct_2q = struct.Struct("<2q")
    return _struct_2q
class db(object):
  _type          = 'robot_custom_msgs/db'
  _md5sum = '9c311561e0acab097731704c85ada1aa'
  _request_class  = dbRequest
  _response_class = dbResponse
