import re

file = "../export_doc1457_testocr_text_20260209101932.txt"
pagePattern = r'^-{15}\s.*-{15}$'

with open(file, "r") as f:
    textFile = f.read()
    # print(textFile)
    splitText = re.split(pagePattern, textFile, flags=re.M)

    pageNb = 67
    for text in splitText[1:]:
        name = "volume1_page" + str(pageNb) + ".txt"
        with open(name, 'w', newline='') as a:
          a.write(text)
        pageNb += 1
