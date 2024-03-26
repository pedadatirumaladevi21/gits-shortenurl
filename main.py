# pip install pyshorteners
# pip install pyperclip

import pyshorteners
url=input('enter the url:')
def shortenurl(url):
    S=pyshorteners.Shortener()
    print(S.tinyurl.short(url))

shortenurl(url)

