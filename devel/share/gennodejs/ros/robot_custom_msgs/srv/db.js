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

class dbRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.id = null;
    }
    else {
      if (initObj.hasOwnProperty('id')) {
        this.id = initObj.id
      }
      else {
        this.id = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type dbRequest
    // Serialize message field [id]
    bufferOffset = _serializer.int64(obj.id, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type dbRequest
    let len;
    let data = new dbRequest(null);
    // Deserialize message field [id]
    data.id = _deserializer.int64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'robot_custom_msgs/dbRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ef7df1d34137d3879d089ad803388efa';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    #inputs
    int64 id
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new dbRequest(null);
    if (msg.id !== undefined) {
      resolved.id = msg.id;
    }
    else {
      resolved.id = 0
    }

    return resolved;
    }
};

class dbResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.tableid = null;
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
      this.text = null;
    }
    else {
      if (initObj.hasOwnProperty('tableid')) {
        this.tableid = initObj.tableid
      }
      else {
        this.tableid = 0;
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
      if (initObj.hasOwnProperty('text')) {
        this.text = initObj.text
      }
      else {
        this.text = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type dbResponse
    // Serialize message field [tableid]
    bufferOffset = _serializer.int64(obj.tableid, buffer, bufferOffset);
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
    // Serialize message field [text]
    bufferOffset = _serializer.string(obj.text, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type dbResponse
    let len;
    let data = new dbResponse(null);
    // Deserialize message field [tableid]
    data.tableid = _deserializer.int64(buffer, bufferOffset);
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
    // Deserialize message field [text]
    data.text = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.text.length;
    return length + 124;
  }

  static datatype() {
    // Returns string type for a service object
    return 'robot_custom_msgs/dbResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd43bda5143fd7d192dd6191338cdba5e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    #output
    int64 tableid
    
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
    
    string text
    
    
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new dbResponse(null);
    if (msg.tableid !== undefined) {
      resolved.tableid = msg.tableid;
    }
    else {
      resolved.tableid = 0
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

    if (msg.text !== undefined) {
      resolved.text = msg.text;
    }
    else {
      resolved.text = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: dbRequest,
  Response: dbResponse,
  md5sum() { return '0b56db4429947d5d82235b9718d8f033'; },
  datatype() { return 'robot_custom_msgs/db'; }
};
