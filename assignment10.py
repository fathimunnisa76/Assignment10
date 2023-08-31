# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 19:38:11 2023

@author: HP
"""

import pandas as pd
df=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\friends__names.xlsx")
df

df[df['quality']=='intelligent']

df[df['quality']=='funny']

df2=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\family_members.xlsx")
df2

df2[(df2['relation']=='brother') | (df2['relation']=='sister')]


df2[(df2['relation']=='mother') | (df2['relation']=='father')]

lst1=['mother','father']
df2[~df2['relation'].isin(lst1)]

lst2=['brother']
df2[~df2['relation'].isin(lst2)]

lst3=['mother','father','brother']
df2[df2['relation'].isin(lst3)]

df3=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\vegfood_items.xlsx")
df3

df3[df3['type']=='soup']

df3[df3['type']=='fry']

df3[df3['type']=='curry']

lst4=['soup','fry']
df3[df3.type.isin(lst4)]

lst5=['soup','fry']
df3[~df3.type.isin(lst5)]

df3[(df3['type']=='soup') | (df3['type']=='fry')]

df4=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\nonveg_items.xlsx")
df4

df4[df4['item']=='chicken']

df4[df4['item']=='mutton']

df4[df4['type']=='fry']

lst6=['chicken','fry']
df4[(df4['type'].isin(lst6)) | (df4['item'].isin(lst6))]

lst7=['mutton','fry']
df4[(~(df4['type'].isin(lst7))) & (~(df4['item'].isin(lst7)))]


df5=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\months_with_season.xlsx")
df5

df5[df5['season']=='rainy']

df5[df5['season']=='summer']

df5[df5['season']=='winter']

df5[(df5['season']=='winter') | (df5['season']=='summer')]

lst8=['summer','rainy']
df5[~df5['season'].isin(lst8)]

df5[(df5['season']=='winter') | (df5['season']=='rainy')]

df6=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\flowers_names.xlsx")
df6

df6[df6['colour_name']=='red']

df6[df6['colour_name']=='pink']

df6[df6['colour_name']=='white']

lst9=['red','pink']
df6[df6['colour_name'].isin(lst9)]

lst10=['red','white']
df6[~df6['colour_name'].isin(lst10)]

df6[(df6['colour_name']=='red') | (df6['colour_name']=='pink')]

