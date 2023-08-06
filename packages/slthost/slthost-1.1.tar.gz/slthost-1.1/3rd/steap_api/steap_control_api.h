#pragma once
#ifndef STEAP_CONTROL_API_H
#define STEAP_CONTROL_API_H

#include <stdint.h>
#include <mutex>

#ifdef STEAP_STATIC_LIB
#define DLL_API  extern
#else
#ifdef STEAPAPI_EXPORTS
#define DLL_API __declspec(dllexport)  
#else
#define DLL_API __declspec(dllimport)  
#endif
#endif

#define ENUM_TYPE_CASE(x)   case x: return(#x);

#define MAX_IP_LEN 16
#define RECV_TIMEOUT_STR "recv_timeout"

#ifndef STEAP_API_NAMESPACE
#define STEAP_API_NAMESPACE steap_api
#endif
#ifndef STEAP_API_NAMESPACE_BEGIN
#define STEAP_API_NAMESPACE_BEGIN namespace STEAP_API_NAMESPACE {
#endif
#ifndef STEAP_API_NAMESPACE_END
#define STEAP_API_NAMESPACE_END }
#endif

#define RES_OK 0
#define ERR_ALLOC -1
#define ERR_TIMEOUT -2
#define ERR_REQ_FAIL -3
using namespace std;


enum pcmsg_name
{
	PCMSG_LOGIN = 0x1,
	PCMSG_CONFIG,
	PCMSG_DATETIME,
	PCMSG_CHSTATUS,
	PCMSG_VERSION,
	PCMSG_LOG,
	PCMSG_NIO_TOKEN,
	PCMSG_DBC,
	PCMSG_XCP,
	PCMSG_NIO_CONFIG,
	PCMSG_REBOOT_DEVICE,
	PCMSG_AMP,
	PCMSG_SHELL_EXEC,
	PCMSG_RECORD_WORKING,
	PCMSG_HEARTBEAT,
	PCMSG_GATEWAY
};
static inline const char* PCNAME(enum pcmsg_name name)
{
	switch (name)
	{
		ENUM_TYPE_CASE(PCMSG_LOGIN);
		ENUM_TYPE_CASE(PCMSG_CONFIG);
		ENUM_TYPE_CASE(PCMSG_DATETIME);
		ENUM_TYPE_CASE(PCMSG_CHSTATUS);
		ENUM_TYPE_CASE(PCMSG_VERSION);
		ENUM_TYPE_CASE(PCMSG_LOG);
		ENUM_TYPE_CASE(PCMSG_NIO_TOKEN);
		ENUM_TYPE_CASE(PCMSG_DBC);
		ENUM_TYPE_CASE(PCMSG_XCP);
		ENUM_TYPE_CASE(PCMSG_NIO_CONFIG);
		ENUM_TYPE_CASE(PCMSG_REBOOT_DEVICE);
		ENUM_TYPE_CASE(PCMSG_AMP);
		ENUM_TYPE_CASE(PCMSG_SHELL_EXEC);
		ENUM_TYPE_CASE(PCMSG_RECORD_WORKING);
		ENUM_TYPE_CASE(PCMSG_HEARTBEAT);
		ENUM_TYPE_CASE(PCMSG_GATEWAY);
	}
	return "Unsupported!";
}

enum pcmsg_type
{
	PCMSG_OK = 0,
	PCMSG_ERR,
	PCMSG_GET,
	PCMSG_SET,
	PCMSG_RST,
	PCMSG_ADD,
	PCMSG_DEL,
	PCMSG_SUSPEND,
	PCMSG_RESUME
};
static inline const char* PCTYPE(enum pcmsg_type type)
{
	switch (type)
	{
		ENUM_TYPE_CASE(PCMSG_OK);
		ENUM_TYPE_CASE(PCMSG_ERR);
		ENUM_TYPE_CASE(PCMSG_GET);
		ENUM_TYPE_CASE(PCMSG_SET);
		ENUM_TYPE_CASE(PCMSG_RST);
		ENUM_TYPE_CASE(PCMSG_ADD);
		ENUM_TYPE_CASE(PCMSG_DEL);
		ENUM_TYPE_CASE(PCMSG_SUSPEND);
		ENUM_TYPE_CASE(PCMSG_RESUME);
	}
	return "Unsupported!";

}
/* msg for stconfig */
typedef struct _stconfig_msg
{
	uint32_t ver;           /* define the version */
	uint32_t id;            /* The id value is automatically added to monitor whether the message is lost.  */
	uint32_t name;
	uint32_t type;
	uint32_t len;               /* the length of content */
	char content[];
}stconfig_msg_t;

