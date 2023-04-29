import pyshorteners

def short_url(url):
    shortener=pyshorteners.Shortener()
    a=shortener.tinyurl.short(url)
    return a

url_data="https://stackoverflow.com/questions/65348890/python-was-not-found-run-without-arguments-to-install-from-the-microsoft-store"
print(short_url(url_data))