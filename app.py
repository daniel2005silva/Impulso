# Importação do modulo time para esperar o carregamento das paginas
import time
# Importação do modulo webdriver para definir qual navegador será utilizado
from selenium import webdriver
# Configuracao para permitir o funcionamento do webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=chrome_options)
# Modulo utilizado para selecionar as tags da pagina 
from bs4 import BeautifulSoup
# Método o site a ser acessado
driver.get("https://dafbnafar-kb.saude.gov.br/s/desenvolvimento/app/kibana#/dashboard/dc5f0570-7f1f-11ea-ae22-c5191b41d130?embed=true&_g=()")
# Método para aguardar o carregamento da pagina
time.sleep(60)
# Atribuindo a variavel o botão na pagina. Método para encontrar o botão dá pagina pelo caminho completo no código
btGrafico = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[3]/dashboard-app/dashboard-viewport-provider/div/div/div[12]/div/div[1]/div/div/div/button")
# Atribuindo a variavel o número total de exames no Brasil Positivo/Detectável
tlBrasil = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[3]/dashboard-app/dashboard-viewport-provider/div/div/div[9]/div/div[2]/div/div/div/div/div/div/div/span")
# Método para fazer o clique no botão armazenado na variavel
btGrafico.click()
# Atribuindo a variavel o caminho do segundo botão para exibir a tabela
btExibirTab = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div/div[2]/button[1]")
# Dando o clique nesse segundo botão encontrado
btExibirTab.click()
# Atribuindo a varival o caminho do botão titulo da tabela para mudar a ordem de itens na tabela para Positivo/Detectável
btMudarDados = driver.find_element_by_xpath("/html/body/div[4]/span/div/div/div[2]/div[3]/div[1]/table/thead/tr/th[2]/button")
# Dando o clique para mudar a ordem de itens na tabela
btMudarDados.click()
# Dando o segundo clique para deixar a tabela na ordem preterida
btMudarDados.click()
# Atribuindo a variavel o caminho da tabela
dados = driver.find_element_by_xpath("/html/body/div[4]/span/div/div/div[2]/div[3]/div[1]/table")
# Atribuindo a variavel o codigo HTML da tabela 
html = dados.get_attribute("outerHTML")
# Atribuindo a variavel o codigo HTML do número total de exames Positivo/Detectável no Brasil
totalBr = tlBrasil.get_attribute("outerHTML")
# Método para converter o código
soup = BeautifulSoup(html, "html.parser")
# Atribuindo a variavel o código convertido em HTML
posDetBr = BeautifulSoup(totalBr, "html.parser")
# Atribuindo a variavel a tabela
tabela = soup.find(name='table')
# Selecionando todos th dentro da tabela
#th = tabela.find_all('span', class_ = 'euiTableCellContent__text')

# Declarações de vetores
conteudo = []
estados = []
status = []
tlExames = []
#titulo = []
#icremento = 0
#for i in th:
  #print(i.next_element)
  #titulo.append(i.next_element)
  #icremento+= 1

# Atribuindo a variavel uma lista de td da tabela
td = tabela.find_all('div', class_ = 'euiFlexItem euiFlexItem--flexGrowZero')
# Método for para percorrer todos os td encontrados
for c in td:
  #print(c.text)

  # Armazenando no vetor um item por vez, convertido para texto
  conteudo.append(c.text)

# Declarações de variaveis auxiliares para ajudar na obtenção dos itens desejados
aux = 0
aux1 = 0
aux2 = 3
aux3 = 6

#print(conteudo)
# Por haver tds em branco, e seguir o mesmo padrão de localização, lógica para ao percorrer a lista de td, separar quem é 
# o estado, o resultado e o total
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
# Método para percorrer os estados
for w in estados:
  print(w + ":")
  # tlExames armazenou o total de exames de cada estado
  print("Total de exames: " + tlExames[aux])
  # str converte para string, round arredonda para duas casa decimais, float converte a string em número
  print(str(round((float(tlExames[aux]) / float(posDetBr.text) * 100), 2)) + "%")
  print("--------------------------------------------------------------")
  aux += 1

'''

print(titulo[0])
print(titulo[1])
print(titulo[2])'''