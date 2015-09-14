from selenium import webdriver

browser = webdriver.Firefox()

type(browser)

browser.get('http://digital2.library.ucla.edu/Search.do?keyWord=&selectedProjects=27&pager.offset=50&viewType=1&maxPageItems=1000')

links = browser.find_elements_by_class_name('searchTitle')
for i in range(len(links)):  
    links = browser.find_elements_by_class_name('searchTitle')
    link = links[i]  # specify the i'th link on the page
    link.click()
    print("clicked!")
    browser.back() 