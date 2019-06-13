import pandas
from dateutil import parser

user_df = pandas.read_csv('processed_data/prj_user_preview_data.csv')
tweets_df = pandas.read_csv('original_data/prj_tweet_preview_data.csv')

ids = user_df["ID"]
ids = list(ids.values)
ages = []
tweets_numbers = []

for id in ids:
    last_date =  parser.parse(tweets_df.loc[tweets_df['User_ID'] == id]["createdAt"].values.max())

    first_date = parser.parse(tweets_df.loc[tweets_df['User_ID'] == id]["createdAt"].values.min())

    age = last_date - first_date

    age = age.days
    tweets_number = len(tweets_df.loc[tweets_df['User_ID'] == id]["Tweet_ID"].values)

    ages.append(age)
    tweets_numbers.append(tweets_number)

user_df['Age'] = pandas.Series(ages, index=user_df.index)
user_df['Income'] = pandas.Series(tweets_numbers, index=user_df.index)

user_df.to_csv("processed_data/prj_user_preview_data.csv")
