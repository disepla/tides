# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 21:17:19 2020

@author: Rui
"""

import zipfile
from pathlib import Path
import pandas as pd
import numpy as np

header_list = ["index", "Maregrafo", "Data", "Sensor", 'NM']
tide_gauge_data = pd.DataFrame()


def read_td_file(file, zip_file = False, print_filename = True, print_error_filename = True, dayfirst = False):
    if print_filename:
        print(file)
    try:
        if zip_file:
            file = zip.open(file) 
        df = pd.read_csv(file, comment='#', header=None, sep='%|: ', engine='python')
        
        df.reset_index(inplace = True)
        df.columns = header_list
        df['Data'] = pd.to_datetime(df['Data'], dayfirst = dayfirst)
        return df
    
    except : 
        if print_error_filename:
            print('erro no ficheiro' , file)
        return
    
    
    

#%% read zip files

for file in Path('D:/Dados/Marégrafos/Cascais/dayfirstfalse').rglob('*.zip'):
    zip = zipfile.ZipFile(file)
    files_in_zip = zip.namelist()
    water_level_files = [s for s in files_in_zip if ".aq" in s]
    for file in water_level_files:
        tide_gauge_data = tide_gauge_data.append(read_td_file(file, zip_file = True))

for file in Path('D:/Dados/Marégrafos/Cascais/dayfirsttrue').rglob('*.zip'):
    zip = zipfile.ZipFile(file)
    files_in_zip = zip.namelist()
    water_level_files = [s for s in files_in_zip if ".aq" in s]
    for file in water_level_files:
        tide_gauge_data = tide_gauge_data.append(read_td_file(file, zip_file = True, dayfirst = True))

        
#%% read other files
for file in Path('D:/Dados/Marégrafos/Cascais/dayfirstfalse').rglob('*.aq'):
    tide_gauge_data = tide_gauge_data.append(read_td_file(file))

for file in Path('D:/Dados/Marégrafos/Cascais/dayfirsttrue').rglob('*.aq'):
    tide_gauge_data = tide_gauge_data.append(read_td_file(file, dayfirst = True))


#%%
tide_gauge_data.set_index('Data', inplace = True)

#%%
td = tide_gauge_data.copy()
sea_level_nmm = tide_gauge_data['NM'].loc[:'2009-2-2'] - 2080
td.loc[:'2009-2-2', 'NM'] = sea_level_nmm

#data files erased
#02-02-2009
#20-02-2009
#14-05-2009 8h
#15-06-2009 6h-8h
#18-06-2009 
#19-06-2009 
#20-06-2009 
#13/20-07-2009

#td[td['NM'] > 3000] = np.NaN #só há um erro no dia 16-21-2017

td.loc[td['NM'] > 3000] = np.NaN
td['NM'] /= 1000
td.to_pickle('cascais.pkl')
td.to_pickle('cascais_the_old_protocol_4.pkl', protocol = 4)
td['NM'].resample('Y').mean().plot()
td_hour = td.resample('H').mean()
td_hour.to_pickle('cascais_hour.pkl')
