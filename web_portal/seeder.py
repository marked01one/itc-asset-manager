import json, sys, requests
import pandas as pd
from datetime import datetime

class IncorrectArgumentsError(Exception):
  '''
  Extension exception class for incorrect args 
  '''


def seed_data(model: str):
  if model.lower() == 'transformer':
    # Extract dataset as Pandas DataFrame
    df = pd.read_csv("../analysis/dataset_main.csv", index_col=False)
    # Loop all objects 
    for i in range(len(df['serial_number'])):
      response = requests.post(
        f"http://localhost:8000/api/transformer/",
        data={
          "manufacturer": df['manufacturer'][i],
          "region": df['region'][i],
          'serial_number': df['serial_number'][i],
          'kva': float(df['kva'][i]),
          'date_created': f"{2023 - int(df['age'][i])}-01-01"
        }
      )  
      print(f"Response code: {response.status_code}")
    return
  
  
  if model.lower() == 'failure':
    # Extract dataset as Pandas DataFrame
    df = pd.read_csv("../analysis/dataset_main.csv", index_col=False)
    # Loop all objects
    for i in range(len(df['serial_number'])):
      response = requests.post(
        "http://localhost:8000/api/failure/",
        data={
          'transformer': df['serial_number'][i],
          'failure_cause': df['failure_cause'][i],
          'date_failed': datetime.strptime(df['failure_date'][i], "%m/%d/%Y").strftime("%Y-%m-%d")
        }
      )
      print(f"Response code: {response.status_code}")
    pass
  
  else:
    # Open the JSON
    with open("./seed/seed_data.json", "r") as file:
      obj_list: list[dict] = json.load(file)[model.lower()]
    # Loop through all objects in the JSON
    for body in obj_list:
      response = requests.post(f"http://localhost:8000/api/{model.lower()}/", data=body)
      print(f"Response code: {response.status_code}")
    return
  
  

if __name__ == '__main__':
  if len(sys.argv) != 2:
    raise IncorrectArgumentsError(f"Current number of args ({len(sys.argv)}) is not equal to 2!")
  
  seed_data(model=sys.argv[1].lower())



