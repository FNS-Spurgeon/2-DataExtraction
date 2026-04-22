import csv
import os

folder = "../index/index-txt/criticism"
infoList = []

for subdir, dirs, files in os.walk(folder):  # We parse the directories
    for file in files:
        if not file.endswith(".DS_Store"):
            path = os.path.join(subdir, file)  # Path to the file
            print(path)

            with open(path, "r") as f:
                mainCat = path.split("/")[-3]  # Main category (First level of the index)
                subCat = path.split("/")[-2]  # Subcategory (Second level of the index)
                subSubCat = path.split("/")[-1]  # Sub-subcategory (Third level of the index)

                textFile = f.read()
                cleanedTextFile = textFile.replace("\n", " ")

                entryLines = cleanedTextFile.split(";")  # We split the text to get each entry
                for entry in entryLines:
                    entryInfo = entry.split(",")  # We split the text to get portion of information
                    print(entryInfo)

                    # From the split information, we get the author[0], the date[1], the volume and the vol/page[2]
                    authorName = entryInfo[0]
                    date = entryInfo[1]
                    pageInfo = entryInfo[2].split(" ")

                    # All the information are stored in a list
                    infoList.append(
                        [mainCat, subCat, subSubCat[:-4], authorName, date, pageInfo[1][:-1].upper(), pageInfo[-1]])

            # print(infoList[1])

# The list is transformed into a CSV file corresponding to the main category
fields = ['main_category', 'subcategory', 'sub_subcategory', 'author_name', 'date', 'volume', 'page']
with open('criticism.csv', 'w', newline='') as c:
    writer = csv.writer(c)
    writer.writerow(fields)
    writer.writerows(infoList)
