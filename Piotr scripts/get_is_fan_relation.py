import pandas

df = pandas.read_csv('original_data/prj_following.csv', delimiter=",")
df = df[["followerID", "userID"]]
df = df.rename(
    columns={"followerID" : "fanID", "userID" : "idolID"})


df.to_csv("processed_data/is_fan.csv", index=False)