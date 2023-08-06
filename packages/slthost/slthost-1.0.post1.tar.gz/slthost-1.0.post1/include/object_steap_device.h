#ifndef _OBJECT_STEAP_DEVICE_H_
#define _OBJECT_STEAP_DEVICE_H_

#include <Python.h>
#include <structmember.h>
#include "steap_control_api.h"


#define STEAP_DEVICE_OBJECT_NAME "steap_device"

typedef struct {
    PyObject_HEAD
    steap_device_t* dev;
    PyObject* response_content;
    PyObject* name;
    PyObject* dict;
} steap_device_object;

extern PyTypeObject steap_device_object_type;

// Copied from tupleobject.h
#define PySteapDevice_GetSteapDevice(sd) ((steap_device_object*)sd)
#define PySteapDevice_GetName(sd) (PySteapDevice_GetSteapDevice(sd)->name)

#define PySteapDevice_Check(op) \
    PyType_FastSubclass(Py_TYPE(op), Py_TPFLAGS_BASETYPE)
#define PySteapDevice_CheckExact(op) (Py_TYPE(PySteapDevice_GetSteapDevice(op)) == &steap_device_object_type)



bool setup_steap_device_object(PyObject* module);

#endif // _OBJECT_NEO_DEVICE_H_
