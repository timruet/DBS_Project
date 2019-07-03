import csv
from tqdm import tqdm

FOLDER_NAME = "original_data/"

FILE_NAME = "prj_tweet.csv"

NAME = FOLDER_NAME + FILE_NAME

with open(NAME, 'r', encoding="utf8") as csv_file:
    csw_reader = csv.reader(csv_file, delimiter=';')
    csw_reader = list(csw_reader)

with open(f"processed_data/{FILE_NAME}", 'w', encoding="utf8", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in tqdm(csw_reader):
        csv_writer.writerows([row])