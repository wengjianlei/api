import unittest
from api.BookDeskApi import BookDeskApi
from parameterized import parameterized
from tools.read_json import ReadJson
import json
#读取数据函数
def get_data():
    data = ReadJson("bookdesk.json").read_json()
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("payload")))
    return arrs

class TestBookDesk(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_bookdesk(self, url, headers,payload):
        #调用书桌方法
        s=BookDeskApi().api_post_bookdeskapi(url,headers,payload)
        print("查看响应结果", s.json())

if __name__ == '__main__':
    unittest.main()
