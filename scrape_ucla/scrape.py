#!/usr/bin/env python3

import bs4, requests, os

url = 'http://digital2.library.ucla.edu/viewItem.do?ark=21198/zz0002ksb2'
os.makedirs('aids_posters', exist_ok=True)
while not url.endswith('#'):
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

print('Done.')
