from bs4 import BeautifulSoup
import requests
import sys
import codecs

textContent = []
for x in range(50):
    # true_page = "https://www.politifact.com/factchecks/list/?page=" + str(x) + "&ruling=true"
    false_page = "https://www.politifact.com/factchecks/list/?page=" + str(x) + "&ruling=false"

    # true_code = requests.get(true_page, timeout=20)
    false_code = requests.get(false_page, timeout=20)

    # true_content = BeautifulSoup(true_code.content, "html.parser")
    false_content = BeautifulSoup(false_code.content, "html.parser")

    elems = false_content.select('.m-statement__quote')
    textContent.append(elems)

with codecs.open('false_data.txt', encoding='utf-8', mode='w') as filehandle:
    for listitem in textContent:
        filehandle.write(u'%s\n' % listitem)