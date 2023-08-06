#ifndef _DEVICE_CONTROL_MODULE_H_
#define _DEVICE_CONTROL_MODULE_H_
#include <Python.h>
#include "object_steap_device.h"

#define DEVICE_CONTROL_MODULE_NAME "slthost.dev_ctl"
#define DEVICE_CONTROL_MODULE_DESCRIPTION "Copyright Sealta, Inc."
#define DEVICE_CONTROL_MODULE_VERSION 001


#define _DOC_DEV_CTL_MODULE \
    "Python C code module, used to control the sealta device" \
    "\t>>> from slthost import dev_ctl\n" \
    "\t>>> dev = dev_ctl.create_steap_device(\"192.168.100.100\", 3, 3)\n" \
    "\t>>> res_code,res_string = dev.start_data_record()\n" \
    "\t>>> res_code,res_string = dev.stop_data_record()\n" \
    "\t>>> res_code=dev_ctl.delete_steap_device(dev)\n" \
    "\n" 



#define _DOC_CREATE_DEVICES \
DEVICE_CONTROL_MODULE_NAME ".create_steap_device(ip,send_timeout,recv_timeout)\n" \
"\n" \
"create steap device class. return a :class:`" DEVICE_CONTROL_MODULE_NAME "." STEAP_DEVICE_OBJECT_NAME "`" \
"\n" \
"Args:\n" \
"\tip (string): device ip address\n\n" \
"\tsend_timeout (int): send timeout (uint s)\n\n" \
"\trecv_timeout (int): receive timeout (uint s)\n\n" \
"\n" \
"Raises:\n" \
"\t:class:`" DEVICE_CONTROL_MODULE_NAME ".RuntimeError`\n" \
"\n" \
"Returns:\n" \
"\t:class:`" DEVICE_CONTROL_MODULE_NAME "." STEAP_DEVICE_OBJECT_NAME "`. \n" \
"\n" \
"\t>>> from slthost import dev_ctl\n" \
"\t>>> dev = dev_ctl.create_steap_device(\"192.168.100.100\", 3, 3)\n" \
"\t>>> res_code,res_string = dev.start_data_record()\n" \
"\n" \
".. note::\n\t:class:`" DEVICE_CONTROL_MODULE_NAME "." STEAP_DEVICE_OBJECT_NAME "` should be delete by user call delete_steap_device()\n\n"

#define _DOC_DELETE_DEVICES \
DEVICE_CONTROL_MODULE_NAME ".delete_steap_device(ip,send_timeout,recv_timeout)\n" \
"\n" \
"delete steap device class. return 0" \
"\n" \
"Args:\n" \
"\tsteap_device_object (:class:`" DEVICE_CONTROL_MODULE_NAME "." STEAP_DEVICE_OBJECT_NAME "`): :class:`" DEVICE_CONTROL_MODULE_NAME "." STEAP_DEVICE_OBJECT_NAME "`" \
"\n" \
"Raises:\n" \
"\t:class:`" DEVICE_CONTROL_MODULE_NAME ".RuntimeError`\n" \
"\n" \
"Returns:\n" \
"\t0 \n" \
"\n" \
"\t>>> from slthost import dev_ctl\n" \
"\t>>> dev = dev_ctl.create_steap_device(\"192.168.100.100\", 3, 3)\n" \
"\t>>> res_code,res_string = dev.start_data_record()\n" \
"\t>>> res_code=dev_ctl.delete_steap_device(dev)\n" \
"\n" \
".. note::\n\t:class:`" DEVICE_CONTROL_MODULE_NAME "." STEAP_DEVICE_OBJECT_NAME "` should be delete by user call delete_steap_device()\n\n"

#define _DOC_START_DATA_RECORD \
STEAP_DEVICE_OBJECT_NAME ".start_data_record()\n" \
"\n" \
"send command to make the sealta device start recording " \
"\n" \
"Args:\n" \
"\n" \
"Raises:\n" \
"\t:class:`" DEVICE_CONTROL_MODULE_NAME ".RuntimeError`\n" \
"\n" \
"Returns:\n" \
"\tTuple: ((int)result code, (string)result content string),\n" \
"\tresult code:\n"\
"\t\tRES_OK 0\n"\
"\t\tERR_ALLOC -1\n"\
"\t\tERR_TIMEOUT -2\n"\
"\t\tERR_REQ_FAIL -3\n"\
"\n" \
"\t>>> from slthost import dev_ctl\n" \
"\t>>> dev = dev_ctl.create_steap_device(\"192.168.100.100\", 3, 3)\n" \
"\t>>> res_code,res_string = dev.start_data_record()\n" \
"\t>>> res_code=dev_ctl.delete_steap_device(dev)\n" \
"\n" \
".. note::\n\t\n\n"

#define _DOC_STOP_DATA_RECORD \
STEAP_DEVICE_OBJECT_NAME ".stop_data_record()\n" \
"\n" \
"send command to make the sealta device stop recording " \
"\n" \
"Args:\n" \
"\n" \
"Raises:\n" \
"\t:class:`" DEVICE_CONTROL_MODULE_NAME ".RuntimeError`\n" \
"\n" \
"Returns:\n" \
"\tTuple: ((int)result code, (string)result content string),\n" \
"\tresult code:\n"\
"\t\tRES_OK 0\n"\
"\t\tERR_ALLOC -1\n"\
"\t\tERR_TIMEOUT -2\n"\
"\t\tERR_REQ_FAIL -3\n"\
"\n" \
"\t>>> from slthost import dev_ctl\n" \
"\t>>> dev = dev_ctl.create_steap_device(\"192.168.100.100\", 3, 3)\n" \
"\t>>> res_code,res_string = dev.start_data_record()\n" \
"\t>>> res_code,res_string = dev.stop_data_record()\n" \
"\t>>> res_code=dev_ctl.delete_steap_device(dev)\n" \
"\n" \
".. note::\n\t\n\n"

#ifdef _cplusplus
extern "C" {
#endif

    //int setup_module_defines(PyObject* module);

#ifdef _cplusplus
}
#endif // extern "C" {

#endif