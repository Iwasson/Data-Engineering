import pandas as pd

def load_csv(path: str) -> pd.DataFrame:
  with open(path, "r") as input:
    data = pd.read_csv(input)
  return data

def missing_data(data: pd.DataFrame) -> None:
    missing_count = data.isna().sum()
    missing_pct = missing_count / len(data) * 100
    missing_df = pd.concat([missing_count, missing_pct], axis=1, keys=['missing_count', 'missing_pct'])
    missing_df = missing_df[missing_df['missing_count'] > 0] 
    missing_df.index.name = 'column'
    missing_df = missing_df.sort_values(by='missing_pct', ascending=True)
    print(missing_df)


def assertions(data: pd.DataFrame) -> bool:
  date_counts = pd.DataFrame(data.value_counts(["Crash Month", "Crash Day", "Crash Year"]))
  print(date_counts)

  latitude_counts   = pd.DataFrame(data.value_counts(["Latitude Degrees", "Latitude Minutes", "Latitude Seconds"]))
  longitude_counts  = pd.DataFrame(data.value_counts(["Longitude Degrees", "Longitude Minutes", "Longitude Seconds"]))
  print(latitude_counts)
  print(longitude_counts)

  crash_counts = pd.DataFrame(data.value_counts(["Record Type"]))
  print(crash_counts)

  crash_months_counts = pd.DataFrame(data.value_counts(["Crash Month"]))
  print(crash_months_counts)

csv_data = load_csv("Hwy26Crashes2019_S23.csv")
assertions(csv_data)
