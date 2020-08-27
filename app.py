import requests
from bs4 import BeautifulSoup
from time import sleep
url = "http://plataforma.saude.gov.br/coronavirus/virus-respiratorios/"

req = requests.get(url)

res = BeautifulSoup(req.content,'html.parser')
#sleep(10)
#element2 = res.find('div', {"class": "container-fluid"})
element = res.find('euiTable euiTable--compressed euiTable--responsive')
#ele = element.find('#document')
print(element)
for item in element:
  print("========================")
  print(item)