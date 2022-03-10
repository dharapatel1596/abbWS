; Auto-generated. Do not edit!


(cl:in-package robot_custom_msgs-srv)


;//! \htmlinclude db-request.msg.html

(cl:defclass <db-request> (roslisp-msg-protocol:ros-message)
  ((id
    :reader id
    :initarg :id
    :type cl:integer
    :initform 0))
)

(cl:defclass db-request (<db-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <db-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'db-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_custom_msgs-srv:<db-request> is deprecated: use robot_custom_msgs-srv:db-request instead.")))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <db-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:id-val is deprecated.  Use robot_custom_msgs-srv:id instead.")
  (id m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <db-request>) ostream)
  "Serializes a message object of type '<db-request>"
  (cl:let* ((signed (cl:slot-value msg 'id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <db-request>) istream)
  "Deserializes a message object of type '<db-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'id) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<db-request>)))
  "Returns string type for a service object of type '<db-request>"
  "robot_custom_msgs/dbRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'db-request)))
  "Returns string type for a service object of type 'db-request"
  "robot_custom_msgs/dbRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<db-request>)))
  "Returns md5sum for a message object of type '<db-request>"
  "0b56db4429947d5d82235b9718d8f033")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'db-request)))
  "Returns md5sum for a message object of type 'db-request"
  "0b56db4429947d5d82235b9718d8f033")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<db-request>)))
  "Returns full string definition for message of type '<db-request>"
  (cl:format cl:nil "#inputs~%int64 id~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'db-request)))
  "Returns full string definition for message of type 'db-request"
  (cl:format cl:nil "#inputs~%int64 id~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <db-request>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <db-request>))
  "Converts a ROS message object to a list"
  (cl:list 'db-request
    (cl:cons ':id (id msg))
))
;//! \htmlinclude db-response.msg.html

(cl:defclass <db-response> (roslisp-msg-protocol:ros-message)
  ((tableid
    :reader tableid
    :initarg :tableid
    :type cl:integer
    :initform 0)
   (target_pick_position_x
    :reader target_pick_position_x
    :initarg :target_pick_position_x
    :type cl:float
    :initform 0.0)
   (target_pick_position_y
    :reader target_pick_position_y
    :initarg :target_pick_position_y
    :type cl:float
    :initform 0.0)
   (target_pick_position_z
    :reader target_pick_position_z
    :initarg :target_pick_position_z
    :type cl:float
    :initform 0.0)
   (target_pick_orientation_x
    :reader target_pick_orientation_x
    :initarg :target_pick_orientation_x
    :type cl:float
    :initform 0.0)
   (target_pick_orientation_y
    :reader target_pick_orientation_y
    :initarg :target_pick_orientation_y
    :type cl:float
    :initform 0.0)
   (target_pick_orientation_z
    :reader target_pick_orientation_z
    :initarg :target_pick_orientation_z
    :type cl:float
    :initform 0.0)
   (target_pick_orientation_w
    :reader target_pick_orientation_w
    :initarg :target_pick_orientation_w
    :type cl:float
    :initform 0.0)
   (target_place_position_x
    :reader target_place_position_x
    :initarg :target_place_position_x
    :type cl:float
    :initform 0.0)
   (target_place_position_y
    :reader target_place_position_y
    :initarg :target_place_position_y
    :type cl:float
    :initform 0.0)
   (target_place_position_z
    :reader target_place_position_z
    :initarg :target_place_position_z
    :type cl:float
    :initform 0.0)
   (target_place_orientation_x
    :reader target_place_orientation_x
    :initarg :target_place_orientation_x
    :type cl:float
    :initform 0.0)
   (target_place_orientation_y
    :reader target_place_orientation_y
    :initarg :target_place_orientation_y
    :type cl:float
    :initform 0.0)
   (target_place_orientation_z
    :reader target_place_orientation_z
    :initarg :target_place_orientation_z
    :type cl:float
    :initform 0.0)
   (target_place_orientation_w
    :reader target_place_orientation_w
    :initarg :target_place_orientation_w
    :type cl:float
    :initform 0.0)
   (text
    :reader text
    :initarg :text
    :type cl:string
    :initform ""))
)

(cl:defclass db-response (<db-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <db-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'db-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_custom_msgs-srv:<db-response> is deprecated: use robot_custom_msgs-srv:db-response instead.")))

(cl:ensure-generic-function 'tableid-val :lambda-list '(m))
(cl:defmethod tableid-val ((m <db-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:tableid-val is deprecated.  Use robot_custom_msgs-srv:tableid instead.")
  (tableid m))

(cl:ensure-generic-function 'target_pick_position_x-val :lambda-list '(m))
(cl:defmethod target_pick_position_x-val ((m <db-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_pick_position_x-val is deprecated.  Use robot_custom_msgs-srv:target_pick_position_x instead.")
  (target_pick_position_x m))

(cl:ensure-generic-function 'target_pick_position_y-val :lambda-list '(m))
(cl:defmethod target_pick_position_y-val ((m <db-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_pick_position_y-val is deprecated.  Use robot_custom_msgs-srv:target_pick_position_y instead.")
  (target_pick_position_y m))

(cl:ensure-generic-function 'target_pick_position_z-val :lambda-list '(m))
(cl:defmethod target_pick_position_z-val ((m <db-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_pick_position_z-val is deprecated.  Use robot_custom_msgs-srv:target_pick_position_z instead.")
  (target_pick_position_z m))

(cl:ensure-generic-function 'target_pick_orientation_x-val :lambda-list '(m))
(cl:defmethod target_pick_orientation_x-val ((m <db-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_pick_orientation_x-val is deprecated.  Use robot_custom_msgs-srv:target_pick_orientation_x instead.")
  (target_pick_orientation_x m))

(cl:ensure-generic-function 'target_pick_orientation_y-val :lambda-list '(m))
(cl:defmethod target_pick_orientation_y-val ((m <db-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_pick_orientation_y-val is deprecated.  Use robot_custom_msgs-srv:target_pick_orientation_y instead.")
  (target_pick_orientation_y m))

(cl:ensure-generic-function 'target_pick_orientation_z-val :lambda-list '(m))
(cl:defmethod target_pick_orientation_z-val ((m <db-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_pick_orientation_z-val is deprecated.  Use robot_custom_msgs-srv:target_pick_orientation_z instead.")
  (target_pick_orientation_z m))

(cl:ensure-generic-function 'target_pick_orientation_w-val :lambda-list '(m))
(cl:defmethod target_pick_orientation_w-val ((m <db-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_pick_orientation_w-val is deprecated.  Use robot_custom_msgs-srv:target_pick_orientation_w instead.")
  (target_pick_orientation_w m))

(cl:ensure-generic-function 'target_place_position_x-val :lambda-list '(m))
(cl:defmethod target_place_position_x-val ((m <db-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_place_position_x-val is deprecated.  Use robot_custom_msgs-srv:target_place_position_x instead.")
  (target_place_position_x m))

(cl:ensure-generic-function 'target_place_position_y-val :lambda-list '(m))
(cl:defmethod target_place_position_y-val ((m <db-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_place_position_y-val is deprecated.  Use robot_custom_msgs-srv:target_place_position_y instead.")
  (target_place_position_y m))

(cl:ensure-generic-function 'target_place_position_z-val :lambda-list '(m))
(cl:defmethod target_place_position_z-val ((m <db-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_place_position_z-val is deprecated.  Use robot_custom_msgs-srv:target_place_position_z instead.")
  (target_place_position_z m))

(cl:ensure-generic-function 'target_place_orientation_x-val :lambda-list '(m))
(cl:defmethod target_place_orientation_x-val ((m <db-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_place_orientation_x-val is deprecated.  Use robot_custom_msgs-srv:target_place_orientation_x instead.")
  (target_place_orientation_x m))

(cl:ensure-generic-function 'target_place_orientation_y-val :lambda-list '(m))
(cl:defmethod target_place_orientation_y-val ((m <db-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_place_orientation_y-val is deprecated.  Use robot_custom_msgs-srv:target_place_orientation_y instead.")
  (target_place_orientation_y m))

(cl:ensure-generic-function 'target_place_orientation_z-val :lambda-list '(m))
(cl:defmethod target_place_orientation_z-val ((m <db-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_place_orientation_z-val is deprecated.  Use robot_custom_msgs-srv:target_place_orientation_z instead.")
  (target_place_orientation_z m))

(cl:ensure-generic-function 'target_place_orientation_w-val :lambda-list '(m))
(cl:defmethod target_place_orientation_w-val ((m <db-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_place_orientation_w-val is deprecated.  Use robot_custom_msgs-srv:target_place_orientation_w instead.")
  (target_place_orientation_w m))

(cl:ensure-generic-function 'text-val :lambda-list '(m))
(cl:defmethod text-val ((m <db-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:text-val is deprecated.  Use robot_custom_msgs-srv:text instead.")
  (text m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <db-response>) ostream)
  "Serializes a message object of type '<db-response>"
  (cl:let* ((signed (cl:slot-value msg 'tableid)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'target_pick_position_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'target_pick_position_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'target_pick_position_z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'target_pick_orientation_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'target_pick_orientation_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'target_pick_orientation_z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'target_pick_orientation_w))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'target_place_position_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'target_place_position_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'target_place_position_z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'target_place_orientation_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'target_place_orientation_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'target_place_orientation_z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'target_place_orientation_w))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'text))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'text))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <db-response>) istream)
  "Deserializes a message object of type '<db-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'tableid) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'target_pick_position_x) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'target_pick_position_y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'target_pick_position_z) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'target_pick_orientation_x) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'target_pick_orientation_y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'target_pick_orientation_z) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'target_pick_orientation_w) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'target_place_position_x) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'target_place_position_y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'target_place_position_z) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'target_place_orientation_x) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'target_place_orientation_y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'target_place_orientation_z) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'target_place_orientation_w) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'text) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'text) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<db-response>)))
  "Returns string type for a service object of type '<db-response>"
  "robot_custom_msgs/dbResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'db-response)))
  "Returns string type for a service object of type 'db-response"
  "robot_custom_msgs/dbResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<db-response>)))
  "Returns md5sum for a message object of type '<db-response>"
  "0b56db4429947d5d82235b9718d8f033")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'db-response)))
  "Returns md5sum for a message object of type 'db-response"
  "0b56db4429947d5d82235b9718d8f033")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<db-response>)))
  "Returns full string definition for message of type '<db-response>"
  (cl:format cl:nil "#output~%int64 tableid~%~%float64 target_pick_position_x~%float64 target_pick_position_y~%float64 target_pick_position_z~%~%float64 target_pick_orientation_x~%float64 target_pick_orientation_y~%float64 target_pick_orientation_z~%float64 target_pick_orientation_w~%~%float64 target_place_position_x~%float64 target_place_position_y~%float64 target_place_position_z~%~%float64 target_place_orientation_x~%float64 target_place_orientation_y~%float64 target_place_orientation_z~%float64 target_place_orientation_w~%~%string text~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'db-response)))
  "Returns full string definition for message of type 'db-response"
  (cl:format cl:nil "#output~%int64 tableid~%~%float64 target_pick_position_x~%float64 target_pick_position_y~%float64 target_pick_position_z~%~%float64 target_pick_orientation_x~%float64 target_pick_orientation_y~%float64 target_pick_orientation_z~%float64 target_pick_orientation_w~%~%float64 target_place_position_x~%float64 target_place_position_y~%float64 target_place_position_z~%~%float64 target_place_orientation_x~%float64 target_place_orientation_y~%float64 target_place_orientation_z~%float64 target_place_orientation_w~%~%string text~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <db-response>))
  (cl:+ 0
     8
     8
     8
     8
     8
     8
     8
     8
     8
     8
     8
     8
     8
     8
     8
     4 (cl:length (cl:slot-value msg 'text))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <db-response>))
  "Converts a ROS message object to a list"
  (cl:list 'db-response
    (cl:cons ':tableid (tableid msg))
    (cl:cons ':target_pick_position_x (target_pick_position_x msg))
    (cl:cons ':target_pick_position_y (target_pick_position_y msg))
    (cl:cons ':target_pick_position_z (target_pick_position_z msg))
    (cl:cons ':target_pick_orientation_x (target_pick_orientation_x msg))
    (cl:cons ':target_pick_orientation_y (target_pick_orientation_y msg))
    (cl:cons ':target_pick_orientation_z (target_pick_orientation_z msg))
    (cl:cons ':target_pick_orientation_w (target_pick_orientation_w msg))
    (cl:cons ':target_place_position_x (target_place_position_x msg))
    (cl:cons ':target_place_position_y (target_place_position_y msg))
    (cl:cons ':target_place_position_z (target_place_position_z msg))
    (cl:cons ':target_place_orientation_x (target_place_orientation_x msg))
    (cl:cons ':target_place_orientation_y (target_place_orientation_y msg))
    (cl:cons ':target_place_orientation_z (target_place_orientation_z msg))
    (cl:cons ':target_place_orientation_w (target_place_orientation_w msg))
    (cl:cons ':text (text msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'db)))
  'db-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'db)))
  'db-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'db)))
  "Returns string type for a service object of type '<db>"
  "robot_custom_msgs/db")