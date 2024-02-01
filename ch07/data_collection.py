import requests
import pandas as pd
from dotenv import load_dotenv
import os

# .env 파일이 활성화
load_dotenv()

SERVICE_KEY = os.getenv('SEOUL_API_KEY')
print(SERVICE_KEY)








# data = None
# for j in range(1,5):
#     url = f'http://openapi.seoul.go.kr:8088/{SERVICE_KEY}/json/tbLnOpendataRtmsV/{1+((j-1)*1000)}/{j*1000}'
#     print(url)
#     req = requests.get(url)
#     content = req.json()
#     con = content['tbLnOpendataRtmsV']['row']
#     result = pd.DataFrame(con)
#     data = pd.concat([data, result])
# data = data.reset_index(drop=True)
