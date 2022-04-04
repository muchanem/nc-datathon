import pandas as pd


def csv_to_hdf(csv="broadband_survey.csv", name="broadband_survey", hdf="database.h5"):
    df = pd.read_csv(csv)
    df.to_hdf(hdf,key=name,mode="a")

def df_from_hdf(hdf="database.h5", name="broadband_survey"):
    return pd.read_hdf(hdf,key=name)

df = df_from_hdf()
df["RecordedDate"] = pd.to_datetime(df["RecordedDate"])
print(min(df["RecordedDate"]))
print(df["c_primary_reason_no_internet"].value_counts())