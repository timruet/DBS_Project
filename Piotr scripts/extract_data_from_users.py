import pandas

df = pandas.read_csv('original_data/prj_user.csv', delimiter=",")
df = df[["id", "screenName", "name", "verified", "location"]]
df = df.rename(
    columns={"id": "id", "screenName": "screenName", "name": "name", 'location': 'city', "verified": "wearGlasses"})


df.to_csv("processed_data/prj_user.csv", index=False, na_rep='NULL')
