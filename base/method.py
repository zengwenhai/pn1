import requests
from pn1.utils.excel_data import *
from pn1.utils.operationExcel import OperationExcel
from pn1.utils.OperationJson import OperationJson
from pn1.page.IaGou import *

# operationExcel = OperationExcel()
# print(operationExcel.get_url(1))


# def checkHeader(row, f1=None, f2=None):
#     """检测请求头"""
#     url = operationExcel.get_url(row=row)
#     url = url.split('/')
#     if url[4] == 'positionAjax.json?needAddtionalResult=false':
#         return f1
#     elif url[5] == 'byPosition.json':
#         return f2


class Method(object):

    def __init__(self):
        self.operationJson = OperationJson()
        self.excel = OperationExcel()

    # def post(self, row):
    #     try:
    #         r = requests.post(url=self.excel.get_url(row=row),
    #                           data=self.operationJson.getRequestsData(row=row),
    #                           headers= getHeadersValue(),
    #                           timeout=5,
    #                           verify=False)
    #         return r
    #     except Exception as e:
    #         raise RuntimeError('接口请求发生未知错误')

    def post(self, row, data):
        try:
            r = requests.post(url=self.excel.get_url(row=row),
                              data=data,
                              headers= getHeadersValue(),
                              timeout=5,
                              verify=False)
            return r
        except Exception as e:
            raise RuntimeError('接口请求发生未知错误')


    def get(self, url, params=None):
        r = requests.get(url=url, params=params,
                         headers=getHeadersValue(),
                         timeout=6)
        return r


class IsContent:

    def __init__(self):
        self.excel = OperationExcel()

    def isContent(self, row, str2):
        flag = None
        if self.excel.getExpect(row=row) in str2:
            flag = True
        else:
            flag = False
        return flag