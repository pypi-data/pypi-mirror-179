#ifndef _EXCEPTIONS_H_
#define _EXCEPTIONS_H_
#include <Python.h>

#ifdef _cplusplus
extern "C" {
#endif

PyObject* _set_exception(char* msg, const char* func_name);
#define set_exception(msg) _set_exception(msg, __FUNCTION__);



#ifdef _cplusplus
}
#endif // extern "C" {

#endif // _EXCEPTIONS_H_
