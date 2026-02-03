import re
import os
import csv

txtFolder = "../testFiles"

dateRegEx = r'(^[0-9]{4}(\-[0-9]{1,4})*\.\s[A-Z]*\[*|^\[*[0-9]{4}(\-*\/*[0-9]{1,4})*\.*\?*\]*\s[A-Z]\[*|^\[[ac\. ]*[0-9]{4}(\-*\/*[0-9]{1,4})*\.*\?*\]*\s[A-Z]\[*)'
authorRegEx = r"\d\.*[\.\]]\s(Unknown\.|[A-Z]\.,*\s*[A-Z]*\.*|\[*(D')*(De\s)*([A-Z][a-z]+-)*([A-Z][a-z]+)(,\s)\[*([A-Z][a-z]+\s)*([A-Z][a-z]+)(,\s)*(of|de)*\s*([A-Z][a-z]+)*(\sof|de)*(\s[A-Z][a-z]+)*\(*\?*\)*\.*\]*)"

allusionsList = []

for txt in os.listdir(txtFolder):
  print(txt)
  txt_path = os.path.join(txtFolder, txt)
  label, ext = os.path.splitext(txt_path)
  # print(label)

  if txt_path.endswith('.txt'):
    with open(txt_path, "r") as f:
      txtFile = f.read()
      # print(txtFile)

      volume = "Vol.2"

      pageNb_head = re.search(r'^\d+\s|\d+\sCha', txtFile, flags=re.M)
      pageNb = re.split(r'\s', pageNb_head.group())[0]

      # print(pageNb)

      date = re.search(dateRegEx,
                      txtFile, flags=re.M).group()

      # print(date[:-2])

      author = re.search(authorRegEx, txtFile, flags=re.M).group(1)
      # print(author)

      text = re.split(authorRegEx, txtFile)
      # print(text[-1])

      title = re.split(r'([Ii]m[Pp]r[iy]nted|[Pp]rinted|Unique|, dated|[Ww]ritten|\[?\bin\b\]?|\b[Bb]ook\b|MS[S]?\.|\[?\b[cf]ol\b|sign\.|\[?\bto\b|\bp[p]?\b\.)', text[-1], 1)
      # print(title)

      remainingText = ''.join(title[1:])

      allusionsList.append([volume, pageNb, date[:-2], author, title[0], remainingText])

print(allusionsList)
'''fields = ['Volume', 'Page', 'Date', 'Author', 'Title','Text']

with open('allusionsListTest5.csv', 'w', newline='') as c:
    writer = csv.writer(c)
    writer.writerow(fields)
    writer.writerows(allusionsList)'''