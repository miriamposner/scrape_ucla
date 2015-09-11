from selenium import webdriver

browser = webdriver.Firefox()

type(browser)

browser.get('http://digital2.library.ucla.edu/Search.do?keyWord=&selectedProjects=27&pager.offset=50&viewType=1&maxPageItems=1000')

pageItems = browser.find_elements_by_class_name('searchTitle')
for link in pageItems:
    element.click(link)
    browser.back()
    print("clicked!")
