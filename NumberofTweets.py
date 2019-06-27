#faster
#number of tweets
nf = pd.Series()
k=0
for i in range(len(users_df["id"])): 
    try:
        k = float(users_df["id"][i])
        x = tweets_df["tweetID"].where(tweets_df["userID"]==k)
        x = x.dropna()
        nf=nf.append(pd.Series([len(x)],index=[k]))
    except:
        pass

