import csv

FOLDER_NAME = "original_data/"

FILE_NAME = "prj_tweet_preview_data.csv"

NAME = FOLDER_NAME + FILE_NAME

with open(NAME, 'r', encoding="utf8") as csv_file:
    csw_reader = csv.reader(csv_file, delimiter=';')
    csw_reader = list(csw_reader)

with open(NAME, 'w', encoding="utf8", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in csw_reader:
        # row = row[0].split(",")
        csv_writer.writerows([row])