import pandas as pd
from typing import List

def load_data(path: str, cols: List[str]) -> pd.DataFrame:
  """
  Loads a csv file and returns a pandas dataframe
  """
  with open(path, 'r') as input:
    if not cols:
      data = pd.read_csv(input)
      return data
    else:
      data = pd.read_csv(input, usecols=cols)
      return data

def drop_col(data: pd.DataFrame, col_name: str) -> pd.DataFrame:
  """
  Drops a given column from a dataframe
  """
  new_data = data.drop(columns=col_name)
  return new_data

data = load_data("bc_trip259172515_230215.csv", None)
data = drop_col(data, "EVENT_NO_STOP")
data = drop_col(data, "GPS_SATELLITES")
data = drop_col(data, "GPS_HDOP")
print(data.describe())

print("\n")

use_cols_data = load_data("bc_trip259172515_230215.csv",
                          ["EVENT_NO_TRIP", "VEHICLE_ID", "OPD_DATE", "METERS", "ACT_TIME", "GPS_LONGITUDE", "GPS_LATITUDE"])
print(use_cols_data.describe())
