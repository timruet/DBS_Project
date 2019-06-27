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

