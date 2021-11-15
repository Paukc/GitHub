from selenium import webdriver
import time
#  import pandas as pd

driver = webdriver.Chrome('./chromedriver.exe')
web = 'https://www.starz.com/ar/es/view-all/blocks/1402530'
driver.get(web)
time.sleep(3)

"""boton_az = driver.find_element('//@class_="active"De la A a la Z')
boton_az.click()"""

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(10)

peliculas = driver.find_elements_by_xpath('.//h3[@class_="title text-center on-hover"]')

movies = []
for pelicula in peliculas:
    movies.append(pelicula)

print(movies)
