import pandas as pd

def write_csv_pandas(path,data):
    data.to_csv(path, index=False)

def write_more_csv_pandas(path,data):
    data.to_csv(path, index=False)
        
def read_csv_pandas(csv_file):
     data = pd.read_csv(csv_file)
     return data

def take_data_from_csv(data,index):
      var = []

      for i in range(len(data.values)):
           var.append(data.values[i][index])

      return var