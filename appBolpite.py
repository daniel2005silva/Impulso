 
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
driver.get("http://www.bolpite.com.br/")
# Método para aguardar o carregamento da pagina
time.sleep(60)

# Atribuindo a variavel o caminho da tabela
dados = driver.find_element_by_xpath("/html/body/div/div/table")
# Atribuindo a variavel o codigo HTML da tabela 
html = dados.get_attribute("outerHTML")


# Método para converter o código
soup = BeautifulSoup(html, "html.parser")

# Atribuindo a variavel a tabela
tabela = soup.find(name='table')
# Selecionando todos th dentro da tabela
celulas = tabela.find_all('td')
# Declarações de vetores
pos = []
bolp = []
pts = []

auxPos = 0
auxBolp = 1
auxPts = 2

contador = 0
# Método for para percorrer todos os td encontrados
for c in celulas:
  
  if contador == auxPos:
    pos.append(c.text)
  elif contador == auxBolp:
    bolp.append(c.text)
  elif contador == auxPts:
    pts.append(c.text)

    auxPos = auxPos + 3
    auxBolp = auxBolp + 3
    auxPts = auxPts + 3 

  contador = contador + 1
  
contador = 0

print('CLASSIFICAÇÃO DOS BOLPITEIROS')

for b in bolp:
  
  print(b + ' tem ' + pts[contador] + ' pontos.')
  

  contador = contador + 1


#print(conteudo)