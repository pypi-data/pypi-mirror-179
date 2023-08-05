import os, sys, json
from epkernel import epcam, BASE

def init(path:str): 
    epcam.init(path)
    BASE.set_config_path(path)

def set_sys_attr_path(path:str):
    try:
        BASE.set_sysAttr_path(path)
    except Exception as e:
        print(e)
    return 

def set_user_attr_path(path:str):
    try:
        BASE.set_userAttr_path(path)
    except Exception as e:
        print(e)
    return  
