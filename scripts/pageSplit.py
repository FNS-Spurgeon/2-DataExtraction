import os
import re

file = "../../1-Transcription/vol2/1801-1825-allusions.txt"  # Txt file exported from eScriptorium (Batch of pages)
folder = "../pages"

pagePattern = r'^-{15}\s.*-{15}$'

with open(file, "r") as f:
    textFile = f.read()

    # We split the text by pages
    splitText = re.split(pagePattern, textFile, flags=re.M)

    pageNb = 1 # Number of the first page of the batch
    for text in splitText[1:]:
        name = "part2_p" + str(pageNb) + ".txt"
        print(name)

        file_path = os.path.join(folder, name)
        with open(file_path, 'w', newline='') as a:
          a.write(text)
        pageNb += 1
