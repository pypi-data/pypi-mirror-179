#include "defines.h"
#include "exceptions.h"
#include "device_control_module.h"


static int steap_device_object_alloc(steap_device_object* self, PyObject* args, PyObject* kwds)
{
    self->name = PyUnicode_FromString("");
    self->dev = (steap_device_t*)malloc(sizeof(steap_device_t)/sizeof(char));
    if (self->dev == NULL)
    {
        set_exception((char*)"malloc steap device fail\n");
    }
    else
    {
        memset(self->dev, 0, sizeof(steap_device_t));
    }
    return 0;
}
static void steap_device_object_dealloc(steap_device_object* self)
{
    if (self->dev != NULL)
    {
        free(self->dev);
        self->dev = NULL;
    }
    Py_XDECREF(self->name);
    Py_TYPE(self)->tp_free((PyObject*)self);
}

static PyObject* steap_device_object_getattr(PyObject* o, PyObject* attr_name)
{
    return PyObject_GenericGetAttr(o, attr_name);
}
static int steap_device_object_setattr(PyObject* o, PyObject* name, PyObject* value)
{
    return PyObject_GenericSetAttr(o, name, value);
}
// Shamelessly copied from base36enc
static PyObject* convert_to_base36(unsigned long value)
{
    char base36[37] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    /* log(2**64) / log(36) = 12.38 => max 13 char + '\0' */
    char buffer[100];
    unsigned int offset = sizeof(buffer);

    buffer[--offset] = '\0';
    do {
        buffer[--offset] = base36[value % 36];
    } while (value /= 36);
    return PyUnicode_FromString(&buffer[offset]);
}

static PyObject* steap_device_object_tp_repr(PyObject* o)
{
    // example output: <ics.NeoDevice neoVI FIRE2 CY1234>
    steap_device_object* sd = (steap_device_object*)(o);
    
    return PyUnicode_FromFormat("<" DEVICE_CONTROL_MODULE_NAME "." STEAP_DEVICE_OBJECT_NAME " %U >", sd->name);
}
/*********************************device control interface*********************************************/
void user_callback(char* content, uint32_t content_len, pcmsg_name name, pcmsg_type type, void* user_ptr)
{
    if (strcmp(content, RECV_TIMEOUT_STR) == 0)
    {
        PySteapDevice_GetSteapDevice(user_ptr)->response_content =
            Py_BuildValue("s", "receive timeout");
    }
    else
    {
        PySteapDevice_GetSteapDevice(user_ptr)->response_content = 
            Py_BuildValue("s#", content, content_len);
    }

}
PyObject* meth_start_data_record(PyObject* self, PyObject* args)
{
    int ret = 0;
    if (!PyArg_ParseTuple(args, arg_parse(":", __FUNCTION__))) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
    ret = steap_api::start_data_record((PySteapDevice_GetSteapDevice(self)->dev),
        user_callback, (void*)self);
    //ret = steap_api::start_data_record((PySteapDevice_GetSteapDevice(self)->dev),
    //    NULL, NULL);
    Py_END_ALLOW_THREADS
    PyObject* value = Py_BuildValue("iO", ret, PySteapDevice_GetSteapDevice(self)->response_content);
    
    return value;
   
}
PyObject* meth_stop_data_record(PyObject* self, PyObject* args)
{
    int ret = 0;
    if (!PyArg_ParseTuple(args, arg_parse(":", __FUNCTION__))) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
    ret = steap_api::stop_data_record((PySteapDevice_GetSteapDevice(self)->dev),
        user_callback, (void*)self);
    Py_END_ALLOW_THREADS
    PyObject* value = Py_BuildValue("IO", ret, PySteapDevice_GetSteapDevice(self)->response_content);
    return value;
}

static PyMethodDef steap_device_object_methods[] = {
    { "start_data_record",  meth_start_data_record,  METH_VARARGS, _DOC_START_DATA_RECORD},
    { "stop_data_record",  meth_stop_data_record,  METH_VARARGS, _DOC_STOP_DATA_RECORD},
    { NULL, NULL, 0, NULL },
};
static PyMemberDef steap_device_object_members[] = {
    { (char*)"Name", T_OBJECT_EX, offsetof(steap_device_object, name), 0, (char*)"String describing DeviceType, extension to Python api only." },
    //{ (char*)"Dev", T_OBJECT, offsetof(steap_device_object, dev), 0, (char*)"" },
    { NULL, 0, 0, 0, 0 },
};
PyTypeObject steap_device_object_type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    DEVICE_CONTROL_MODULE_NAME "." STEAP_DEVICE_OBJECT_NAME,             /* tp_name */
    sizeof(steap_device_object), /* tp_basicsize */
    0,                         /* tp_itemsize */
    (destructor)steap_device_object_dealloc,/* tp_dealloc */
    0,                         /* tp_print */
    0,                         /* tp_getattr */
    0,                         /* tp_setattr */
    0,                         /* tp_reserved */
    steap_device_object_tp_repr, /* tp_repr */
    0,                         /* tp_as_number */
    0,                         /* tp_as_sequence */
    0,                         /* tp_as_mapping */
    0,                         /* tp_hash  */
    0,                         /* tp_call */
    0,                         /* tp_str */
    steap_device_object_getattr, /* tp_getattro */
    steap_device_object_setattr, /* tp_setattro */
    0,                         /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,        /* tp_flags */
    STEAP_DEVICE_OBJECT_NAME" object",           /* tp_doc */
    0,                         /* tp_traverse */
    0,                         /* tp_clear */
    0,                         /* tp_richcompare */
    0,                         /* tp_weaklistoffset */
    0,                         /* tp_iter */
    0,                         /* tp_iternext */
    steap_device_object_methods, /* tp_methods */
    steap_device_object_members, /* tp_members */
    0,                         /* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    (initproc)steap_device_object_alloc, /* tp_init */
};

bool setup_steap_device_object(PyObject* module)
{
    //neo_device_object_type.ob_type = &PyType_Type;
    steap_device_object_type.tp_new = PyType_GenericNew;
    steap_device_object_type.tp_dictoffset = offsetof(steap_device_object, dict);
    if (PyType_Ready(&steap_device_object_type) < 0) {
        return false;
    }
    Py_INCREF(&steap_device_object_type);
    PyModule_AddObject(module, STEAP_DEVICE_OBJECT_NAME, (PyObject*)&steap_device_object_type);
    return true;
}