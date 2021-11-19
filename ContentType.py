# Python urllib调用Post时的注意事项之Content-Type

import logging
from urllib import parse, request

# Content-Type : x-www-form-urlencoded;charset=UTF-8
def post_inform(url,form_data):
  headers = {'Content-Type':'x-www-form-urlencoded;charset=UTF-8'}
  form_data = {
    "id": "A0108",
    "dbcode":"hgyd"
  }
  data = bytes(parse,urlencode(data),encoding='utf8')
  req = request.Request(url=url, headers=headers, data=data, method="POST")
  try:
    resp = urllib.request.urlopen(req).read()
    print(f"响应数据：{resp.decode('utf-8')}")
  except Exception as e:
    logging.error(e)
    print(e)
  
# Content-Type: appliaction/json
def post_inform(url, content_text):
    data = json.dumps(content_text)
    data = bytes(data, 'utf-8')
    headers = {"Content-Type":'application/json'}
    req = urllib.request.Request(url=url, headers=headers, data=data)
    try:
        resp = urllib.request.urlopen(req).read()
        print(f"响应数据：{resp.decode('utf-8')}")
        df = json2dataframe(resp.decode('utf-8'))
        return df
    except Exception as e:
        logging.error(e)
        print(e)
