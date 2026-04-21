import csv
import os

file = "../biography/episodes/education.txt"
folder = "../pages/vol3-pages/index/biography"
infoList = []

for subdir, dirs, files in os.walk(folder):
    for file in files:
        if not file.endswith(".DS_Store"):
            path = os.path.join(subdir, file)
            print(path)

            with open(path, "r") as f:
                mainCat = path.split("/")[-3]
                subCat = path.split("/")[-2]
                subSubCat = path.split("/")[-1]

                textFile = f.read()
                cleanedTextFile = textFile.replace("\n", " ")

                entryLines = cleanedTextFile.split(";")
                for entry in entryLines:
                    entryInfo = entry.split(",")
                    print(entryInfo)

                    authorName = entryInfo[0]
                    date = entryInfo[1]
                    pageInfo = entryInfo[2].split(" ")

                    infoList.append([mainCat, subCat, subSubCat[:-4], authorName, date, pageInfo[1][:-1].upper(), pageInfo[2]])

            # print(infoList[1])


            '''if subSubCat != "":
                csv_name = subSubCat[:-4] + '.csv'
            else:
                csv_name = subCat[:-4] + '.csv'''

fields = ['main_category', 'subcategory', 'sub_subcategory', 'author_name', 'date', 'volume', 'page']
with open('biography.csv', 'w', newline='') as c:
    writer = csv.writer(c)
    writer.writerow(fields)
    writer.writerows(infoList)
