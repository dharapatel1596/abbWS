// Generated by gencpp from file robot_custom_msgs/OrderData.msg
// DO NOT EDIT!


#ifndef ROBOT_CUSTOM_MSGS_MESSAGE_ORDERDATA_H
#define ROBOT_CUSTOM_MSGS_MESSAGE_ORDERDATA_H

#include <ros/service_traits.h>


#include <robot_custom_msgs/OrderDataRequest.h>
#include <robot_custom_msgs/OrderDataResponse.h>


namespace robot_custom_msgs
{

struct OrderData
{

typedef OrderDataRequest Request;
typedef OrderDataResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct OrderData
} // namespace robot_custom_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::robot_custom_msgs::OrderData > {
  static const char* value()
  {
    return "9c311561e0acab097731704c85ada1aa";
  }

  static const char* value(const ::robot_custom_msgs::OrderData&) { return value(); }
};

template<>
struct DataType< ::robot_custom_msgs::OrderData > {
  static const char* value()
  {
    return "robot_custom_msgs/OrderData";
  }

  static const char* value(const ::robot_custom_msgs::OrderData&) { return value(); }
};


// service_traits::MD5Sum< ::robot_custom_msgs::OrderDataRequest> should match
// service_traits::MD5Sum< ::robot_custom_msgs::OrderData >
template<>
struct MD5Sum< ::robot_custom_msgs::OrderDataRequest>
{
  static const char* value()
  {
    return MD5Sum< ::robot_custom_msgs::OrderData >::value();
  }
  static const char* value(const ::robot_custom_msgs::OrderDataRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::robot_custom_msgs::OrderDataRequest> should match
// service_traits::DataType< ::robot_custom_msgs::OrderData >
template<>
struct DataType< ::robot_custom_msgs::OrderDataRequest>
{
  static const char* value()
  {
    return DataType< ::robot_custom_msgs::OrderData >::value();
  }
  static const char* value(const ::robot_custom_msgs::OrderDataRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::robot_custom_msgs::OrderDataResponse> should match
// service_traits::MD5Sum< ::robot_custom_msgs::OrderData >
template<>
struct MD5Sum< ::robot_custom_msgs::OrderDataResponse>
{
  static const char* value()
  {
    return MD5Sum< ::robot_custom_msgs::OrderData >::value();
  }
  static const char* value(const ::robot_custom_msgs::OrderDataResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::robot_custom_msgs::OrderDataResponse> should match
// service_traits::DataType< ::robot_custom_msgs::OrderData >
template<>
struct DataType< ::robot_custom_msgs::OrderDataResponse>
{
  static const char* value()
  {
    return DataType< ::robot_custom_msgs::OrderData >::value();
  }
  static const char* value(const ::robot_custom_msgs::OrderDataResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // ROBOT_CUSTOM_MSGS_MESSAGE_ORDERDATA_H
