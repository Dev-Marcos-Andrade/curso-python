import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.facebook.com')
except urllib.error.URLError:
    print('O site não está acessível no momento.')
else:
    print('Consegui acessa o site com sucesso!')