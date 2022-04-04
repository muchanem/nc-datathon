import pandas as pd
import matplotlib.pyplot as plt

def csv_to_hdf(csv="broadband_survey.csv", name="broadband_survey", hdf="database.h5"):
    df = pd.read_csv(csv)
    df.to_hdf(hdf,key=name,mode="a")

def df_from_hdf(hdf="database.h5", name="broadband_survey"):
    return pd.read_hdf(hdf,key=name)

df = df_from_hdf()
df["RecordedDate"] = pd.to_datetime(df["RecordedDate"])
#print(min(df["RecordedDate"]))
#print(df["c_primary_reason_no_internet"].value_counts())
df = df.loc[df["state_code"] == 37]

groups = df.groupby(by=["county_code", pd.Grouper(key="RecordedDate", freq="3M")])
#groups = df.groupby(by=["county_code"])

groups = [x[1] for x in groups]
records = []
for i, group in enumerate(groups):
    per_access = len(group.loc[(group["dl_speed"] >= 25) & (group["ul_speed"] >= 3)])/len(group)
    obj = {
        "per_access": per_access,
        "county_name": group["county_name"].iloc[0],
        "county_code": group["county_code"].iloc[0],
        "week": group["RecordedDate"].dt.strftime("%Y-%m").iloc[0]
    }
    records.append(obj)

week_county = pd.DataFrame.from_records(records)
county = week_county.sort_values(by=["week","county_code"])
print(week_county)
print(week_county["per_access"].describe())

alamance = week_county.loc[week_county["county_code"] == 1]
plt.scatter(alamance["week"],alamance["per_access"])
plt.show()
exit()

#groups = df.groupby(by=["county_code", pd.Grouper(key="RecordedDate", freq="1M")])
groups = df.groupby(by=["county_code"])

groups = [x[1] for x in groups]
records = []
for i, group in enumerate(groups):
    per_access = len(group.loc[(group["dl_speed"] >= 25) & (group["ul_speed"] >= 3)])/len(group)
    obj = {
        "per_access": per_access,
        "county_name": group["county_name"].iloc[0],
        "county_code": group["county_code"].iloc[0],
        "week": group["RecordedDate"].dt.strftime("%Y-%m").iloc[0]
    }
    records.append(obj)

ndf = pd.DataFrame.from_records(records)
ndf = ndf.sort_values(by="county_code")
print(ndf)