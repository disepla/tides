# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 09:34:05 2021

@author: Rui
"""
import pandas as pd
import matplotlib.pyplot as plt


#%%
df_dgt_h = pd.read_pickle('cascais_hour_ss.pkl')
dados = df_dgt_h.loc['2019-6-5':'2019-9-30']



fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, sharey=True, sharex=True)
 
dados['NM'].plot(ax = ax0, label=u'Observations', color='C0')
dados['Tide'].plot(ax = ax1, label=u'Tide Fit', color='C1')
dados['SS'].plot(ax = ax2,  label=u'Residual', color='C2')
   
    
fig.legend(ncol=3, loc='upper center')
