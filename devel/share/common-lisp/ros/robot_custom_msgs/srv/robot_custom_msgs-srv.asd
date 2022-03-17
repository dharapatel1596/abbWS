
(cl:in-package :asdf)

(defsystem "robot_custom_msgs-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "OrderData" :depends-on ("_package_OrderData"))
    (:file "_package_OrderData" :depends-on ("_package"))
  ))