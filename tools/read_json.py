import json

class ReadJson(object):
    '''初始化的方法读取文件名称'''
    def __init__(self,filename):
        self.filepath="../data/"+filename

    def read_json(self):
        with open(self.filepath,"r",encoding="utf-8") as f:
            '''调用load方法加载文件流'''
            return json.load(f)

if __name__ == '__main__':
    data=ReadJson("bookdesk.json").read_json()
    arrs=[((data.get("url"),
                 data.get("headers"),
                 data.get("payload"),
                 data.get("epect_result"),
                 data.get("status_code")))]
    print(arrs)