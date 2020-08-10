import pandas as pd
import requests
import json
from numpyencoder import NumpyEncoder

data = pd.read_excel(r'test.xlsx', sheet_name='Teeeest1', header=0)
df = pd.DataFrame(data)
#print (df)

for ind in df.index:
    my_data = { 'Product' : df['Product'][ind], 'Owner' : df['Owner'][ind], 'Price' : df['Price'][ind]}
    json_data = json.dumps(my_data, sort_keys=True, indent=4, cls=NumpyEncoder)
    print (my_data)
