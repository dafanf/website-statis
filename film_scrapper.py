import os
import json
from urllib import request
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By

DRIVER_PATH = f'{os.getcwd()}/driver/chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
driver = webdriver.Chrome(DRIVER_PATH, options=options)
driver.get('https://m.imdb.com/list/ls063868333/')
driver.maximize_window()
filmlist = []
i=1
now = datetime.now()
while i <= 100:
    for film in driver.find_elements(by=By.CLASS_NAME, value='mode-simple'):
        image = film.find_element(by=By.TAG_NAME, value='img')
        try:
            opener = request.build_opener()
            opener.addheaders = [('User-Agent', 'MyApp/1.0')]
            request.install_opener(opener)
            # request.urlretrieve(image.get_attribute('src'), f'img/{i}.png')
            driver.execute_script(f'window.scrollBy(0, 400)')
            i= i+1
            filmlist.append(
            {   "ranking": film.find_element(by=By.CLASS_NAME, value='unbold').text,
                "title": film.find_elements(by=By.CLASS_NAME, value='h4')[1].text,
                "release_year": film.find_elements(by=By.CLASS_NAME, value='nowrap')[0].text,
                "runtime": film.find_elements(by=By.TAG_NAME, value='span')[8].text,
                "genre":film.find_element(by=By.CLASS_NAME, value='genre').text,
                "image_src": image.get_attribute('src'),
                "scrapping_time" : now.strftime("%Y-%m-%d %H:%M:%S")
            })
            print('url found')
        except TypeError:
            print('url not found')
    # try:
    #     driver.find_element(by=By.CLASS_NAME,value="pagination").find_element_by_partial_link_text(f'{pagination_page+1}').click()
    #     pagination_page= pagination_page+1
    # except NoSuchElementException as e:
    #     break;
with open(f'{os.getcwd()}\JSON\scraper_filmlist.json','w') as file:
    jdumps=json.dumps(filmlist, indent=6)
    file.writelines(jdumps)
driver.quit()