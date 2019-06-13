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

#Pandas Series with number of tweets with corresponding userID as index
l = pd.Series()
nt = pd.Series()
for j in range(len(tweets_df["userID"])):
    n=0
    if not(tweets_df["userID"][j] in l.unique()):
        l = l.append(pd.Series([tweets_df["userID"][j]]))
        for i in range(len(tweets_df["userID"])-(j+1)):
            if tweets_df["userID"][i+j+1] == tweets_df["userID"][j]:
                n += 1
        nt = nt.append(to_append=pd.Series([n],index=[tweets_df["userID"][j]])) 