/*回调函数指针定义 字符串地址 字符串长度 消息名称 消息类型 用户自定义数据指针
字符串地址指针不能修改指针内的内容，只能拷贝出再修改，否则nanamsg会出错*/
typedef void(*steap_callback)(char*, uint32_t, pcmsg_name, pcmsg_type, void*);



typedef struct
{
	char device_ip[MAX_IP_LEN];//设备ip      
	mutex* send_mtx;//发送消息互斥锁.
	int recv_timeout;//接收超时 单位秒
	int send_timeout;//发送超时 单位秒
}steap_device_t;
STEAP_API_NAMESPACE_BEGIN
	/// <summary>
	/// 查找设备,阻塞调用。
	/// </summary>
	/// <param name="dev">设备结构体指针</param>
	/// <param name="cb">用户回调函数</param>
	/// <param name="user_ptr">用户自定义数据指针</param>
	/// <returns>ERR_ALLOC -1,ERR_TIMEOUT -2，ERR_REQ_FAIL -3,RES_OK 0</returns>
	DLL_API int find_device(steap_device_t* dev, steap_callback cb, void* user_ptr);
/// <summary>
/// 获取设备版本信息
/// </summary>
/// <param name="dev">设备结构体指针</param>
/// <param name="cb">用户回调函数</param>
/// <param name="user_ptr">用户自定义数据指针</param>
/// <returns>ERR_ALLOC -1,ERR_TIMEOUT -2，ERR_REQ_FAIL -3,RES_OK 0</returns>
DLL_API int get_device_version(steap_device_t* dev, steap_callback cb, void* user_ptr);
/// <summary>
/// 获取设备时间
/// </summary>
/// <param name="dev">设备结构体指针</param>
/// <param name="cb">用户回调函数</param>
/// <param name="user_ptr">用户自定义数据指针</param>
/// <returns>ERR_ALLOC -1,ERR_TIMEOUT -2，ERR_REQ_FAIL -3,RES_OK 0</returns>
DLL_API int get_device_date_time(steap_device_t* dev, steap_callback cb, void* user_ptr);
/// <summary>
/// 获取通道流量信息
/// </summary>
/// <param name="dev">设备结构体指针</param>
/// <param name="cb">用户回调函数</param>
/// <param name="user_ptr">用户自定义数据指针</param>
/// <returns>ERR_ALLOC -1,ERR_TIMEOUT -2，ERR_REQ_FAIL -3,RES_OK 0</returns>
DLL_API int get_channel_throughput(steap_device_t* dev, steap_callback cb, void* user_ptr);
/// <summary>
/// 获取设备配置信息
/// </summary>
/// <param name="dev">设备结构体指针</param>
/// <param name="cb">用户回调函数</param>
/// <param name="user_ptr">用户自定义数据指针</param>
/// <returns>ERR_ALLOC -1,ERR_TIMEOUT -2，ERR_REQ_FAIL -3,RES_OK 0</returns>
DLL_API int get_device_config(steap_device_t* dev, steap_callback cb, void* user_ptr);
/// <summary>
/// 设置udp数据流ip和端口
/// </summary>
/// <param name="dev">设备结构体指针</param>
/// <param name="ip_port_str">数据流ip和端口号字符串 eg.192.168.100.100:6666</param>
/// <param name="cb">用户回调函数</param>
/// <param name="user_ptr">用户自定义数据指针</param>
/// <returns>ERR_ALLOC -1,ERR_TIMEOUT -2，ERR_REQ_FAIL -3,RES_OK 0</returns>
DLL_API int set_gateway_ip_port(steap_device_t* dev, char* ip_port_str, steap_callback cb, void* user_ptr);
/// <summary>
/// 获取设备日志文件
/// </summary>
/// <param name="dev">设备结构体指针</param>
/// <param name="cb">用户回调函数</param>
/// <param name="user_ptr">用户自定义数据指针</param>
/// <returns>ERR_ALLOC -1,ERR_TIMEOUT -2，ERR_REQ_FAIL -3,RES_OK 0</returns>
DLL_API int get_device_log(steap_device_t* dev, steap_callback cb, void* user_ptr);
/// <summary>
/// 获取AMP设备配置
/// </summary>
/// <param name="dev">设备结构体指针</param>
/// <param name="cb">用户回调函数</param>
/// <param name="user_ptr">用户自定义数据指针</param>
/// <returns>ERR_ALLOC -1,ERR_TIMEOUT -2，ERR_REQ_FAIL -3,RES_OK 0</returns>
DLL_API int get_amp_device_config(steap_device_t* dev, steap_callback cb, void* user_ptr);
/// <summary>
/// 设置amp设备配置字符串
/// </summary>
/// <param name="dev">设备结构体指针</param>
/// <param name="amp_config_json">amp设备配置json字符串</param>
/// <param name="cb">用户回调函数</param>
/// <param name="user_ptr">用户自定义数据指针</param>
/// <returns>ERR_ALLOC -1,ERR_TIMEOUT -2，ERR_REQ_FAIL -3,RES_OK 0</returns>
DLL_API int set_amp_device_config(steap_device_t* dev, char* amp_config_json, steap_callback cb, void* user_ptr);
/// <summary>
/// 删除异常的amp设备
/// </summary>
/// <param name="dev">设备结构体指针</param>
/// <param name="cb">用户回调函数</param>
/// <param name="user_ptr">用户自定义数据指针</param>
/// <returns>ERR_ALLOC -1,ERR_TIMEOUT -2，ERR_REQ_FAIL -3,RES_OK 0</returns>
DLL_API int delete_amp_device(steap_device_t* dev, steap_callback cb, void* user_ptr);
/// <summary>
/// 重启数采设备
/// </summary>
/// <param name="dev">设备结构体指针</param>
/// <param name="cb">用户回调函数</param>
/// <param name="user_ptr">用户自定义数据指针</param>
/// <returns>ERR_ALLOC -1,ERR_TIMEOUT -2，ERR_REQ_FAIL -3,RES_OK 0</returns>
DLL_API int reboot_device(steap_device_t* dev, steap_callback cb, void* user_ptr);
/// <summary>
/// 执行用户自定义脚本
/// </summary>
/// <param name="dev">设备结构体指针</param>
/// <param name="shell_str">用户自定义脚本字符串</param>
/// <param name="cb">用户回调函数</param>
/// <param name="user_ptr">用户自定义数据指针</param>
/// <returns>ERR_ALLOC -1,ERR_TIMEOUT -2，ERR_REQ_FAIL -3,RES_OK 0</returns>
DLL_API int set_shell_exec(steap_device_t* dev, char* shell_str, steap_callback cb, void* user_ptr);
/// <summary>
/// 设置设备时间，如果传入时间字符串指针为空获取本地时间并设置默认时区
/// </summary>
/// <param name="dev">设备结构体指针</param>
/// <param name="time_json">时间字符串 eg. {"time_str":"2022-01-01 00:00:00","time_zone_str":"Asia/Shanghai"}</param>
/// <param name="cb">用户回调函数</param>
/// <param name="user_ptr">用户自定义数据指针</param>
/// <returns>ERR_ALLOC -1,ERR_TIMEOUT -2，ERR_REQ_FAIL -3,RES_OK 0</returns>
DLL_API int set_device_date_time(steap_device_t* dev, char* time_json, steap_callback cb, void* user_ptr);
/// <summary>
/// 重置设备流量信息
/// </summary>
/// <param name="dev">设备结构体指针</param>
/// <param name="cb">用户回调函数</param>
/// <param name="user_ptr">用户自定义数据指针</param>
/// <returns>ERR_ALLOC -1,ERR_TIMEOUT -2，ERR_REQ_FAIL -3,RES_OK 0</returns>
DLL_API int reset_channel_throughput(steap_device_t* dev, steap_callback cb, void* user_ptr);
/// <summary>
/// 设置设备配置信息
/// </summary>
/// <param name="dev"></param>
/// <param name="config_str"></param>
/// <param name="cb"></param>
/// <param name="user_ptr">用户自定义数据指针</param>
/// <returns>ERR_ALLOC -1,ERR_TIMEOUT -2，ERR_REQ_FAIL -3,RES_OK 0</returns>
DLL_API int set_device_config(steap_device_t* dev, char* config_str, steap_callback cb, void* user_ptr);
/// <summary>
/// 向设备发送心跳包
/// </summary>
/// <param name="dev">设备结构体指针</param>
/// <param name="cb">用户回调函数</param>
/// <param name="user_ptr">用户自定义数据指针</param>
/// <returns>ERR_ALLOC -1,ERR_TIMEOUT -2，ERR_REQ_FAIL -3,RES_OK 0</returns>
DLL_API int device_heartbeat(steap_device_t* dev, steap_callback cb, void* user_ptr);
/// <summary>
/// 停止设备udp转发报文
/// </summary>
/// <param name="dev">设备结构体指针</param>
/// <param name="config_str">设备配置json字符串</param>
/// <param name="cb">用户回调函数</param>
/// <param name="user_ptr">用户自定义数据指针</param>
/// <returns>ERR_ALLOC -1,ERR_TIMEOUT -2，ERR_REQ_FAIL -3,RES_OK 0</returns>
DLL_API int stop_udp_gateway(steap_device_t* dev, steap_callback cb, void* user_ptr);
/// <summary>
/// 开始设备udp转发报文
/// </summary>
/// <param name="dev">设备结构体指针</param>
/// <param name="config_str">设备配置json字符串</param>
/// <param name="cb">用户回调函数</param>
/// <param name="user_ptr">用户自定义数据指针</param>
/// <returns>ERR_ALLOC -1,ERR_TIMEOUT -2，ERR_REQ_FAIL -3,RES_OK 0</returns>
DLL_API int start_udp_gateway(steap_device_t* dev, char* config_str, steap_callback cb, void* user_ptr);
/// <summary>
/// 获取设备记录数据状态
/// </summary>
/// <param name="dev">设备结构体指针</param>
/// <param name="cb">用户回调函数</param>
/// <param name="user_ptr">用户自定义数据指针</param>
/// <returns></returns>
DLL_API int get_data_record_status(steap_device_t* dev, steap_callback cb, void* user_ptr);
/// <summary>
/// 开始设备数据记录
/// </summary>
/// <param name="dev">设备结构体指针</param>
/// <param name="cb">用户回调函数</param>
/// <param name="user_ptr">用户自定义数据指针</param>
/// <returns></returns>
DLL_API int start_data_record(steap_device_t* dev, steap_callback cb, void* user_ptr);
/// <summary>
/// 停止设备数据记录
/// </summary>
/// <param name="dev">设备结构体指针</param>
/// <param name="cb">用户回调函数</param>
/// <param name="user_ptr">用户自定义数据指针</param>
/// <returns></returns>
DLL_API int stop_data_record(steap_device_t* dev, steap_callback cb, void* user_ptr);
/// <summary>
/// uds发送命令函数（目前未实现）
/// </summary>
/// <param name="dev">设备结构体指针</param>
/// <param name="cb">用户回调函数</param>
/// <param name="user_ptr">用户自定义数据指针</param>
/// <returns>ERR_ALLOC -1,ERR_TIMEOUT -2，ERR_REQ_FAIL -3,RES_OK 0</returns>
DLL_API int uds_send_command(steap_device_t* dev, steap_callback cb, void* user_ptr);
/// <summary>
/// uds接收命令函数（目前未实现）
/// </summary>
/// <param name="dev">设备结构体指针</param>
/// <param name="cb">用户回调函数</param>
/// <param name="user_ptr">用户自定义数据指针</param>
/// <returns>ERR_ALLOC -1,ERR_TIMEOUT -2，ERR_REQ_FAIL -3,RES_OK 0</returns>
DLL_API int uds_receive_command(steap_device_t* dev, steap_callback cb, void* user_ptr);
/// <summary>
/// 初始化设备函数
/// </summary>
/// <param name="dev">设备结构体指针</param>
/// <param name="ip">ip地址字符串</param>
/// <param name="send_timeout">发送超时时间</param>
/// <param name="recv_timeout">接收超时时间</param>
/// <returns>调用成功返回0 调用失败返回-1</returns>
DLL_API int init_steap_device(steap_device_t* dev, char* ip, int send_timeout, int recv_timeout);
/// <summary>
/// 析构设备变量函数
/// </summary>
/// <param name="dev">设备结构体指针</param>
/// <returns>调用成功返回0 调用失败返回-1</returns>
DLL_API int deinit_steap_device(steap_device_t* dev);
STEAP_API_NAMESPACE_END

#endif
