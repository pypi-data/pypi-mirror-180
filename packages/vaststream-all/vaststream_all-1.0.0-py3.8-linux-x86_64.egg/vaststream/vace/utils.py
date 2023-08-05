"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8

__all__ = ["err_check", "readImageFile", "genFileMd5sum", "genBufferMd5sum", "saveHandelToImage"]

from typing import Any
from _vaststream_pybind11 import vace as _vace
from vaststream.vacm.common import DataBuffer
from vaststream.vacm.common import DataHandle

def err_check(func):
    def wrapper(*args,**kwargs):
        ret = func(*args,**kwargs)
        if ret != _vace.vaceER_SUCCESS:
            raise Exception(f"{func.__name__} return error {ret}.")
        return ret
    return wrapper

# ================================ API ============================
def readImageFile(imageFile:str, 
                  imageWidth:int, 
                  imageHeight:int,
                  memSize:int) -> DataHandle:
    """
    Read image file to buffer.\n
    """
    _hadle = _vace.readImageFile(imageFile, imageWidth, imageHeight, memSize)
    return DataHandle(_hadle)

def genFileMd5sum(imageFile: str) -> str:
    """
    generate file md5 sum\n
    imageFile [in]: image file name.\n
    """
    return _vace.genFileMd5sum(imageFile)

def genBufferMd5sum(bufferHandle: DataBuffer, outputSize: int) -> str:
    """
    generate buffer md5 sum\n
    handle [in]: the handle of buffer.\n
    """
    return _vace.genBufferMd5sum(bufferHandle.ptr, outputSize)

def saveHandelToImage(outputSize: int,
                      outputDevice: DataHandle,
                      imageSavePath: str) -> None:
    """
    saveHandelToImage\n
    outputSize [in]: the size of Handle.\n
    outputDevice [in]: device Handle.\n
    imageSavePath[in]: imgae path.\n
    """
    return _vace.saveHandelToImage(outputSize, outputDevice.ptr, imageSavePath)