// Auto-generated. Do not edit!

// (in-package robot_custom_msgs.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class OrderDataRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.start = null;
    }
    else {
      if (initObj.hasOwnProperty('start')) {
        this.start = initObj.start
      }
      else {
        this.start = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type OrderDataRequest
    // Serialize message field [start]
    bufferOffset = _serializer.string(obj.start, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type OrderDataRequest
    let len;
    let data = new OrderDataRequest(null);
    // Deserialize message field [start]
    data.start = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.start.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'robot_custom_msgs/OrderDataRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '34ede85548daeef03201b4a532fb98e1';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    #inputs
    string start
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new OrderDataRequest(null);
    if (msg.start !== undefined) {
      resolved.start = msg.start;
    }
    else {
      resolved.start = ''
    }

    return resolved;
    }
};

class OrderDataResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.raw_id = null;
      this.table_id = null;
      this.order_time = null;
      this.target_pick_position_x = null;
      this.target_pick_position_y = null;
      this.target_pick_position_z = null;
      this.target_pick_orientation_x = null;
      this.target_pick_orientation_y = null;
      this.target_pick_orientation_z = null;
      this.target_pick_orientation_w = null;
      this.target_place_position_x = null;
      this.target_place_position_y = null;
      this.target_place_position_z = null;
      this.target_place_orientation_x = null;
      this.target_place_orientation_y = null;
      this.target_place_orientation_z = null;
      this.target_place_orientation_w = null;
      this.validation_text = null;
    }
    else {
      if (initObj.hasOwnProperty('raw_id')) {
        this.raw_id = initObj.raw_id
      }
      else {
        this.raw_id = 0;
      }
      if (initObj.hasOwnProperty('table_id')) {
        this.table_id = initObj.table_id
      }
      else {
        this.table_id = 0;
      }
      if (initObj.hasOwnProperty('order_time')) {
        this.order_time = initObj.order_time
      }
      else {
        this.order_time = '';
      }
      if (initObj.hasOwnProperty('target_pick_position_x')) {
        this.target_pick_position_x = initObj.target_pick_position_x
      }
      else {
        this.target_pick_position_x = 0.0;
      }
      if (initObj.hasOwnProperty('target_pick_position_y')) {
        this.target_pick_position_y = initObj.target_pick_position_y
      }
      else {
        this.target_pick_position_y = 0.0;
      }
      if (initObj.hasOwnProperty('target_pick_position_z')) {
        this.target_pick_position_z = initObj.target_pick_position_z
      }
      else {
        this.target_pick_position_z = 0.0;
      }
      if (initObj.hasOwnProperty('target_pick_orientation_x')) {
        this.target_pick_orientation_x = initObj.target_pick_orientation_x
      }
      else {
        this.target_pick_orientation_x = 0.0;
      }
      if (initObj.hasOwnProperty('target_pick_orientation_y')) {
        this.target_pick_orientation_y = initObj.target_pick_orientation_y
      }
      else {
        this.target_pick_orientation_y = 0.0;
      }
      if (initObj.hasOwnProperty('target_pick_orientation_z')) {
        this.target_pick_orientation_z = initObj.target_pick_orientation_z
      }
      else {
        this.target_pick_orientation_z = 0.0;
      }
      if (initObj.hasOwnProperty('target_pick_orientation_w')) {
        this.target_pick_orientation_w = initObj.target_pick_orientation_w
      }
      else {
        this.target_pick_orientation_w = 0.0;
      }
      if (initObj.hasOwnProperty('target_place_position_x')) {
        this.target_place_position_x = initObj.target_place_position_x
      }
      else {
        this.target_place_position_x = 0.0;
      }
      if (initObj.hasOwnProperty('target_place_position_y')) {
        this.target_place_position_y = initObj.target_place_position_y
      }
      else {
        this.target_place_position_y = 0.0;
      }
      if (initObj.hasOwnProperty('target_place_position_z')) {
        this.target_place_position_z = initObj.target_place_position_z
      }
      else {
        this.target_place_position_z = 0.0;
      }
      if (initObj.hasOwnProperty('target_place_orientation_x')) {
        this.target_place_orientation_x = initObj.target_place_orientation_x
      }
      else {
        this.target_place_orientation_x = 0.0;
      }
      if (initObj.hasOwnProperty('target_place_orientation_y')) {
        this.target_place_orientation_y = initObj.target_place_orientation_y
      }
      else {
        this.target_place_orientation_y = 0.0;
      }
      if (initObj.hasOwnProperty('target_place_orientation_z')) {
        this.target_place_orientation_z = initObj.target_place_orientation_z
      }
      else {
        this.target_place_orientation_z = 0.0;
      }
      if (initObj.hasOwnProperty('target_place_orientation_w')) {
        this.target_place_orientation_w = initObj.target_place_orientation_w
      }
      else {
        this.target_place_orientation_w = 0.0;
      }
      if (initObj.hasOwnProperty('validation_text')) {
        this.validation_text = initObj.validation_text
      }
      else {
        this.validation_text = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type OrderDataResponse
    // Serialize message field [raw_id]
    bufferOffset = _serializer.int64(obj.raw_id, buffer, bufferOffset);
    // Serialize message field [table_id]
    bufferOffset = _serializer.int64(obj.table_id, buffer, bufferOffset);
    // Serialize message field [order_time]
    bufferOffset = _serializer.string(obj.order_time, buffer, bufferOffset);
    // Serialize message field [target_pick_position_x]
    bufferOffset = _serializer.float64(obj.target_pick_position_x, buffer, bufferOffset);
    // Serialize message field [target_pick_position_y]
    bufferOffset = _serializer.float64(obj.target_pick_position_y, buffer, bufferOffset);
    // Serialize message field [target_pick_position_z]
    bufferOffset = _serializer.float64(obj.target_pick_position_z, buffer, bufferOffset);
    // Serialize message field [target_pick_orientation_x]
    bufferOffset = _serializer.float64(obj.target_pick_orientation_x, buffer, bufferOffset);
    // Serialize message field [target_pick_orientation_y]
    bufferOffset = _serializer.float64(obj.target_pick_orientation_y, buffer, bufferOffset);
    // Serialize message field [target_pick_orientation_z]
    bufferOffset = _serializer.float64(obj.target_pick_orientation_z, buffer, bufferOffset);
    // Serialize message field [target_pick_orientation_w]
    bufferOffset = _serializer.float64(obj.target_pick_orientation_w, buffer, bufferOffset);
    // Serialize message field [target_place_position_x]
    bufferOffset = _serializer.float64(obj.target_place_position_x, buffer, bufferOffset);
    // Serialize message field [target_place_position_y]
    bufferOffset = _serializer.float64(obj.target_place_position_y, buffer, bufferOffset);
    // Serialize message field [target_place_position_z]
    bufferOffset = _serializer.float64(obj.target_place_position_z, buffer, bufferOffset);
    // Serialize message field [target_place_orientation_x]
    bufferOffset = _serializer.float64(obj.target_place_orientation_x, buffer, bufferOffset);
    // Serialize message field [target_place_orientation_y]
    bufferOffset = _serializer.float64(obj.target_place_orientation_y, buffer, bufferOffset);
    // Serialize message field [target_place_orientation_z]
    bufferOffset = _serializer.float64(obj.target_place_orientation_z, buffer, bufferOffset);
    // Serialize message field [target_place_orientation_w]
    bufferOffset = _serializer.float64(obj.target_place_orientation_w, buffer, bufferOffset);
    // Serialize message field [validation_text]
    bufferOffset = _serializer.string(obj.validation_text, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type OrderDataResponse
    let len;
    let data = new OrderDataResponse(null);
    // Deserialize message field [raw_id]
    data.raw_id = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [table_id]
    data.table_id = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [order_time]
    data.order_time = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [target_pick_position_x]
    data.target_pick_position_x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [target_pick_position_y]
    data.target_pick_position_y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [target_pick_position_z]
    data.target_pick_position_z = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [target_pick_orientation_x]
    data.target_pick_orientation_x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [target_pick_orientation_y]
    data.target_pick_orientation_y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [target_pick_orientation_z]
    data.target_pick_orientation_z = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [target_pick_orientation_w]
    data.target_pick_orientation_w = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [target_place_position_x]
    data.target_place_position_x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [target_place_position_y]
    data.target_place_position_y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [target_place_position_z]
    data.target_place_position_z = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [target_place_orientation_x]
    data.target_place_orientation_x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [target_place_orientation_y]
    data.target_place_orientation_y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [target_place_orientation_z]
    data.target_place_orientation_z = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [target_place_orientation_w]
    data.target_place_orientation_w = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [validation_text]
    data.validation_text = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.order_time.length;
    length += object.validation_text.length;
    return length + 136;
  }

  static datatype() {
    // Returns string type for a service object
    return 'robot_custom_msgs/OrderDataResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2d0e503dd50b9e8afd392ac3fc21b7af';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    #output
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
    
    
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new OrderDataResponse(null);
    if (msg.raw_id !== undefined) {
      resolved.raw_id = msg.raw_id;
    }
    else {
      resolved.raw_id = 0
    }

    if (msg.table_id !== undefined) {
      resolved.table_id = msg.table_id;
    }
    else {
      resolved.table_id = 0
    }

    if (msg.order_time !== undefined) {
      resolved.order_time = msg.order_time;
    }
    else {
      resolved.order_time = ''
    }

    if (msg.target_pick_position_x !== undefined) {
      resolved.target_pick_position_x = msg.target_pick_position_x;
    }
    else {
      resolved.target_pick_position_x = 0.0
    }

    if (msg.target_pick_position_y !== undefined) {
      resolved.target_pick_position_y = msg.target_pick_position_y;
    }
    else {
      resolved.target_pick_position_y = 0.0
    }

    if (msg.target_pick_position_z !== undefined) {
      resolved.target_pick_position_z = msg.target_pick_position_z;
    }
    else {
      resolved.target_pick_position_z = 0.0
    }

    if (msg.target_pick_orientation_x !== undefined) {
      resolved.target_pick_orientation_x = msg.target_pick_orientation_x;
    }
    else {
      resolved.target_pick_orientation_x = 0.0
    }

    if (msg.target_pick_orientation_y !== undefined) {
      resolved.target_pick_orientation_y = msg.target_pick_orientation_y;
    }
    else {
      resolved.target_pick_orientation_y = 0.0
    }

    if (msg.target_pick_orientation_z !== undefined) {
      resolved.target_pick_orientation_z = msg.target_pick_orientation_z;
    }
    else {
      resolved.target_pick_orientation_z = 0.0
    }

    if (msg.target_pick_orientation_w !== undefined) {
      resolved.target_pick_orientation_w = msg.target_pick_orientation_w;
    }
    else {
      resolved.target_pick_orientation_w = 0.0
    }

    if (msg.target_place_position_x !== undefined) {
      resolved.target_place_position_x = msg.target_place_position_x;
    }
    else {
      resolved.target_place_position_x = 0.0
    }

    if (msg.target_place_position_y !== undefined) {
      resolved.target_place_position_y = msg.target_place_position_y;
    }
    else {
      resolved.target_place_position_y = 0.0
    }

    if (msg.target_place_position_z !== undefined) {
      resolved.target_place_position_z = msg.target_place_position_z;
    }
    else {
      resolved.target_place_position_z = 0.0
    }

    if (msg.target_place_orientation_x !== undefined) {
      resolved.target_place_orientation_x = msg.target_place_orientation_x;
    }
    else {
      resolved.target_place_orientation_x = 0.0
    }

    if (msg.target_place_orientation_y !== undefined) {
      resolved.target_place_orientation_y = msg.target_place_orientation_y;
    }
    else {
      resolved.target_place_orientation_y = 0.0
    }

    if (msg.target_place_orientation_z !== undefined) {
      resolved.target_place_orientation_z = msg.target_place_orientation_z;
    }
    else {
      resolved.target_place_orientation_z = 0.0
    }

    if (msg.target_place_orientation_w !== undefined) {
      resolved.target_place_orientation_w = msg.target_place_orientation_w;
    }
    else {
      resolved.target_place_orientation_w = 0.0
    }

    if (msg.validation_text !== undefined) {
      resolved.validation_text = msg.validation_text;
    }
    else {
      resolved.validation_text = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: OrderDataRequest,
  Response: OrderDataResponse,
  md5sum() { return '9c311561e0acab097731704c85ada1aa'; },
  datatype() { return 'robot_custom_msgs/OrderData'; }
};
