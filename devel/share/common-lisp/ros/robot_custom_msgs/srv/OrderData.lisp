; Auto-generated. Do not edit!


(cl:in-package robot_custom_msgs-srv)


;//! \htmlinclude OrderData-request.msg.html

(cl:defclass <OrderData-request> (roslisp-msg-protocol:ros-message)
  ((start
    :reader start
    :initarg :start
    :type cl:string
    :initform ""))
)

(cl:defclass OrderData-request (<OrderData-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <OrderData-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'OrderData-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_custom_msgs-srv:<OrderData-request> is deprecated: use robot_custom_msgs-srv:OrderData-request instead.")))

(cl:ensure-generic-function 'start-val :lambda-list '(m))
(cl:defmethod start-val ((m <OrderData-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:start-val is deprecated.  Use robot_custom_msgs-srv:start instead.")
  (start m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <OrderData-request>) ostream)
  "Serializes a message object of type '<OrderData-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'start))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'start))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <OrderData-request>) istream)
  "Deserializes a message object of type '<OrderData-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'start) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'start) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<OrderData-request>)))
  "Returns string type for a service object of type '<OrderData-request>"
  "robot_custom_msgs/OrderDataRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'OrderData-request)))
  "Returns string type for a service object of type 'OrderData-request"
  "robot_custom_msgs/OrderDataRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<OrderData-request>)))
  "Returns md5sum for a message object of type '<OrderData-request>"
  "9c311561e0acab097731704c85ada1aa")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'OrderData-request)))
  "Returns md5sum for a message object of type 'OrderData-request"
  "9c311561e0acab097731704c85ada1aa")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<OrderData-request>)))
  "Returns full string definition for message of type '<OrderData-request>"
  (cl:format cl:nil "#inputs~%string start~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'OrderData-request)))
  "Returns full string definition for message of type 'OrderData-request"
  (cl:format cl:nil "#inputs~%string start~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <OrderData-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'start))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <OrderData-request>))
  "Converts a ROS message object to a list"
  (cl:list 'OrderData-request
    (cl:cons ':start (start msg))
))
;//! \htmlinclude OrderData-response.msg.html

(cl:defclass <OrderData-response> (roslisp-msg-protocol:ros-message)
  ((raw_id
    :reader raw_id
    :initarg :raw_id
    :type cl:integer
    :initform 0)
   (table_id
    :reader table_id
    :initarg :table_id
    :type cl:integer
    :initform 0)
   (order_time
    :reader order_time
    :initarg :order_time
    :type cl:string
    :initform "")
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
   (validation_text
    :reader validation_text
    :initarg :validation_text
    :type cl:string
    :initform ""))
)

(cl:defclass OrderData-response (<OrderData-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <OrderData-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'OrderData-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_custom_msgs-srv:<OrderData-response> is deprecated: use robot_custom_msgs-srv:OrderData-response instead.")))

(cl:ensure-generic-function 'raw_id-val :lambda-list '(m))
(cl:defmethod raw_id-val ((m <OrderData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:raw_id-val is deprecated.  Use robot_custom_msgs-srv:raw_id instead.")
  (raw_id m))

(cl:ensure-generic-function 'table_id-val :lambda-list '(m))
(cl:defmethod table_id-val ((m <OrderData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:table_id-val is deprecated.  Use robot_custom_msgs-srv:table_id instead.")
  (table_id m))

(cl:ensure-generic-function 'order_time-val :lambda-list '(m))
(cl:defmethod order_time-val ((m <OrderData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:order_time-val is deprecated.  Use robot_custom_msgs-srv:order_time instead.")
  (order_time m))

(cl:ensure-generic-function 'target_pick_position_x-val :lambda-list '(m))
(cl:defmethod target_pick_position_x-val ((m <OrderData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_pick_position_x-val is deprecated.  Use robot_custom_msgs-srv:target_pick_position_x instead.")
  (target_pick_position_x m))

(cl:ensure-generic-function 'target_pick_position_y-val :lambda-list '(m))
(cl:defmethod target_pick_position_y-val ((m <OrderData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_pick_position_y-val is deprecated.  Use robot_custom_msgs-srv:target_pick_position_y instead.")
  (target_pick_position_y m))

(cl:ensure-generic-function 'target_pick_position_z-val :lambda-list '(m))
(cl:defmethod target_pick_position_z-val ((m <OrderData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_pick_position_z-val is deprecated.  Use robot_custom_msgs-srv:target_pick_position_z instead.")
  (target_pick_position_z m))

(cl:ensure-generic-function 'target_pick_orientation_x-val :lambda-list '(m))
(cl:defmethod target_pick_orientation_x-val ((m <OrderData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_pick_orientation_x-val is deprecated.  Use robot_custom_msgs-srv:target_pick_orientation_x instead.")
  (target_pick_orientation_x m))

(cl:ensure-generic-function 'target_pick_orientation_y-val :lambda-list '(m))
(cl:defmethod target_pick_orientation_y-val ((m <OrderData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_pick_orientation_y-val is deprecated.  Use robot_custom_msgs-srv:target_pick_orientation_y instead.")
  (target_pick_orientation_y m))

(cl:ensure-generic-function 'target_pick_orientation_z-val :lambda-list '(m))
(cl:defmethod target_pick_orientation_z-val ((m <OrderData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_pick_orientation_z-val is deprecated.  Use robot_custom_msgs-srv:target_pick_orientation_z instead.")
  (target_pick_orientation_z m))

(cl:ensure-generic-function 'target_pick_orientation_w-val :lambda-list '(m))
(cl:defmethod target_pick_orientation_w-val ((m <OrderData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_pick_orientation_w-val is deprecated.  Use robot_custom_msgs-srv:target_pick_orientation_w instead.")
  (target_pick_orientation_w m))

(cl:ensure-generic-function 'target_place_position_x-val :lambda-list '(m))
(cl:defmethod target_place_position_x-val ((m <OrderData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_place_position_x-val is deprecated.  Use robot_custom_msgs-srv:target_place_position_x instead.")
  (target_place_position_x m))

(cl:ensure-generic-function 'target_place_position_y-val :lambda-list '(m))
(cl:defmethod target_place_position_y-val ((m <OrderData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_place_position_y-val is deprecated.  Use robot_custom_msgs-srv:target_place_position_y instead.")
  (target_place_position_y m))

(cl:ensure-generic-function 'target_place_position_z-val :lambda-list '(m))
(cl:defmethod target_place_position_z-val ((m <OrderData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_place_position_z-val is deprecated.  Use robot_custom_msgs-srv:target_place_position_z instead.")
  (target_place_position_z m))

(cl:ensure-generic-function 'target_place_orientation_x-val :lambda-list '(m))
(cl:defmethod target_place_orientation_x-val ((m <OrderData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_place_orientation_x-val is deprecated.  Use robot_custom_msgs-srv:target_place_orientation_x instead.")
  (target_place_orientation_x m))

(cl:ensure-generic-function 'target_place_orientation_y-val :lambda-list '(m))
(cl:defmethod target_place_orientation_y-val ((m <OrderData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_place_orientation_y-val is deprecated.  Use robot_custom_msgs-srv:target_place_orientation_y instead.")
  (target_place_orientation_y m))

(cl:ensure-generic-function 'target_place_orientation_z-val :lambda-list '(m))
(cl:defmethod target_place_orientation_z-val ((m <OrderData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_place_orientation_z-val is deprecated.  Use robot_custom_msgs-srv:target_place_orientation_z instead.")
  (target_place_orientation_z m))

(cl:ensure-generic-function 'target_place_orientation_w-val :lambda-list '(m))
(cl:defmethod target_place_orientation_w-val ((m <OrderData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:target_place_orientation_w-val is deprecated.  Use robot_custom_msgs-srv:target_place_orientation_w instead.")
  (target_place_orientation_w m))

(cl:ensure-generic-function 'validation_text-val :lambda-list '(m))
(cl:defmethod validation_text-val ((m <OrderData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_custom_msgs-srv:validation_text-val is deprecated.  Use robot_custom_msgs-srv:validation_text instead.")
  (validation_text m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <OrderData-response>) ostream)
  "Serializes a message object of type '<OrderData-response>"
  (cl:let* ((signed (cl:slot-value msg 'raw_id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'table_id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'order_time))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'order_time))
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
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'validation_text))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'validation_text))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <OrderData-response>) istream)
  "Deserializes a message object of type '<OrderData-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'raw_id) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'table_id) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'order_time) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'order_time) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
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
      (cl:setf (cl:slot-value msg 'validation_text) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'validation_text) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<OrderData-response>)))
  "Returns string type for a service object of type '<OrderData-response>"
  "robot_custom_msgs/OrderDataResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'OrderData-response)))
  "Returns string type for a service object of type 'OrderData-response"
  "robot_custom_msgs/OrderDataResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<OrderData-response>)))
  "Returns md5sum for a message object of type '<OrderData-response>"
  "9c311561e0acab097731704c85ada1aa")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'OrderData-response)))
  "Returns md5sum for a message object of type 'OrderData-response"
  "9c311561e0acab097731704c85ada1aa")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<OrderData-response>)))
  "Returns full string definition for message of type '<OrderData-response>"
  (cl:format cl:nil "#output~%int64 raw_id~%int64 table_id~%string order_time~%~%float64 target_pick_position_x~%float64 target_pick_position_y~%float64 target_pick_position_z~%~%float64 target_pick_orientation_x~%float64 target_pick_orientation_y~%float64 target_pick_orientation_z~%float64 target_pick_orientation_w~%~%float64 target_place_position_x~%float64 target_place_position_y~%float64 target_place_position_z~%~%float64 target_place_orientation_x~%float64 target_place_orientation_y~%float64 target_place_orientation_z~%float64 target_place_orientation_w~%~%string validation_text~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'OrderData-response)))
  "Returns full string definition for message of type 'OrderData-response"
  (cl:format cl:nil "#output~%int64 raw_id~%int64 table_id~%string order_time~%~%float64 target_pick_position_x~%float64 target_pick_position_y~%float64 target_pick_position_z~%~%float64 target_pick_orientation_x~%float64 target_pick_orientation_y~%float64 target_pick_orientation_z~%float64 target_pick_orientation_w~%~%float64 target_place_position_x~%float64 target_place_position_y~%float64 target_place_position_z~%~%float64 target_place_orientation_x~%float64 target_place_orientation_y~%float64 target_place_orientation_z~%float64 target_place_orientation_w~%~%string validation_text~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <OrderData-response>))
  (cl:+ 0
     8
     8
     4 (cl:length (cl:slot-value msg 'order_time))
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
     4 (cl:length (cl:slot-value msg 'validation_text))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <OrderData-response>))
  "Converts a ROS message object to a list"
  (cl:list 'OrderData-response
    (cl:cons ':raw_id (raw_id msg))
    (cl:cons ':table_id (table_id msg))
    (cl:cons ':order_time (order_time msg))
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
    (cl:cons ':validation_text (validation_text msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'OrderData)))
  'OrderData-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'OrderData)))
  'OrderData-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'OrderData)))
  "Returns string type for a service object of type '<OrderData>"
  "robot_custom_msgs/OrderData")