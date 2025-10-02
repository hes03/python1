import requests
import os

path = os.getcwd()+'/data'
if not os.path.exists(path):
    os.makedirs(path)

name = input('이름>')

url = f'https://www.google.com/search?sca_esv=5d812c3a7137edf1&sxsrf=AE3TifMeFQSIU8KeRJ2Kb-7OnzMzFHJ6zA:1756773518709&udm=2&fbs=AIIjpHyDg0Pef0CibV20xjIa-FReIKmAxsMTxuQCKLhb9OUJki0DxYQJ2cWp-4Nzr6A22Hd6jjCiXj3pHtJL4GF4IdmcOPhtuymirNki6M4-FI6ZoETbBnaaxo8y1CZ3qaFm0ocB70ZM-0EjlhzTyMEuwmDb2fXngn38DqwxdyrTIyH6ZW9irjsPl9lNb-UK7Wtb5_h_jKKWUjWJJuX24DJ8kcXyxw90psx5yxwsuoeMI4TXlPcu3dU&q={name}&sa=X&sqi=2&ved=2ahUKEwiNiqKs67iPAxVahlYBHRRVOhgQtKgLegQIGxAB&biw=844&bih=710&dpr=1.25'
res = requests.get(url)


file_name = f'data/{name}.html'
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(res.text)


