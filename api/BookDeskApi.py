import requests

class BookDeskApi(object):
    def api_post_bookdeskapi(self,url,headers,payload):

        return requests.post(url,headers=headers,json=payload)

