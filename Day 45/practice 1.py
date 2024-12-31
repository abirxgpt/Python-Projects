from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup)
# prints whole HTML code

# print(soup.prettify())
# pretty the code and turn indents in it at the time

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# first print the whole title line
# second print the whole title name such as "title" itself
# third print the string or name of the website we've given it

# print(soup.p)
# print(soup.a)
# print(soup.br)
# print(soup.h1)
#
# these all print the particular things but only the first one we find in it

