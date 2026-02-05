import re
import os
import csv

txtFolder = "../testFiles_extraction"

dateRegEx = r'\n(^\[?\d{4}-*\/*\d{0,4}[\.\?]?\]?|^\[?([nac]\.)+\s\d{4}[\.?]?\]?|^\[\d{2}\]\d{2}\.)(\s[?[A-Z])'
authorRegEx = r"\d\.*[\.\]]\s(Unknown\.|[A-Z]\.*,*\s*[A-Z]*\.|\[?(D')?(De\s)?([A-Z]?[a-z]+-)?([A-Z][a-z]+)(,\s)\[*([A-Z][a-z]+\s)*([A-Z][a-z]+)(,\s)*(of|de)*\s*([A-Z][a-z]+)*(\sof|de)*(\s[A-Z][a-z]+)*\(?\??\)?\.?\]?)|([A-Z]\[?[a-z]*\]?),\s([A-Z]\[?[a-z]*\]?)\."
titleRegEx = r"([Ii]m[Pp]r[iy]nted|[Pp]rinted|Unique|, dated|[Ww]ritten|\[?\bin\b\]?|\b[Bb]ook\b|MS[S]?\.|\[?\b[cfv]ol\b|sign\.|\[?\bto\b|\b[pf]p?\b\.)"

allusionsList = []

for txt in os.listdir(txtFolder):
  print(txt)
  txt_path = os.path.join(txtFolder, txt)
  label, ext = os.path.splitext(txt_path)

  if txt_path.endswith('.txt'):
    with open(txt_path, "r") as f:
      txtFile = f.read()
      # print(txtFile)

      volume = "Vol.2"

      pageNb_head = re.search(r'^\d*\s|\s\d*$', txtFile, flags=re.M)
      pageNb = re.split(r'\s', pageNb_head.group())
      pageNb_clean = "".join(pageNb)
      # print(pageNb_clean)

      date = re.search(dateRegEx, txtFile, flags=re.M).group(1)
      # print(date)

      author = re.search(authorRegEx, txtFile, flags=re.M).group(1)
      # print(author)

      text = re.split(authorRegEx, txtFile)
      # print(text[-1])

      title = re.split(titleRegEx, text[-1], 1)
      title_clean = re.sub(r'^\s', '', title[0])
      # print(title[0])

      remainingText = ''.join(title[1:])

      allusionsList.append([volume, pageNb_clean, date, author, title_clean, remainingText])

print(allusionsList)
fields = ['Volume', 'Page', 'Date', 'Author', 'Title','Quotation']

with open('allusionsListTest8.csv', 'w', newline='') as c:
    writer = csv.writer(c)
    writer.writerow(fields)
    writer.writerows(allusionsList)