#ifndef _DEFINES_H_
#define _DEFINES_H_
#include <Python.h>
// https://bugs.python.org/issue28769
// 2.x     = char* PyString_AsString(return_value);
// 3.0-3.6 = char* PyUnicode_AsUTF8(value);
// 3.7     = const char* PyUnicode_AsUTF8(value);
#if (PY_MAJOR_VERSION >= 3) && (PY_MINOR_VERSION >= 7)
#define PyUniStr_AsStrOrUTF8(obj) (char*)PyUnicode_AsUTF8(obj)
#elif (PY_MAJOR_VERSION >= 3)
#define PyUniStr_AsStrOrUTF8(obj) PyUnicode_AsUTF8(obj)
#elif (PY_MAJOR_VERSION == 2)
#define PyUniStr_AsStrOrUTF8(obj) PyString_AsString(obj)
#else
#error Failed to suppport PyUnicode_AsUTF8
#endif

 // __func__, __FUNCTION__ and __PRETTY_FUNCTION__ are not preprocessor macros.
 // but MSVC doesn't follow c standard and treats __FUNCTION__ as a string literal macro...
#ifdef _MSC_VER
#define arg_parse(a,f) a f
#else
const char* arg_parse(const char* args, const char* func)
{
    static char buffer[128];
    memset(buffer, '\0', sizeof(buffer) / sizeof(buffer[0]));
    strcpy(buffer, args);
    strcat(buffer, func);
    return (const char*)buffer;
}
#endif

#endif 

