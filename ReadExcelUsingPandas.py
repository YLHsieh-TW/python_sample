import pandas as pd
import requests
import json
from numpyencoder import NumpyEncoder

data = pd.read_excel(r'test.xlsx', sheet_name='Teeeest1', header=0)
df = pd.DataFrame(data)
#print (df)

for ind in df.index:
    #r = requests.post('https://www.google.com.tw/')
    header = {'Authorization': 'PS-Auth key=c479a66f…c9484d; runas=doe-main\johndoe;'}
    #print ('Price => ', df['Product'][ind], '\tOwner => ', df['Owner'][ind], '\tPrice => ', df['Price'][ind])
    my_data = { 'Product' : df['Product'][ind], 'Owner' : df['Owner'][ind], 'Price' : df['Price'][ind]}
    ##session = requests.Session()
    ##session.headers.update(header)
    json_data = json.dumps(my_data, sort_keys=True, indent=4, cls=NumpyEncoder)
    print (my_data)
    ##response = session.post('https://www.google.com.tw/', data = my_data)
    ##prinf ('web respon code', response)