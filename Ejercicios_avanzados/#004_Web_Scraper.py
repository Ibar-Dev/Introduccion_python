import requests
from bs4 import BeautifulSoup

def web_scraper(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Implementa lógica para extraer información de la página utilizando BeautifulSoup
            # Por ejemplo, encontrar todos los elementos <a> y mostrar sus textos
            links = soup.find_all('a')
            for link in links:
                print(link.text)
        else:
            print("Error al obtener la página:", response.status_code)
    except Exception as e:
        print("Error:", e)

# Ejemplo de uso:
url = 'https://example.com'
web_scraper(url)


# Instalar requests:
# requests es una biblioteca de Python que facilita la realización de solicitudes HTTP. 
# Puedes instalarlo utilizando pip, el administrador de paquetes de Python. 
# Abre tu terminal o línea de comandos y ejecuta el siguiente comando:

# En la terminal:
# pip install requests



# Instalar BeautifulSoup:
# BeautifulSoup es una biblioteca de Python para extraer datos de archivos HTML y XML. 
# También puedes instalarlo utilizando pip. Ejecuta este comando en tu terminal o línea de comandos:

# En la terminal:
# pip install beautifulsoup4