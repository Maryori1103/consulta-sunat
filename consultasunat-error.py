from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

#iniciar el driver
driver = webdriver.Chrome()

#Maximizar el navegador
driver.maximize_window()

#URL de la web
url = 'https://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/FrameCriterioBusquedaWeb.jsp'

# Abre la web
driver.get(url)

# Esperar unos segundos para que cargue la página
time.sleep(3)

#busqueda por ruc
RUC = driver.find_element(By.ID,'txtRuc').send_keys('20604560ABC')
    
time.sleep(1)

buscar = driver.find_element(By.ID,'btnAceptar').click()

# Esperar unos segundos para que cargue la respuesta
time.sleep(5)


# Cerrar el navegador
driver.quit()
