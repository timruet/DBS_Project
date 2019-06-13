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

#gives dataframe with userIDs as columns and followers in rows
l = pd.Series()
nf = pd.DataFrame()
k= 0
for i in range(len(followings_df["userID"])):
    if not(followings_df["userID"][i] in l.unique()):
        l = l.append(to_append=pd.Series([followings_df["userID"][i]]))
        l_i = pd.Series() 
        for j in (range(len(followings_df["userID"]))):
            if followings_df["userID"][i]==followings_df["userID"][j]:
                l_i = l_i.append(to_append=pd.Series([followings_df["followerID"][j]]),ignore_index=True)
        nf[str(followings_df["userID"][i])]= l_i
