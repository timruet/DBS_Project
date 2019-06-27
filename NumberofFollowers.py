#is fan of
#faster
k=0
ifo=pd.DataFrame()
for i in range(len(users_df["id"])): 
    l_i = pd.Series()
    try:
        k = float(users_df["id"][i])
        x = followings_df["followerID"].where(followings_df["userID"]==k)
        x = x.dropna()
        ifo[users_df["id"][i]]=x
    except:
        pass
