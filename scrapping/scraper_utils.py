from selenium import webdriver
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def initialize_driver():
    # Configura el driver de Selenium
    service = Service(ChromeDriverManager().install())
    option= webdriver.ChromeOptions()
    # option.add_argument("--headless")
    option.add_argument("windows-size=1920,1080")
    driver = Chrome(service=service, options=option)

    return driver

def get_news_articles():

    # Inicializa el driver
    driver = initialize_driver()
    
    # Visita la página de noticias
    driver.get("https://elpais.com/america/economia/")
    time.sleep(5)  # Espera para que la página cargue completamente
    
    # Encuentra los artículos en la página
    articles_elements = driver.find_elements(By.CSS_SELECTOR, "h2.c_t a")

    # Extrae los datos de cada artículo
    news_data = []
    for article in articles_elements:
        try:
            title = article.text
            url = article.get_attribute("href")

            # Extraer la fecha usando el siguiente selector CSS
            date_element = driver.find_element(By.CSS_SELECTOR, "span.c_a_t time#sc_date")
            date = date_element.text
            
            # Extraer la descripción (puedes cambiar el selector si necesitas más contexto)
            description_element = driver.find_element(By.CSS_SELECTOR, "p.c_d")
            description = description_element.text
            
            news_data.append({
                "title": title,
                "date": date,
                "description": description,
                "url": url
            })
        except Exception as e:
            print(f"Error al procesar el artículo: {e}")
    
    # Cierra el navegador
    driver.quit()

    return news_data