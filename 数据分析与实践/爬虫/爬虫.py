import requests

url = "https://www.icourse163.org/"

dic = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'}

resp = requests.get(url, headers=dic)

print(resp.text)