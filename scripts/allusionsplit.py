import re
import os

txtFolder = "../testFiles_split"

for txt in os.listdir(txtFolder):
  txt_path = os.path.join(txtFolder, txt)
  label, ext = os.path.splitext(txt_path)

  if txt.endswith('.txt'):
    with open(txt_path, "r") as f:
      # We get the first line of each line to preserve page numbers
      content = f.readline()
      textFile = f.read()

      # Regular expression to find different format of dates
      pattern = r'((^\[?\d{4}-*\/*\d{0,4}[\.\?]?\]?|^\[?([nac]\.)+\s\d{4}[\.?]?\]?|^\[\d{2}\]\d{2}\.)(\s[?[A-Z]))'

      # We add two lines before entry dates
      splitText = re.sub(pattern, r"\n\1", textFile, flags=re.M)

      # We split the text by dates
      newText = re.split(r"\n?\n\n", splitText)
      # print(newText)

      # Each entry is exported in a new .txt file
      allusionNb = 1
      for allusion in newText[1:]:
        name = label + "_allusion_" + str(allusionNb) + ".txt"
        with open(name, 'w', newline='') as a:
          a.write(content + "\n" + allusion)
        allusionNb = allusionNb + 1
        print(name)