from pn1.utils.operationExcel import OperationExcel
from pn1.utils.OperationJson import OperationJson
import json
from pn1.utils.public import *


operationJson = OperationJson()
operationExcel = OperationExcel()


def setSo(kd='自动化测试工程师'):
    """对搜索的数据重新赋值"""
    dict1 = json.loads(operationJson.getRequestsData(1))
    dict1['kd'] = kd
    return dict1


def writePositionId(content):
    """把职位的ID写到文件中"""
    with open(get_dir(filename='positionId'), 'w') as f:
        f.write(content)


def getPositionId():
    """获取职位招聘的ID"""
    with open(get_dir(filename='positionId'), 'r') as f:
        return json.loads(f.read())


def setpositionInfo(row):
    dict1 = json.loads(operationJson.getRequestsData(row=row))
    dict1['positionId'] = getPositionId()[0]
    return dict1


def getUrl(positionID):
    # urlInfo = operationExcel.get_url(2)
    listUrl = []
    for item in getPositionId():
        urlInfo = 'https://www.lagou.com/jobs/{0}.html'.format(item)
        listUrl.append(urlInfo)
    return listUrl


#print(setSo('性能测试工程师'))

# print(type(getPositionId()))
# print(getUrl(getPositionId()))
print(getUrl(getPositionId()))