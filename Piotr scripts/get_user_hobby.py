import pandas
from dateutil import parser
from collections import Counter

user_df = pandas.read_csv('processed_data/prj_user_preview_data.csv')
tweets_df = pandas.read_csv('original_data/prj_tweet_preview_data.csv')

ids = user_df["ID"]
ids = list(ids.values)

hobby_1_list = []
hobby_2_list = []

def get_users_most_popular_hashtags_list(tweets_df, user_id, number_of_wanted_hashtags=2):
    """
    :param user_id: id of user for which we want to get
    :return: list of strings, size of number_of_wanted_hashtags or smaller if user doesn't have enough hashtags
    """
    tweets = list(tweets_df.loc[tweets_df['User_ID'] == user_id]["tweet"].values)

    tweets_with_hashtag = [tweet for tweet in tweets if "#" in tweet]

    user_hashtags = []

    for tweet in tweets_with_hashtag:
        user_hashtags += [i[1:] for i in tweet.split() if i.startswith("#")]

    users_most_common_hashtags = [word for word, word_count in Counter(user_hashtags).most_common(number_of_wanted_hashtags)]

    return users_most_common_hashtags

for id in ids:
    users_most_common_hashtags = get_users_most_popular_hashtags_list(tweets_df=tweets_df, user_id = id, number_of_wanted_hashtags=2)

    if len(users_most_common_hashtags) < 2:
        while len(users_most_common_hashtags) < 2:
            users_most_common_hashtags.append(None)

    hobby_1_list.append(users_most_common_hashtags[0])
    hobby_2_list.append(users_most_common_hashtags[1])


hobby_df = pandas.read_csv('processed_data/prj_user_preview_data.csv')
hobby_df['Hobby'] = pandas.Series(hobby_1_list, index=hobby_df.index)
hobby_df = hobby_df[["ID", "Hobby"]]
hobby_df.to_csv("processed_data/hobby1.csv")


hobby_df = pandas.read_csv('processed_data/prj_user_preview_data.csv')
hobby_df['Hobby'] = pandas.Series(hobby_2_list, index=hobby_df.index)
hobby_df = hobby_df[["ID", "Hobby"]]
hobby_df.to_csv("processed_data/hobby2.csv")