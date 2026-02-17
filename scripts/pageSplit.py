import os
import re

file = "../15e-allusions.txt"
folder = "../pages"
pagePattern = r'^-{15}\s.*-{15}$'

with open(file, "r") as f:
    textFile = f.read()
    # print(textFile)
    splitText = re.split(pagePattern, textFile, flags=re.M)

    pageNb = 14
    for text in splitText[1:]:
        name = "vol1_p" + str(pageNb) + ".txt"
        print(name)

        file_path = os.path.join(folder, name)
        with open(file_path, 'w', newline='') as a:
          a.write(text)
        pageNb += 1
