# O modulo time aqui foi utilizado para esperar o carregamento das paginas atraves do firefox
import time

import pandas as pd
# o modulo webdriver e necessario para definir qual navegador sera utilizado para fazer a automacao
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=chrome_options)
# o modulo Select sera utilizado para interagir com a caixa de selecao onde sera definido o ano em que quero buscar os dados
from selenium.webdriver.support.ui import Select

# esse modulo sera utilizado para 
from bs4 import BeautifulSoup

# a linha abaixo define qual e o navegador que queremos utilizar, lembrando que eu instalei somente o driver para conexao com o firefox, mas existem tambem para Chrome e InternetExplorer
#driver = webdriver.Chrome()

# abaixo foi definido qual e o site que quero acessar
driver.get("https://dafbnafar-kb.saude.gov.br/s/desenvolvimento/app/kibana#/dashboard/dc5f0570-7f1f-11ea-ae22-c5191b41d130?embed=true&_g=()")

#print(driver.page_source.encode('utf-8'))
# o Sleep abaixo e para aguardar o carregamento da pagina
time.sleep(60)

# Aqui estou buscando o elemento que possui na classe o valor valo01, que e respectivo ao valor da receita onde quero clicar para ir na proxima pagina
btGrafico = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[3]/dashboard-app/dashboard-viewport-provider/div/div/div[12]/div/div[1]/div/div/div/button")

#print(receita)
tlBrasil = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[3]/dashboard-app/dashboard-viewport-provider/div/div/div[9]/div/div[2]/div/div/div/div/div/div/div/span")
# aqui e feito um clique no elemento que foi encontrado acima
btGrafico.click()

# aguardando o carregamento da pagina
#time.sleep(60)

btExibirTab = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div/div[2]/button[1]")
#print(btExibirTab)

btExibirTab.click()

#time.sleep(30)

btMudarDados = driver.find_element_by_xpath("/html/body/div[4]/span/div/div/div[2]/div[3]/div[1]/table/thead/tr/th[2]/button")

#print(btMudarDados)

btMudarDados.click()

#time.sleep(60)

btMudarDados.click()

#time.sleep(60)
# armazenando a div que possui a tabela dentro da variavel dados
dados = driver.find_element_by_xpath("/html/body/div[4]/span/div/div/div[2]/div[3]/div[1]/table")

# aqui e pegado o codigo HTML que esta dentro da div bd01 no codigo que foi mostrado acima
html = dados.get_attribute("outerHTML")
totalBr = tlBrasil.get_attribute("outerHTML")
# com o codigo HTML dentro da variavel, vamos usar o BeautifulSoup para fazer o parser desse HTML
soup = BeautifulSoup(html, "html.parser")
posDetBr = BeautifulSoup(totalBr, "html.parser")
# dentro da variavel soup temos o codigo html retornado pelo Selenium ja convertido para o BS
 # vou utilizar o metodo select_one para buscar o elemento table dentro desse codigo
#table = soup.select_one("table")
tabela = soup.find(name='table')
th = tabela.find_all('span', class_ = 'euiTableCellContent__text')

conteudo = []
estados = []
status = []
tlExames = []
titulo = []
#icremento = 0
#for i in th:
  #print(i.next_element)
  #titulo.append(i.next_element)
  #icremento+= 1

td = tabela.find_all('div', class_ = 'euiFlexItem euiFlexItem--flexGrowZero')


for c in td:
  #print(c.text)
  conteudo.append(c.text)

aux = 0
aux1 = 0
aux2 = 3
aux3 = 6

#print(conteudo)

for y in conteudo:
  if(aux == aux1):
    estados.append(y)
    aux1 = aux1 + 8
  
  if(aux == aux2):
    status.append(y)
    aux2 = aux2 + 8

  if(aux == aux3):
    tlExames.append(y)
    aux3 = aux3 + 8

  aux = aux + 1
  #print(y)

#print(estados)
#print('==================')
#print(status)
#print('==================')
#print(tlExames)
#print('==================')
#print(posDetBr)

print("PERCENTUAL DE RESULTADOS POSITIVO/DETECTÁVEL POR ESTADOS")
print("==============================================================")
print("Total de resultados Positivo/Detectável no Brasil " + posDetBr.text)
print("--------------------------------------------------------------")
aux = 0
for w in estados:
  print(w + ":")
  print("Total de exames: " + tlExames[aux])
  print(str(round((float(tlExames[aux]) / float(posDetBr.text) * 100), 2)) + "%")
  print("--------------------------------------------------------------")
  aux += 1

'''
df_full = pd.read_html(str(tabela))
df = df_full[['UF de residência', 'Resultados', 'Nº de exames realizados']]
df.columns = ['Estado', 'Situação', 'Total de exames']

print(titulo[0])
print(titulo[1])
print(titulo[2])'''