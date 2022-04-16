import time
from selenium import webdriver
from bs4 import BeautifulSoup


from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


def get_movies():
    url = "https://www.binged.com/streaming-premiere-dates/?language[]=Malayalam"
  
    # initiating the webdriver. Parameter includes the path of the webdriver.
    op=Options()
    op.add_argument('--headless')
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=op)
    driver.get(url) 
    
    # this is just to ensure that the page is loaded
    time.sleep(5) 
    
    html = driver.page_source
    
    # this renders the JS code and stores all
    # of the information in static HTML code.
    
    # Now, we could simply apply bs4 to html variable
    soup = BeautifulSoup(html, "html.parser")

    tables=soup.find_all('tr')

    movies=[]

    for i in tables[1:]:
        movie={}
        movie['name']=i.find_all('a')[1].text
        movie['image']=i.find_all('a')[0].find('img').get('data-src')
        movie['genre']=i.find(class_="col-genre desktop").text
        movie['language']=i.find(class_="col-languages desktop").text
        movie['platforms']=i.find(class_="col-platform desktop").text
        movie['date']=i.find(class_="col-date desktop").text
        movies.append(movie)
    driver.close()
    return movies


if __name__=="__main__":
    print(get_movies())