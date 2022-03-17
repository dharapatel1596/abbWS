;; Auto-generated. Do not edit!


(when (boundp 'robot_custom_msgs::OrderData)
  (if (not (find-package "ROBOT_CUSTOM_MSGS"))
    (make-package "ROBOT_CUSTOM_MSGS"))
  (shadow 'OrderData (find-package "ROBOT_CUSTOM_MSGS")))
(unless (find-package "ROBOT_CUSTOM_MSGS::ORDERDATA")
  (make-package "ROBOT_CUSTOM_MSGS::ORDERDATA"))
(unless (find-package "ROBOT_CUSTOM_MSGS::ORDERDATAREQUEST")
  (make-package "ROBOT_CUSTOM_MSGS::ORDERDATAREQUEST"))
(unless (find-package "ROBOT_CUSTOM_MSGS::ORDERDATARESPONSE")
  (make-package "ROBOT_CUSTOM_MSGS::ORDERDATARESPONSE"))

(in-package "ROS")





(defclass robot_custom_msgs::OrderDataRequest
  :super ros::object
  :slots (_start ))

(defmethod robot_custom_msgs::OrderDataRequest
  (:init
   (&key
    ((:start __start) "")
    )
   (send-super :init)
   (setq _start (string __start))
   self)
  (:start
   (&optional __start)
   (if __start (setq _start __start)) _start)
  (:serialization-length
   ()
   (+
    ;; string _start
    4 (length _start)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _start
       (write-long (length _start) s) (princ _start s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _start
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _start (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass robot_custom_msgs::OrderDataResponse
  :super ros::object
  :slots (_raw_id _table_id _order_time _target_pick_position_x _target_pick_position_y _target_pick_position_z _target_pick_orientation_x _target_pick_orientation_y _target_pick_orientation_z _target_pick_orientation_w _target_place_position_x _target_place_position_y _target_place_position_z _target_place_orientation_x _target_place_orientation_y _target_place_orientation_z _target_place_orientation_w _validation_text ))

(defmethod robot_custom_msgs::OrderDataResponse
  (:init
   (&key
    ((:raw_id __raw_id) 0)
    ((:table_id __table_id) 0)
    ((:order_time __order_time) "")
    ((:target_pick_position_x __target_pick_position_x) 0.0)
    ((:target_pick_position_y __target_pick_position_y) 0.0)
    ((:target_pick_position_z __target_pick_position_z) 0.0)
    ((:target_pick_orientation_x __target_pick_orientation_x) 0.0)
    ((:target_pick_orientation_y __target_pick_orientation_y) 0.0)
    ((:target_pick_orientation_z __target_pick_orientation_z) 0.0)
    ((:target_pick_orientation_w __target_pick_orientation_w) 0.0)
    ((:target_place_position_x __target_place_position_x) 0.0)
    ((:target_place_position_y __target_place_position_y) 0.0)
    ((:target_place_position_z __target_place_position_z) 0.0)
    ((:target_place_orientation_x __target_place_orientation_x) 0.0)
    ((:target_place_orientation_y __target_place_orientation_y) 0.0)
    ((:target_place_orientation_z __target_place_orientation_z) 0.0)
    ((:target_place_orientation_w __target_place_orientation_w) 0.0)
    ((:validation_text __validation_text) "")
    )
   (send-super :init)
   (setq _raw_id (round __raw_id))
   (setq _table_id (round __table_id))
   (setq _order_time (string __order_time))
   (setq _target_pick_position_x (float __target_pick_position_x))
   (setq _target_pick_position_y (float __target_pick_position_y))
   (setq _target_pick_position_z (float __target_pick_position_z))
   (setq _target_pick_orientation_x (float __target_pick_orientation_x))
   (setq _target_pick_orientation_y (float __target_pick_orientation_y))
   (setq _target_pick_orientation_z (float __target_pick_orientation_z))
   (setq _target_pick_orientation_w (float __target_pick_orientation_w))
   (setq _target_place_position_x (float __target_place_position_x))
   (setq _target_place_position_y (float __target_place_position_y))
   (setq _target_place_position_z (float __target_place_position_z))
   (setq _target_place_orientation_x (float __target_place_orientation_x))
   (setq _target_place_orientation_y (float __target_place_orientation_y))
   (setq _target_place_orientation_z (float __target_place_orientation_z))
   (setq _target_place_orientation_w (float __target_place_orientation_w))
   (setq _validation_text (string __validation_text))
   self)
  (:raw_id
   (&optional __raw_id)
   (if __raw_id (setq _raw_id __raw_id)) _raw_id)
  (:table_id
   (&optional __table_id)
   (if __table_id (setq _table_id __table_id)) _table_id)
  (:order_time
   (&optional __order_time)
   (if __order_time (setq _order_time __order_time)) _order_time)
  (:target_pick_position_x
   (&optional __target_pick_position_x)
   (if __target_pick_position_x (setq _target_pick_position_x __target_pick_position_x)) _target_pick_position_x)
  (:target_pick_position_y
   (&optional __target_pick_position_y)
   (if __target_pick_position_y (setq _target_pick_position_y __target_pick_position_y)) _target_pick_position_y)
  (:target_pick_position_z
   (&optional __target_pick_position_z)
   (if __target_pick_position_z (setq _target_pick_position_z __target_pick_position_z)) _target_pick_position_z)
  (:target_pick_orientation_x
   (&optional __target_pick_orientation_x)
   (if __target_pick_orientation_x (setq _target_pick_orientation_x __target_pick_orientation_x)) _target_pick_orientation_x)
  (:target_pick_orientation_y
   (&optional __target_pick_orientation_y)
   (if __target_pick_orientation_y (setq _target_pick_orientation_y __target_pick_orientation_y)) _target_pick_orientation_y)
  (:target_pick_orientation_z
   (&optional __target_pick_orientation_z)
   (if __target_pick_orientation_z (setq _target_pick_orientation_z __target_pick_orientation_z)) _target_pick_orientation_z)
  (:target_pick_orientation_w
   (&optional __target_pick_orientation_w)
   (if __target_pick_orientation_w (setq _target_pick_orientation_w __target_pick_orientation_w)) _target_pick_orientation_w)
  (:target_place_position_x
   (&optional __target_place_position_x)
   (if __target_place_position_x (setq _target_place_position_x __target_place_position_x)) _target_place_position_x)
  (:target_place_position_y
   (&optional __target_place_position_y)
   (if __target_place_position_y (setq _target_place_position_y __target_place_position_y)) _target_place_position_y)
  (:target_place_position_z
   (&optional __target_place_position_z)
   (if __target_place_position_z (setq _target_place_position_z __target_place_position_z)) _target_place_position_z)
  (:target_place_orientation_x
   (&optional __target_place_orientation_x)
   (if __target_place_orientation_x (setq _target_place_orientation_x __target_place_orientation_x)) _target_place_orientation_x)
  (:target_place_orientation_y
   (&optional __target_place_orientation_y)
   (if __target_place_orientation_y (setq _target_place_orientation_y __target_place_orientation_y)) _target_place_orientation_y)
  (:target_place_orientation_z
   (&optional __target_place_orientation_z)
   (if __target_place_orientation_z (setq _target_place_orientation_z __target_place_orientation_z)) _target_place_orientation_z)
  (:target_place_orientation_w
   (&optional __target_place_orientation_w)
   (if __target_place_orientation_w (setq _target_place_orientation_w __target_place_orientation_w)) _target_place_orientation_w)
  (:validation_text
   (&optional __validation_text)
   (if __validation_text (setq _validation_text __validation_text)) _validation_text)
  (:serialization-length
   ()
   (+
    ;; int64 _raw_id
    8
    ;; int64 _table_id
    8
    ;; string _order_time
    4 (length _order_time)
    ;; float64 _target_pick_position_x
    8
    ;; float64 _target_pick_position_y
    8
    ;; float64 _target_pick_position_z
    8
    ;; float64 _target_pick_orientation_x
    8
    ;; float64 _target_pick_orientation_y
    8
    ;; float64 _target_pick_orientation_z
    8
    ;; float64 _target_pick_orientation_w
    8
    ;; float64 _target_place_position_x
    8
    ;; float64 _target_place_position_y
    8
    ;; float64 _target_place_position_z
    8
    ;; float64 _target_place_orientation_x
    8
    ;; float64 _target_place_orientation_y
    8
    ;; float64 _target_place_orientation_z
    8
    ;; float64 _target_place_orientation_w
    8
    ;; string _validation_text
    4 (length _validation_text)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _raw_id
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _raw_id (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _raw_id) (= (length (_raw_id . bv)) 2)) ;; bignum
              (write-long (ash (elt (_raw_id . bv) 0) 0) s)
              (write-long (ash (elt (_raw_id . bv) 1) -1) s))
             ((and (class _raw_id) (= (length (_raw_id . bv)) 1)) ;; big1
              (write-long (elt (_raw_id . bv) 0) s)
              (write-long (if (>= _raw_id 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _raw_id s)(write-long (if (>= _raw_id 0) 0 #xffffffff) s)))
     ;; int64 _table_id
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _table_id (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _table_id) (= (length (_table_id . bv)) 2)) ;; bignum
              (write-long (ash (elt (_table_id . bv) 0) 0) s)
              (write-long (ash (elt (_table_id . bv) 1) -1) s))
             ((and (class _table_id) (= (length (_table_id . bv)) 1)) ;; big1
              (write-long (elt (_table_id . bv) 0) s)
              (write-long (if (>= _table_id 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _table_id s)(write-long (if (>= _table_id 0) 0 #xffffffff) s)))
     ;; string _order_time
       (write-long (length _order_time) s) (princ _order_time s)
     ;; float64 _target_pick_position_x
       (sys::poke _target_pick_position_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _target_pick_position_y
       (sys::poke _target_pick_position_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _target_pick_position_z
       (sys::poke _target_pick_position_z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _target_pick_orientation_x
       (sys::poke _target_pick_orientation_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _target_pick_orientation_y
       (sys::poke _target_pick_orientation_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _target_pick_orientation_z
       (sys::poke _target_pick_orientation_z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _target_pick_orientation_w
       (sys::poke _target_pick_orientation_w (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _target_place_position_x
       (sys::poke _target_place_position_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _target_place_position_y
       (sys::poke _target_place_position_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _target_place_position_z
       (sys::poke _target_place_position_z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _target_place_orientation_x
       (sys::poke _target_place_orientation_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _target_place_orientation_y
       (sys::poke _target_place_orientation_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _target_place_orientation_z
       (sys::poke _target_place_orientation_z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _target_place_orientation_w
       (sys::poke _target_place_orientation_w (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; string _validation_text
       (write-long (length _validation_text) s) (princ _validation_text s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _raw_id
#+(or :alpha :irix6 :x86_64)
      (setf _raw_id (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _raw_id (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _table_id
#+(or :alpha :irix6 :x86_64)
      (setf _table_id (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _table_id (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; string _order_time
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _order_time (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64 _target_pick_position_x
     (setq _target_pick_position_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _target_pick_position_y
     (setq _target_pick_position_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _target_pick_position_z
     (setq _target_pick_position_z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _target_pick_orientation_x
     (setq _target_pick_orientation_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _target_pick_orientation_y
     (setq _target_pick_orientation_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _target_pick_orientation_z
     (setq _target_pick_orientation_z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _target_pick_orientation_w
     (setq _target_pick_orientation_w (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _target_place_position_x
     (setq _target_place_position_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _target_place_position_y
     (setq _target_place_position_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _target_place_position_z
     (setq _target_place_position_z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _target_place_orientation_x
     (setq _target_place_orientation_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _target_place_orientation_y
     (setq _target_place_orientation_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _target_place_orientation_z
     (setq _target_place_orientation_z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _target_place_orientation_w
     (setq _target_place_orientation_w (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; string _validation_text
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _validation_text (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass robot_custom_msgs::OrderData
  :super ros::object
  :slots ())

(setf (get robot_custom_msgs::OrderData :md5sum-) "9c311561e0acab097731704c85ada1aa")
(setf (get robot_custom_msgs::OrderData :datatype-) "robot_custom_msgs/OrderData")
(setf (get robot_custom_msgs::OrderData :request) robot_custom_msgs::OrderDataRequest)
(setf (get robot_custom_msgs::OrderData :response) robot_custom_msgs::OrderDataResponse)

(defmethod robot_custom_msgs::OrderDataRequest
  (:response () (instance robot_custom_msgs::OrderDataResponse :init)))

(setf (get robot_custom_msgs::OrderDataRequest :md5sum-) "9c311561e0acab097731704c85ada1aa")
(setf (get robot_custom_msgs::OrderDataRequest :datatype-) "robot_custom_msgs/OrderDataRequest")
(setf (get robot_custom_msgs::OrderDataRequest :definition-)
      "#inputs
string start

---
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



")

(setf (get robot_custom_msgs::OrderDataResponse :md5sum-) "9c311561e0acab097731704c85ada1aa")
(setf (get robot_custom_msgs::OrderDataResponse :datatype-) "robot_custom_msgs/OrderDataResponse")
(setf (get robot_custom_msgs::OrderDataResponse :definition-)
      "#inputs
string start

---
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



")



(provide :robot_custom_msgs/OrderData "9c311561e0acab097731704c85ada1aa")


