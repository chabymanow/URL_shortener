import pyshorteners

link = input("Plese enter your URL: ")

short = pyshorteners.Shortener()
shortLink = short.tinyurl.short(link)

print(f"Your short link is: {shortLink}")