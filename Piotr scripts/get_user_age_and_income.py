import pandas
from dateutil import parser
from tqdm import tqdm

user_df = pandas.read_csv('processed_data/prj_user.csv')
tweets_df = pandas.read_csv('original_data/prj_tweet.csv')

ids = user_df["id"]
ids = list(ids.values)
ages = []
tweets_numbers = []

for id in tqdm(ids):

    try:
        last_date = parser.parse(tweets_df.loc[tweets_df['userID'] == int(id)]["createdAt"].values.max())

        first_date = parser.parse(tweets_df.loc[tweets_df['userID'] == int(id)]["createdAt"].values.min())

        age = last_date - first_date

        age = age.days

        tweets_number = len(tweets_df.loc[tweets_df['userID'] == id]["tweetID"].values)


    except Exception as e:
        age = 0
        tweets_number = 0

    ages.append(age)
    tweets_numbers.append(tweets_number)


user_df['age'] = pandas.Series(ages, index=user_df.index)
user_df['income'] = pandas.Series(tweets_numbers, index=user_df.index)

user_df.to_csv("processed_data/prj_user.csv", index=False)
