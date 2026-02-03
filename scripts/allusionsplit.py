import re
import os

txtFolder = "/content"

for txt in os.listdir(txtFolder):
  txt_path = os.path.join(txtFolder, txt)
  label, ext = os.path.splitext(txt_path)
  if txt.endswith('.txt'):
    with open(txt_path, "r") as f:
      content = f.readline()
      # print(content)

      textFile = f.read()

      pattern = r'(^[0-9]{4}(\-[0-9]{1,4})*\.\s[A-Z]*\[*|^\[*[0-9]{4}(\-*\/*[0-9]{1,4})*\.*\?*\]*\s[A-Z]\[*|^\[[ac\. ]*[0-9]{4}(\-*\/*[0-9]{1,4})*\.*\?*\]*\s[A-Z]\[*)'
      # pattern = r'(^"*\s*\[*([0-9]{4})*\]*\.*,*\]* *([A-Z]*[July|Oct.]{3})* \d*)'
      splitText = re.sub(pattern, r"\n\n\1", textFile, flags=re.M)
      newText = re.split(r"\n?\n\n", splitText)
      # print(newText)

      allusionNb = 1
      for allusion in newText[1:]:
        name = label + "_allusion_" + str(allusionNb) + ".txt"
        with open(name, 'w', newline='') as a:
          a.write(content + "\n" + allusion)
        allusionNb = allusionNb + 1
        print(name)