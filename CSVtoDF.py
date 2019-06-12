#I used the unique paths in my dictionary to get to the csv file, you have to change that to your own path
import pandas as pd
import os
import csv
os.chdir("/Users/Tim/Documents/Tim/Studium/Berlin/Informatik/DBS/Projekt")
FILE_NAME = "prj_user.csv"

with open(FILE_NAME, 'r', encoding="utf8") as csv_file:
    csw_reader = csv.reader(csv_file, delimiter=';')
    csw_reader = list(csw_reader)

with open(f'/Users/Tim/Documents/Tim/Studium/Berlin/Informatik/DBS/Projekt/{FILE_NAME}', 'w', encoding="utf8") as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in csw_reader:
        csv_writer.writerows([row])
        
FILE_NAME2 = "prj_following.csv"

with open(FILE_NAME2, 'r', encoding="utf8") as csv_file:
    csw_reader = csv.reader(csv_file, delimiter=';')
    csw_reader = list(csw_reader)

with open(f'/Users/Tim/Documents/Tim/Studium/Berlin/Informatik/DBS/Projekt/{FILE_NAME2}', 'w', encoding="utf8") as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in csw_reader:
        csv_writer.writerows([row])
        
FILE_NAME3 = "prj_tweet.csv"

with open(FILE_NAME3, 'r', encoding="utf8") as csv_file:
    csw_reader = csv.reader(csv_file, delimiter=';')
    csw_reader = list(csw_reader)

with open(f'/Users/Tim/Documents/Tim/Studium/Berlin/Informatik/DBS/Projekt/{FILE_NAME3}', 'w', encoding="utf8") as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in csw_reader:
        csv_writer.writerows([row])
users_df = pd.read_csv("/Users/Tim/Documents/Tim/Studium/Berlin/Informatik/DBS/Projekt/prj_user.csv")

followings_df = pd.read_csv("/Users/Tim/Documents/Tim/Studium/Berlin/Informatik/DBS/Projekt/prj_following.csv")
tweets_df = pd.read_csv("/Users/Tim/Documents/Tim/Studium/Berlin/Informatik/DBS/Projekt/prj_tweet.csv")
