#faster
nf = pd.Series()
k= 0
for i in range(len(users_df["id"])): 
    k = followings_df["userID"][0]
    x = followings_df["followerID"].where(followings_df["userID"]==k)
    x = x.dropna()
    nf=nf.append(pd.Series([len(x)],index=[k]))

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
