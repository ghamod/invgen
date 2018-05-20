#!/usr/bin/python3

import sys
import re
import locale
# Debian package is python3-bs4
from bs4 import BeautifulSoup

# Debian package is python3-pandas
import pandas

from html.parser import HTMLParser
from reportlab.platypus import tables

#Open html file and read contents
file_name = sys.argv[1]
fp = open(file_name)
contents = fp.read()

#Parse contents
soup = BeautifulSoup(contents, 'html.parser')

invoiceNumber = re.findall(r'\d+', soup.find('h3').string)

invoiceNumber = int(invoiceNumber[0])

print(invoiceNumber)

Tables = pandas.read_html(contents)

invoiceTable = Tables[3]

invoiceTable.to_csv('table {}.csv'.format(3))


#print(Tables[3])
