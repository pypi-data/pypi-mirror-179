#include <Python.h>
#include "defines.h"
#include "exceptions.h"
#include "steap_control_api.h"
#include "device_control_module.h"


PyObject* meth_create_steap_device(PyObject* self, PyObject* args)
{
    char* ip_str=NULL;
    int send_timeout = 0;
    int recv_timeout = 0;
    if (!PyArg_ParseTuple(args, arg_parse("sii:", __FUNCTION__),
        &ip_str, &send_timeout, &recv_timeout)) {
        return NULL;
    }
    PyObject* obj = PyObject_CallObject((PyObject*)&steap_device_object_type, NULL);
    if (steap_api::init_steap_device((PySteapDevice_GetSteapDevice(obj)->dev),
        ip_str, send_timeout, recv_timeout) == 0)
    {
        return obj;
    }
    else
    {
        return set_exception((char*)"init steap device error");
    }
    return NULL;
}
PyObject* meth_delete_steap_device(PyObject* self, PyObject* args)
{
    PyObject* steap_device_obj = NULL;
    int send_timeout = 0;
    int recv_timeout = 0;
    if (!PyArg_ParseTuple(args, arg_parse("O:", __FUNCTION__),
        &steap_device_obj)) {
        return NULL;
    }
    if (steap_device_obj == NULL)return NULL;
    if (!PySteapDevice_CheckExact(steap_device_obj)) 
    {
        set_exception((char*)"Argument must be of type slthost.dev_ctl.steap_device_object");
    }
    if (steap_api::deinit_steap_device((PySteapDevice_GetSteapDevice(steap_device_obj)->dev)) == 0)
    {
        PyObject* value = Py_BuildValue("i", 0);
        return value;
    }


    return NULL;
}
static bool add_modul_define(PyObject* m)
{
    PyModule_AddIntMacro(m, RES_OK);
    PyModule_AddIntMacro(m, ERR_ALLOC);
    PyModule_AddIntMacro(m, ERR_TIMEOUT);
    PyModule_AddIntMacro(m, ERR_REQ_FAIL);

    return true;
}


static PyMethodDef MethodTable[] = {
    { "create_steap_device",  meth_create_steap_device,  METH_VARARGS, _DOC_CREATE_DEVICES },
    { "delete_steap_device",  meth_delete_steap_device,  METH_VARARGS, _DOC_DELETE_DEVICES },
    { NULL, NULL, 0, NULL}
};


#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    DEVICE_CONTROL_MODULE_NAME,
    _DOC_DEV_CTL_MODULE,
    -1,          /* m_size */
    MethodTable, /* m_methods */
    NULL,        /* m_reload */
    NULL,        /* m_traverse */
    NULL,        /* m_clear */
    NULL,        /* m_free */
};

static PyObject*
moduleinit(void)
{
    PyObject* m = PyModule_Create(&moduledef);
    if (m == NULL) return NULL;
    if(!add_modul_define(m))return NULL;
    setup_steap_device_object(m);
    return m;
}

PyMODINIT_FUNC
PyInit_dev_ctl(void)
{
    return moduleinit();
}

#else
static PyObject*
moduleinit(void)
{
    PyObject* m = Py_InitModule3(MODULE_NAME, MethodTable, MODULE_HELP);
    if (m == NULL) return NULL;
    return m;
}

PyMODINIT_FUNC
init_dev_ctl(void)
{
    moduleinit();
}
#endif
