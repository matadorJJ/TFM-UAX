# -*- coding: utf-8 -*-
"""anonymizator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CHfgsihEZYZAQDv9W89fiNUTAqq1ST6Q
"""

#
# Juan Julián Moreno Piedra
# 27-08-2024
#

#
# Masking of the real name of the servers
#
#

# Import necessary libraries
import pandas as pd
import os
import io
import gdown

# downoading CST data file from Google Drive
# file has been modified to mask the real name of the servers
# to guarantee confienciality
#
file_id = '13C8r4F8oIn-0Ii4KyvhOm1tUwOij-uFC&usp=drive_fs'
# file_id= '138rPG6moGxMKkt77ogCoCRdBTE_Eh6Ni'
url = f"https://drive.google.com/uc?id={file_id}"
output = 'se.tab'  # Nombre del archivo de salida
gdown.download(url, output, quiet=False)

# downoading Sessions data file from Google Drive
# file has been modified to mask the real name of the servers
# to guarantee confienciality
#
file_id = '14uyoXlGowfDhE7Eoh5DqdTPwnROnGkGV'
# file_id= '138rPG6moGxMKkt77ogCoCRdBTE_Eh6Ni'
url = f"https://drive.google.com/uc?id={file_id}"
output = 'archivo.csv'  # Nombre del archivo de salida
gdown.download(url, output, quiet=False)

# Reading the Backup Sessions CSV file
df_backup = pd.read_csv('archivo.csv')

# Import the CSV file
df_cst = pd.read_csv('se.tab')

# Create a unique set of all servers from both dataframes
unique_servers = set(df_backup['Client']).union(set(df_cst['# Client']))

# Create a mapping from server to alias
server_mapping = {server: f"Server_{i+1}.uax" for i, server in enumerate(unique_servers)}

# Replace the server names in both dataframes using the mapping
df_backup['Client'] = df_backup['Client'].map(server_mapping)
df_cst['# Client'] = df_cst['# Client'].map(server_mapping)

# Save each dataframe to a separate CSV file
df_backup.to_csv('df_backup_anon.csv', index=False)
df_cst.to_csv('df_cst_anon.csv', index=False)



