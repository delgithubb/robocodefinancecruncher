

import pandas as pd
import csv

new_data=[]

data = pd.read_csv('data.csv')
data = data.to_dict(orient='records')
dates=set([row['Date'] for row in data])
new_list=[]
header=['NoOfSales','Date']
with open('noofsalesoverdate.csv', 'w') as output_file:
    csv.writer(output_file).writerow(header)
    for date in dates: 
        sub_list=[]
        for row in data:
            if row['Date']==date:
                sub_list.append(row)
        newrow = [str(len(sub_list)),date]
        csv.writer(output_file).writerow(newrow)
        
    





