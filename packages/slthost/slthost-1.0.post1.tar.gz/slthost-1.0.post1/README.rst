# slthost

Python C code module, used to control the sealta device

# Installing

- `pip install slthost`

# How to use

#### C API can be mimiced almost identically by doing the following:

    >>> from slthost import dev_ctl
    >>> dev = dev_ctl.create_steap_device(\"192.168.100.100\", 3, 3)
    >>> res_code,res_string = dev.start_data_record()
    >>> res_code,res_string = dev.stop_data_record()
    >>> res_code=dev_ctl.delete_steap_device(dev)
