
(cl:in-package :asdf)

(defsystem "robot_custom_msgs-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "db" :depends-on ("_package_db"))
    (:file "_package_db" :depends-on ("_package"))
  ))