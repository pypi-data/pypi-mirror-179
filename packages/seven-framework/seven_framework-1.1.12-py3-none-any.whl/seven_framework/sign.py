# -*- coding: utf-8 -*-
"""
:Author: ChenXiaolei
:Date: 2020-08-24 16:50:09
:LastEditTime: 2022-11-23 15:18:36
:LastEditors: ChenXiaolei
:Description: 签名帮助类
"""
from .crypto import CryptoHelper


class SignHelper(object):
    """ 
    :Description: 签名工具类
    """
    @classmethod
    def params_sign_md5(self,
                        params=None,
                        sign_key=None,
                        sign_lower=False,
                        reverse=False,
                        is_sign_key=False,
                        param_join_str="",
                        kv_join_str=""):
        """
        :Description: 生成签名
        :param params: 必要参数，为字典格式
        :param sign_key: 应用密钥
        :param sign_lower: 返回签名是否小写(默认大写)
        :param reverse: 是否反排序 False:升序 True:降序
        :param is_sign_key: 参数名是否参与签名(默认False不参与)
        :param param_join_str: 参数之前连接的字符串
        :param kv_join_str: is_sign_key=True时,key与value之前连接的字符串
        :return sign: 签名 
        :last_editors: ChenXiaolei
        """

        # 所有参数生成字典
        sign_params = {}
        for k, v in params.items():
            if k.lower() == "sign":
                continue
            sign_params[k] = v

        # 取出字典元素按key的字母升序排序形成列表
        params_sorted = sorted(sign_params.items(),
                               key=lambda e: e[0],
                               reverse=reverse)
        sign = CryptoHelper.md5_encrypt(param_join_str.join(
            u"{}".format(k + kv_join_str + str(v) if is_sign_key else str(v))
            for k, v in params_sorted) + sign_key)

        if sign and sign_lower:
            sign = sign.lower()
        else:
            sign = sign.upper()

        return sign

    @classmethod
    def get_sign_params_str(self,
                            params=None,
                            sign_key=None,
                            reverse=False,
                            is_sign_key=False):
        """
        :description: 获取签名参数字符串(签名MD5前的加密串)
        :param params: 必要参数，为字典格式
        :param sign_key: 应用密钥
        :param reverse: 是否反排序 False:升序 True:降序
        :param is_sign_key: 参数名是否参与签名(默认False不参与)
        :return sign: 签名MD5前的加密串
        :last_editors: ChenXiaolei
        """
        # 所有参数生成字典
        sign_params = {}
        for k, v in params.items():
            if k.lower() == "sign":
                continue
            sign_params[k] = v

        # 取出字典元素按key的字母升序排序形成列表
        params_sorted = sorted(sign_params.items(),
                               key=lambda e: e[0],
                               reverse=reverse)
        sign_params_str = "".join(
            u"{}".format(k + v if is_sign_key else v)
            for k, v in params_sorted) + sign_key

        return sign_params_str