import re
import os
import csv

txtFolder = "../allusions/vol2-allusions/1876-1900-allusions"

# Regular expressions
dateRegEx = r'(^\[?\d{4}-*\/*\d{0,4}[\.\?]?\]?\.?|^\[?([nac]\.)+\s\d{4}-?(\d{1,2})?[\.?]?\]?\.?|^\[\d{2}\]\d{2}\.)(\s[?[A-Z])'
authorRegEx = r"\d\??\.?\]?\.?\s(Unknown\.|[A-Z]\.*,*\s*[A-Z]*\.|\[?(D')?(De\s)?([A-Z]?[a-z]+-)?([A-Z][a-z]+)(,\s)\[*([A-Z][a-z]+\s)*([A-Z][a-z]+)(,\s)*(of|de)*\s*([A-Z][a-z]+)*(\sof|de)*(\s[A-Z][a-z]+)*\(?\??\)?\.?\]?)|([A-Z]\[?[a-z]*\]?),\s([A-Z]\[?[a-z]*\]?)\."
# authorFrRegex = r"\d\??\.?\]?\.?\s(Unknown\.|[A-ZÉÈ]\.*,*\s*[A-ZÉÈ]*\.|\[?(D')?(De\s)?([A-ZÉÈ]?[a-zéèéë]+-)?([A-ZÉÈ][a-zéèé]+)(,\s)\[*([A-ZÉÈ][a-zéèé]+\s)*([A-ZÉÈ][a-zéèé]+)(,\s)*(of|de)*\s*([A-ZÉÈ][a-zéèé]+)*(\sof|de)*(\s[A-ZÉÈ][a-zéèé]+)*\(?\??\)?\.?\]?)|([A-ZÉÈ]\[?[a-zéèé]*\]?),\s([A-ZÉÈ]\[?[a-zéèé]*\]?)\."
titleRegEx = r"([Ii]m[Pp]r[iy]nted|[Pp]rinted|Unique|, dated|[Ww]ritten|\[?\bin\b\]?|\b[Bb]ook\b|MS[S]?\.|\[?\b[cfv]ol\b|sign\.|\[?\bto\b|\b[pf]p?\b\.)"

allusionsList = []

for txt in sorted(os.listdir(txtFolder)):
  # print(txt)
  txt_path = os.path.join(txtFolder, txt)
  label, ext = os.path.splitext(txt_path)
  print(label)

  if txt_path.endswith('.txt'):
    with open(txt_path, "r") as f:
      txtFile = f.read()
      # print(txtFile)

      ID = re.split(r'/', label)[-1]
      volume = "Vol.2"
      part = "part III"
      page = re.split(r'_', ID)[1]

      # pageNb_head = re.search(r'^\d*\s|\s\d*$', txtFile, flags=re.M)
      # pageNb = re.split(r'\s', pageNb_head.group())
      # pageNb_clean = "".join(pageNb)
      # print(pageNb_clean)

      date = re.search(dateRegEx, txtFile, flags=re.M).group(1)
      # print(date)

      if re.search(authorRegEx, txtFile, flags=re.M).group(1):
        author = re.search(authorRegEx, txtFile, flags=re.M).group(1)
      else:
        author = "N/A"
      # print(author)

      # We get the text after the author's name
      text = re.split(authorRegEx, txtFile, maxsplit=1, flags=re.M)
      newText = [t for t in text if t is not None]
      # print(newText[-1])

      # We get the title
      title = re.split(titleRegEx, newText[-1], 1)
      title_clean = re.sub(r'^\s', '', title[0])
      # print(title[0])

      # The remaining text is kept as it is
      remainingText = ''.join(title[1:])

      allusionsList.append([ID, volume, part, page, date, author, title_clean, remainingText])

print(allusionsList)

# We create a CSV file from the list
fields = ['ID', 'Volume', 'Part','Page', 'Date', 'Author', 'Title','Quotation']
with open('vol2-1876-1900-allusions.csv', 'w', newline='') as c:
    writer = csv.writer(c)
    writer.writerow(fields)
    writer.writerows(allusionsList)
