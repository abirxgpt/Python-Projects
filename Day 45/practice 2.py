from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# now we use findall attribute to use it as if we want to select all of the classes or ids or other things from the HTML file

all_anchour_tags = soup.find_all(name="a")
# print(all_anchour_tags)
# this will print all anchor tags in a List format

# for i in all_anchour_tags:
    # print(i.getText())
    # this will print all of the text inside the anchor tags

    # print(i.get("href"))
    # this will print or extract any element from that particular list for example href in this case

# heading = soup.find(name="h1", id="jack")
# print(heading.string)
# this will help in finding even the id of the following project we seem to find or we want to find
# basically helping in narrowing our subjects

# section_name = soup.find(name="h3", class_="heading")
# print(section_name)
# the class only works when we use the "class_" with this cause class is already a given function of the python language

# using_css_selectors = soup.select_one(selector="p a")
# print(using_css_selectors)
# this helps us in selecting a particular attribute using css selectors to narrow down our search

# we can also use it as a selection in different ids or classes as we do in css:
# sections = soup.select(selector="#name")
# # print(sections)
# #
# # headings = soup.select(selector=".heading")
# # print(headings)