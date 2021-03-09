# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 09:34:05 2021

@author: Rui
"""
import pandas as pd


df_dgt = pd.read_pickle('cascais.pkl')
df_dgt['NM'].plot()


#%% ler um dia de dados
dados = df_dgt.loc['2020-12-1']
dados['NM'].plot()

#%% ler um valor - atenção à resolução da série df_dgt.index.resolution


dates = '2020-5-1 10:16'
dados = df_dgt.loc[dates]



#%% ler ano


dados = df_dgt.loc['2010']
dados['NM'].plot()


