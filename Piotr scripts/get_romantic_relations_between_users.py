import pandas
import pandas as pd
from tqdm import tqdm

user_df = pandas.read_csv('processed_data/prj_user.csv')
tweets_df = pandas.read_csv('original_data/prj_tweet.csv')

ids = user_df["id"]
ids = list(ids.values)


def get_retweeted_users_id_and_retweet_date(user_id):
    tweets_and_its_dates = tweets_df.loc[tweets_df['userID'] == int(user_id)][["tweet", 'createdAt']]
    tweets_and_its_dates = [tuple(x) for x in tweets_and_its_dates.values]


    retweets_and_its_dates = [(tweet, date) for tweet, date in tweets_and_its_dates if "RT" in tweet]

    retweeted_users_and_retweet_date = []



    for tweet, date in retweets_and_its_dates:
        words = tweet.split()
        pairs = [words[i] + ' ' + words[i + 1] for i in range(len(words) - 1)]

        try:
            user_screen_name = [i[4:-1] for i in pairs if i.startswith("RT @")][0]

            user_id = get_id_by_user_screen_name(screen_name=user_screen_name)

            retweeted_users_and_retweet_date.append((user_id, date))

        except:
            pass



    return retweeted_users_and_retweet_date


def get_id_by_user_screen_name(screen_name):

    user_id = user_df.loc[user_df['screenName'] == screen_name]["id"].values[0]

    return user_id




retweets = {}


for i, id in tqdm(enumerate(ids)):
    retweeted_users_id_and_retweet_date = get_retweeted_users_id_and_retweet_date(user_id = id)


    if retweeted_users_id_and_retweet_date:
        retweets[id] = retweeted_users_id_and_retweet_date

    if i > 500:
        break


incommon_retweets = []



for id1 in tqdm(ids):
    try:
        for retweeted_user_id, date1 in retweets[id1]:
            try:
                for id2, date2 in retweets[retweeted_user_id]:
                    if (id1 == id2) and (date1 == date2):
                        incommon_retweets.append((id1, retweeted_user_id))
                        print("We have a date !!!")

            except KeyError:
                pass
    except KeyError:
        pass


dates = incommon_retweets
marriages = set([x for x in incommon_retweets if incommon_retweets.count(x) > 1])


dates_df= pd.DataFrame(incommon_retweets, columns=['userID_1', "userID2"])
dates_df.to_csv("processed_data/dates.csv", index=False, na_rep='NULL')

marriages_df= pd.DataFrame(incommon_retweets, columns=['userID_1', "userID2"])
marriages_df.to_csv("processed_data/marriage.csv", index=False, na_rep='NULL')





