import pandas as pd
import PyPDF2
import re

# open the pdf file
object = PyPDF2.PdfFileReader("/Users/dmitrysklyarov/Folder/Python/_10-K-2020-(As-Filed).pdf")

# get number of pages
NumPages = object.getNumPages()

# define keyterms
String = "Social"

for i in range(0, NumPages):
    PageObj = object.getPage(i)
    print("this is page " + str(i))
    Text = PageObj.extractText()
    # print(Text)
    ResSearch = re.search(String, Text)
    print(ResSearch)