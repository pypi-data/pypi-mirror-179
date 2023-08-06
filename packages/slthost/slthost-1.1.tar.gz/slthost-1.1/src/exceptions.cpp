#include "exceptions.h"
#include <sstream>
PyObject* _set_exception(char* msg, const char* func_name)
{
    std::stringstream ss;
    std::string function = std::string(func_name);
    ss << "Error: " << function << "(): " << msg;
    PyErr_SetString(PyExc_Exception, ss.str().c_str());
    return NULL;
}