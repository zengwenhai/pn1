import os


def get_dir(data='data', filename=None):
    """查找文件目录"""
    dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(dirname, data, filename)

print(get_dir(filename='requestData.json'))