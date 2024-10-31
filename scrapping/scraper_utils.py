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
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--headless")  # Modo sin cabeza
    option.add_argument("--disable-gpu")
    option.add_argument("windows-size=1920,1080")
    driver = Chrome(service=service, options=option)

    return driver

def get_news_articles():

    # Inicializa el driver
    driver = initialize_driver()
    
    # Visita la página de noticias
    driver.get("https://www.forbes.com/news/")
    time.sleep(5)  # Espera para que la página cargue completamente
    

    articles_elements = driver.find_elements(By.CSS_SELECTOR, '._4g0BEaLU')
    

    # Extrae los datos de cada artículo
    news_data = []

    for article in articles_elements:
        try:
            title = article.find_element(By.CSS_SELECTOR, '._1-FLFW4R') 
            date = article.find_element(By.CSS_SELECTOR, '.IE8ecQMQ')
            description = article.find_element(By.CSS_SELECTOR, '.Ccg9Ib-7')

            # print("TITLE ARTICLE", title.text)
            print("DESCRIPTION ARTICLE", description.text)
            # print(article.get_attribute('outerHTML'))

            news_data.append({
                "title": title.text,
                "date": date.text,
                "description": description.text,
            })
        except Exception as e:
            print(f"Error al procesar el artículo: {e}")
    
    # Cierra el navegador
    driver.quit()

    return news_data