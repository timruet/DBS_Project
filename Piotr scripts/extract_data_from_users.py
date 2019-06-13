import pandas


df = pandas.read_csv('original_data/prj_user_preview_data.csv')
df = df[["ID", "Screen Name", "Name", "Verified", "Location"]]
df = df.rename(columns={'Screen Name': 'ScreenName', 'Location': 'City', "Verified": "WearGlasses"})
df.to_csv("processed_data/prj_user_preview_data.csv")





