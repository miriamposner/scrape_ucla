Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
pip3 install selenium
SyntaxError: invalid syntax
>>> install selenium
SyntaxError: invalid syntax
>>> import selenium
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import selenium
  File "/Users/miriamposner/Documents/selenium.py", line 1, in <module>
    from selenium import webdriver
ImportError: cannot import name 'webdriver'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/miriamposner/Documents/selenium_scrape.py", line 3, in <module>
    browser.get('http://digital2.library.ucla.edu/Search.do?keyWord=&selectedProjects=27&pager.offset=50&viewType=1&maxPageItems=1000')
NameError: name 'browser' is not defined
>>> from selenium import webdriver
>>> browser.get('www.google.com')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    browser.get('www.google.com')
NameError: name 'browser' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/miriamposner/Documents/selenium_scrape.py", line 9, in <module>
    pageItem = driver.find_elements_by_class_name('searchTitle')
NameError: name 'driver' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/miriamposner/Documents/selenium_scrape.py", line 9, in <module>
    pageItems = driver.find_elements_by_class_name('searchTitle')
NameError: name 'driver' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/miriamposner/Documents/selenium_scrape.py", line 11, in <module>
    element.click(link)
NameError: name 'element' is not defined
>>> ================================ RESTART ================================
>>> 
Found <a> element with that class name!
>>> ================================ RESTART ================================
>>> 
Found <a> element with that class name!
Traceback (most recent call last):
  File "/Users/miriamposner/Documents/trypageitem.py", line 15, in <module>
    for link in elem:
TypeError: 'WebElement' object is not iterable
>>> ================================ RESTART ================================
>>> 
Found <a> element with that class name!
clicked!
>>> ================================ RESTART ================================
>>> 
Found <a> element with that class name!
clicked!
>>> 
