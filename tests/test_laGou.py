import unittest
from pn1.base.method import *
from pn1.page.IaGou import *
from pn1.utils.public import *
import json
from pn1.utils.operationExcel import OperationExcel
from pn1.utils.OperationJson import OperationJson


class LaGou(unittest.TestCase):

    def setUp(self):
        self.obj = Method()
        self.p = IsContent()
        self.excel = OperationExcel()
        self.operation = OperationJson()

    def statusCode(self, r):
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 0)

    def isContent(self, r, row):
        self.statusCode(r)
        self.assertTrue(self.p.isContent(row=row, str2=r.text))

    def test_laGou_001(self):
        r = self.obj.post(row=1, data=self.operation.getRequestsData(1))
        self.isContent(r=r, row=1)
        self.excel.writeResult(1, 'pass')

    def test_laGou_002(self):
        r = self.obj.post(row=1, data=setSo('性能测试工程师'))
        list1 = []
        for i in range(0, 15):
            positionId = r.json()['content']['positionResult']['result'][i]['positionId']
            list1.append(positionId)
        writePositionId(json.dumps(list1))

    def test_laGou_003(self):
        """访问搜索到的每个职位的详情信息"""
        for i in range(15):
            r = self.obj.get(url=getUrl(getPositionId())[i])
            self.assertTrue(self.p.isContent(row=2, str2=r.text))


if __name__ == "__main__":
    unittest.main(verbosity=2)