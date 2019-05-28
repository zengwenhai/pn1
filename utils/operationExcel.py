import xlrd
from xlutils.copy import copy
from pn1.utils.public import *
from pn1.utils.excel_data import *


class OperationExcel(object):
    def getExcel(self):
        db = xlrd.open_workbook(get_dir('data', 'data.xls'))
        sheet = db.sheet_by_name('Sheet1')
        return sheet

    def get_rows(self,):
        """获取数据表的行数"""
        return self.getExcel().nrows

    def get_row_col(self, row, col):
        """获取单元格的内容"""
        return self.getExcel().cell_value(row, col)

    def get_values(self, sheet, n):
        """获取数据表的行数据,每行数据以列表形式返回"""
        list1 = []
        for i in range(n):
            list1.append(sheet.row_values(i))
        return list1

    def get_url(self, row):
        """获取url地址"""
        return self.get_row_col(row, getUrl())

    def get_request_data(self, row):
        """获取请求参数"""
        return self.get_row_col(row, getRequest_data())

    def getExpect(self, row):
        """获取期望结果"""
        return self.get_row_col(row, getExpect())

    def getResult(self, row):
        """获取实际结果"""
        return self.get_row_col(row, getResult())

    def writeResult(self, row, content):
        """测试结果写到文件中"""
        col = getResult()
        work = xlrd.open_workbook(get_dir('data', 'data.xls'))
        old_content = copy(work)
        ws = old_content.get_sheet(0)
        ws.write(row, col, content)
        old_content.save(get_dir('data', 'data.xls'))

    def get_alls(self):
        """获取所有测试用例数"""
        return (self.get_rows() - 1)

    def run_success_result(self):
        """获取执行成功的用例数"""
        pass_count = []
        fail_count = []
        for i in range(1, self.get_rows()):
            if self.getResult(i) == 'pass':
                pass_count.append(i)
            return int(len(pass_count))

    def run_fail_result(self):
        """获取执行失败的用例数"""
        return int(self.get_rows() - 1) -self.run_success_result()

    def run_pass_rate(self):
        """测试结果通过率"""
        rate = ''
        if self.run_fail_result() == 0:
            rate = '100%'
        elif self.run_fail_result() != 0:
            rate = str(int(self.run_success_result()/(self.get_rows()-1)*100)) + '%'
        return rate



if __name__ == "__main__":
    oper = OperationExcel()
    # sheet = oper.getExcel()
    # print(oper.get_rows(sheet))
    # print(oper.get_values(sheet, oper.get_rows(sheet)))
    # print(oper.get_row_col(1,1))
    print(oper.run_success_result())
    print(oper.run_pass_rate())