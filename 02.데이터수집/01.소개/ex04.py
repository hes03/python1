import requests

url = 'https://ssl.pstatic.net/melona/libs/1544/1544463/73bd6aabb4a3c4762782_20250829120611648.jpg'
res = requests.get(url)

file_name = 'data/naver.jpg'
with open(file_name, 'wb') as file:
    file.write(res.content)
    