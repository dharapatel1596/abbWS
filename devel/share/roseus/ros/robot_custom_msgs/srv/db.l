;; Auto-generated. Do not edit!


(when (boundp 'robot_custom_msgs::db)
  (if (not (find-package "ROBOT_CUSTOM_MSGS"))
    (make-package "ROBOT_CUSTOM_MSGS"))
  (shadow 'db (find-package "ROBOT_CUSTOM_MSGS")))
(unless (find-package "ROBOT_CUSTOM_MSGS::DB")
  (make-package "ROBOT_CUSTOM_MSGS::DB"))
(unless (find-package "ROBOT_CUSTOM_MSGS::DBREQUEST")
  (make-package "ROBOT_CUSTOM_MSGS::DBREQUEST"))
(unless (find-package "ROBOT_CUSTOM_MSGS::DBRESPONSE")
  (make-package "ROBOT_CUSTOM_MSGS::DBRESPONSE"))

(in-package "ROS")





(defclass robot_custom_msgs::dbRequest
  :super ros::object
  :slots (_id ))

(defmethod robot_custom_msgs::dbRequest
  (:init
   (&key
    ((:id __id) 0)
    )
   (send-super :init)
   (setq _id (round __id))
   self)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:serialization-length
   ()
   (+
    ;; int64 _id
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _id
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _id (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _id) (= (length (_id . bv)) 2)) ;; bignum
              (write-long (ash (elt (_id . bv) 0) 0) s)
              (write-long (ash (elt (_id . bv) 1) -1) s))
             ((and (class _id) (= (length (_id . bv)) 1)) ;; big1
              (write-long (elt (_id . bv) 0) s)
              (write-long (if (>= _id 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _id s)(write-long (if (>= _id 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _id
#+(or :alpha :irix6 :x86_64)
      (setf _id (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _id (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass robot_custom_msgs::dbResponse
  :super ros::object
  :slots (_tableid _target_pick_position_x _target_pick_position_y _target_pick_position_z _target_pick_orientation_x _target_pick_orientation_y _target_pick_orientation_z _target_pick_orientation_w _target_place_position_x _target_place_position_y _target_place_position_z _target_place_orientation_x _target_place_orientation_y _target_place_orientation_z _target_place_orientation_w _text ))

(defmethod robot_custom_msgs::dbResponse
  (:init
   (&key
    ((:tableid __tableid) 0)
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
    ((:text __text) "")
    )
   (send-super :init)
   (setq _tableid (round __tableid))
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
   (setq _text (string __text))
   self)
  (:tableid
   (&optional __tableid)
   (if __tableid (setq _tableid __tableid)) _tableid)
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
  (:text
   (&optional __text)
   (if __text (setq _text __text)) _text)
  (:serialization-length
   ()
   (+
    ;; int64 _tableid
    8
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
    ;; string _text
    4 (length _text)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _tableid
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _tableid (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _tableid) (= (length (_tableid . bv)) 2)) ;; bignum
              (write-long (ash (elt (_tableid . bv) 0) 0) s)
              (write-long (ash (elt (_tableid . bv) 1) -1) s))
             ((and (class _tableid) (= (length (_tableid . bv)) 1)) ;; big1
              (write-long (elt (_tableid . bv) 0) s)
              (write-long (if (>= _tableid 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _tableid s)(write-long (if (>= _tableid 0) 0 #xffffffff) s)))
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
     ;; string _text
       (write-long (length _text) s) (princ _text s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _tableid
#+(or :alpha :irix6 :x86_64)
      (setf _tableid (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _tableid (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
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
   ;; string _text
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _text (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass robot_custom_msgs::db
  :super ros::object
  :slots ())

(setf (get robot_custom_msgs::db :md5sum-) "0b56db4429947d5d82235b9718d8f033")
(setf (get robot_custom_msgs::db :datatype-) "robot_custom_msgs/db")
(setf (get robot_custom_msgs::db :request) robot_custom_msgs::dbRequest)
(setf (get robot_custom_msgs::db :response) robot_custom_msgs::dbResponse)

(defmethod robot_custom_msgs::dbRequest
  (:response () (instance robot_custom_msgs::dbResponse :init)))

(setf (get robot_custom_msgs::dbRequest :md5sum-) "0b56db4429947d5d82235b9718d8f033")
(setf (get robot_custom_msgs::dbRequest :datatype-) "robot_custom_msgs/dbRequest")
(setf (get robot_custom_msgs::dbRequest :definition-)
      "#inputs
int64 id

---
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



")

(setf (get robot_custom_msgs::dbResponse :md5sum-) "0b56db4429947d5d82235b9718d8f033")
(setf (get robot_custom_msgs::dbResponse :datatype-) "robot_custom_msgs/dbResponse")
(setf (get robot_custom_msgs::dbResponse :definition-)
      "#inputs
int64 id

---
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



")



(provide :robot_custom_msgs/db "0b56db4429947d5d82235b9718d8f033")


