# Importando as  ferramentas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging

logging.basicConfig(level=logging.INFO, filename="programa.log", format="%(asctime)s - %(levelname)s - %(message)s")

driver = webdriver.Chrome()
driver.get("Tirei a URL para não dar treta :D:D:D")
driver.maximize_window()
actions = ActionChains(driver)


formulario = driver.find_element(By.CSS_SELECTOR, 'input#endereco')

actions.move_to_element(formulario)

formulario.send_keys('Aqui o nome da cidade e UF')
actions.click(formulario)
formulario.send_keys()
formulario.send_keys(Keys.RETURN)
time.sleep(1)
formulario.send_keys('\ue015')
time.sleep(1)
formulario.send_keys(Keys.RETURN)
formulario.send_keys('\ue00f')
actions.perform()

buscar = driver.find_element(By.CLASS_NAME, 'primary-button')
actions.move_to_element(buscar)
actions.click(buscar)
actions.perform()


# Verificando o número de estabelecimentos na pesquisa
estabcount = driver.find_element(By.CLASS_NAME, 'estabcount').text
search_item = int(estabcount) # contagem de estabelecimentos

# Definindo e verificando o número de estabelecimentos na barra de rolagem.
pagination = driver.find_element(By.ID, 'pagination').text
item = pagination.split() # contagem de estabelecimentos na página
last_item = item[-1]
page_item = int(last_item)


nextPage = driver.find_element(By.ID,'nextPage')

# for i in range(search_item):
while page_item < search_item:
    enderecos = driver.find_elements(By.CLASS_NAME, "adress-estab")
    for endereco in list(enderecos):
        end = endereco.text
        logging.info(end)
        print(end) # Exibo o texto da busca
        pagina_atual = driver.window_handles[0]
        driver.switch_to.window(pagina_atual)
    actions.move_to_element(nextPage)
    actions.click(nextPage)
    actions.perform()

time.sleep(2)
driver.close()
