import re
import os

txtFolder = "../pages/vol2-pages/1851-1875"
allusionFolder = "../allusions/vol2-allusions/1851-1875-allusions"

for txt in sorted(os.listdir(txtFolder)):
  txt_path = os.path.join(txtFolder, txt)
  label, ext = os.path.splitext(txt_path)

  if txt.endswith('.txt'):
    with open(txt_path, "r") as f:
      # We get the first line of each line to preserve page numbers
      # content = f.readline()
      textFile = f.read()

      # postString = textFile.split("\n", 2)[2]
      # print(postString)

      # Regular expression to find different format of dates
      pattern = r'((^\[?\d{4}-*\/*\d{0,4}[\.\?]?\]?|^\[?([nac]\.)+\s\d{4}[\.?]?\]?|^\[\d{2}\]\d{2}\.)(\s[?,?[A-Z]))'

      # We add a line before entry dates
      splitText = re.sub(pattern, r"\n\1", textFile, flags=re.M)
      # print(splitText)

      # We split the text by dates
      newText = re.split(r"\n?\n\n", splitText)
      # print(newText)

      # Each entry is exported in a new .txt file
      allusionNb = 1
      for allusion in newText[1:]:
        name = label[30:] + "_a" + str(allusionNb) + ".txt"
        allusionPath = os.path.join(allusionFolder, name)

        with open(allusionPath, 'w', newline='') as a:
          a.write(allusion)
        allusionNb = allusionNb + 1
        print(name)