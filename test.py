

import pandas as pd
import csv
from datetime import datetime

new_data=[]

data = pd.read_csv('data.csv')
data = data.to_dict(orient='records')
dates=list([row['Date'] for row in data])
dates.sort(key=lambda date: datetime.strptime(date, "%d.%m.%y"))
print(dates)
    





