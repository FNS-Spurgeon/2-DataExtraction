# Data Extraction
This repository contains the data extracted from the [transcriptions](https://github.com/FNS-Spurgeon/1-Transcription) of the three volumes *Five Hundred Years of Chaucer Criticism and Allusion* (Caroline Spurgeon, 1925), and of the *Supplement* (1920).

## Workflow
  1. The TXT files obtained after the OCR are divided in pages with [pageSplit.py](https://github.com/FNS-Spurgeon/2-DataExtraction/blob/main/scripts/pageSplit.py). Pages are stored in [pages](https://github.com/FNS-Spurgeon/2-DataExtraction/tree/main/pages). 
  2. We isolate each entry of the catalogue in a .txt file with [allusionSplit.py](https://github.com/FNS-Spurgeon/2-DataExtraction/blob/main/scripts/allusionsplit.py), by using the entry date as a split pattern. An ID is assigned to these new files: volume_page_allusionNb. For instance, the file vol1_p21_a1 equals the first allusion on page 21 of volume 1; the file vol1_p18_a2 equals the second allusion on page 18 of volume 1. The files are available in [allusions](https://github.com/FNS-Spurgeon/2-DataExtraction/tree/main/allusions).
  3. From each allusion, we extract specific data and export them in a CSV file, with [dataextraction.py](https://github.com/FNS-Spurgeon/2-DataExtraction/blob/main/scripts/dataextraction.py). We target the date, the author, the title and the remaining of the text. These new files are stored in [csv-files](https://github.com/FNS-Spurgeon/2-DataExtraction/tree/main/csv-files).

## Specific case: the index
Part of the index (vol.3, pp. 10-34), containing a 10-categories classification of Chaucer allusions, has been [transcribed](https://github.com/FNS-Spurgeon/1-Transcription/blob/main/vol3/index.txt) and corrected. Each category and subcategory have been cleanded and split into [TXT files](https://github.com/FNS-Spurgeon/2-DataExtraction/tree/main/index/index-txt), in a hierarchy that reproduces the one of the index. Entries cited for each category are then turned into a [CSV file](https://github.com/FNS-Spurgeon/2-DataExtraction/tree/main/index/index-csv), using the script [indexSplit.py](https://github.com/FNS-Spurgeon/2-DataExtraction/blob/main/scripts/indexSplit.py). The CSV files preserve all the information given by the index, namely the author's surname, the date, the volume's part and the pages.

## Licence
All data are published under the licence [CC-BY](https://creativecommons.org/licenses/by/4.0/).
