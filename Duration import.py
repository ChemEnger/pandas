import pandas as pd
import numpy as np
import os

from tkinter import filedialog
from tkinter import *

from datetime import datetime, date, time

def read_files():
    print('\nSelect file to read')
    TkWindow = Tk()
    TkWindow.withdraw() # we don't want a full GUI, so keep the root window from appearing
    ## Show an "Open" dialog box and return the path to the selected file
    filename = filedialog.askopenfilename(title='Open data file', filetypes=[('Excel', '*.xlsx')], multiple=False)
    TkWindow.destroy()

    if len(filename) == 0:
        print('No files selected - Exiting program.')
        sys.exit()
    else:
        head, tail = os.path.split(filename)
        print(f'Opening {tail} for analysis.')
        return filename

##Attempt 1
def hms_to_s(hms):
    t = 0
    for u in hms.split(':'):
        t = 60 * t + int(u)
    return t

##Attempt 2
def excel_time(time):
    return int(time) + time.hour / 24.0 + time.minute / (24.0*60.0)

##Read df from CSV file (export from Excel)
df = pd.read_excel(read_files(), sheet_name='Sheet1', usecols="A:B", dtype={'Duration': object})

print('\n',df)

df['Duration']= df[['Duration']].to_dict()
df['Duration'] = df['Duration'].astype('<m8[ns]')

print('\n',df)
print('\n',df.dtypes)

##df['Duration'] = df.apply(lambda row : hms_to_s(row['Duration']), axis = 1)
##df['Duration'] = df.apply(lambda row : excel_time(row['Duration']), axis = 1)

##Convert datetime durations to total minutes
df['Duration'] = pd.to_datetime(df['Duration']).dt.time
df['Duration'] = df['Duration'].dt.hour*60 + df['Duration'].dt.minute

##Convert datetime durations to total minutes
df['Duration'] = df['Duration'].dt.hour*60 + df['Duration'].dt.minute

print('\n',df)
