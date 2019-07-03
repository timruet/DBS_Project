import pandas

user_df = pandas.read_csv('processed_data/prj_user.csv')

ids = user_df["id"]
ids = list(ids.values)

error_ids= []

for i, id in enumerate(ids):
    try:
        int(id)
    except:
        error_ids.append(i)


user_df = user_df.drop(user_df.index[error_ids])

user_df.to_csv("processed_data/prj_user.csv", index=False)
