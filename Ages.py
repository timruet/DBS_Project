#faster
import datetime as dt
ages = pd.Series()
tweets_df["createdAt"] = pd.to_datetime(tweets_df["createdAt"])
for j in range(len(users_df["id"]):   
    try:
        k = float(users_df["id"][j])
        x = tweets_df["createdAt"].where(tweets_df["userID"]==k).max()
        y = tweets_df["createdAt"].where(tweets_df["userID"]==k).min()
        a = x-y
        a = a.total_seconds()
        ages = ages.append(to_append=pd.Series([a],index=[k]))        
    except: 
        pass





#Panda Series ages contains the ages with the userID as corresponding index
import datetime as dt
mf = pd.DataFrame(columns = ["age"])
ages = pd.Series()
tweets_df["createdAt"] = pd.to_datetime(tweets_df["createdAt"])
l = pd.Series()
for j in range(len(tweets_df["userID"])):
    if not(tweets_df["userID"][j] in l.unique()):
        l = l.append(to_append=pd.Series([tweets_df["userID"][j]]),ignore_index=True)
        x = tweets_df["userID"][j]
        y = tweets_df["createdAt"][j]
        z = tweets_df["createdAt"][j]
        for i in range(len(tweets_df["userID"])):
            if tweets_df["userID"][i]==x and (tweets_df["createdAt"][i]<y):
                y = tweets_df["createdAt"][i]
            if tweets_df["userID"][i]==x and (tweets_df["createdAt"][i]>z):
                z = tweets_df["createdAt"][i]
        a = z-y
        a = a.total_seconds()
        ages = ages.append(to_append=pd.Series([a],index=[tweets_df["userID"][j]]))

