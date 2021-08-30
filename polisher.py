import numpy as np
import pandas as pd
from datetime import date
from os import listdir
from os.path import isfile, join


def d_day_index(f, n):
    for i1 in range(n):
        f.loc[i1, ['day_index']] = i1+1
    return f


def state_hour(f, n):
    for i2 in range(n + 1):
        dn = 24 * i2
        f.loc[dn:dn + 6, ['state']] = str('dark')
        f.loc[dn + 7:dn + 18, ['state']] = str('light')
        f.loc[dn + 19:dn + 24, ['state']] = str('dark')
    return f


def m_day_and_hour_index(f, n):
    h_counter = 1
    for i3 in range(n + 1):
        dn = 24 * i3
        f.loc[dn:dn + 23, ['day_index']] = i3+1
        for j3 in range(24):
            interval_m = dn + j3
            f.loc[interval_m:interval_m + 1, ['hour_index']] = h_counter
            h_counter = h_counter + 1
    return f


def state_(f, n):
    for i4 in range(n + 1):
        dn = 1440 * i4
        f.loc[dn:dn + 419, ['state']] = str('dark')
        f.loc[dn + 420:dn + 1139, ['state']] = str('light')
        f.loc[dn + 1140:dn + 1439, ['state']] = str('dark')
    return f


def day_and_hour_index(f, n):
    h_counter = 1
    for i5 in range(n + 1):
        dn = 1440 * i5
        f.loc[dn:dn + 1439, ['day_index']] = i5+1
        for j5 in range(24):
            interval_m = dn + (j5*60)
            f.loc[interval_m:interval_m + 60, ['hour_index']] = h_counter
            h_counter = h_counter + 1
    return f


def writer_(main_df, list_of_them, number, method, a_n):
    print(number)
    file = pd.read_excel("{}".format(list_of_them[number]), skiprows=35)
    if method == str('dep_onlywater'):
        file_ = file.rename(columns={'Unnamed: 0': 'date', 'Unnamed: 1': 'time', 'Unnamed: 2': 'animal',
                                     'Unnamed: 3': 'box', '[ml]': 'water'})
        extracted_a1 = file_[file_['box'] == a_n]
        list_index = list(file_[file_['box'] == a_n].index)
        for i6 in range(len(extracted_a1)):
            ind0 = main_df.loc[(main_df['date'] == extracted_a1['date'][list_index[i6]].strftime('%Y-%m-%d')) &
                               (main_df['time'] == extracted_a1['time'][list_index[i6]].strftime('%H:%M:%S'))].index[0]
            main_df.loc[ind0, 'water'] = extracted_a1['water'][list_index[i6]]
    elif method == str('ade_only'):
        file_ = file.rename(columns={'Unnamed: 0': 'date', 'Unnamed: 1': 'time', 'Unnamed: 2': 'animal',
                                     'Unnamed: 3': 'box', '[ml]': 'water', '[ml].1': 'alcohol-5%',
                                     '[ml].2': 'alcohol-10%', '[ml].3': 'alcohol-20%'})
        extracted_a1 = file_[file_['box'] == a_n]
        list_index = list(file_[file_['box'] == a_n].index)
        for i7 in range(len(extracted_a1)):
            ind1 = main_df.loc[(main_df['date'] == extracted_a1['date'][list_index[i7]].strftime('%Y-%m-%d')) &
                               (main_df['time'] == extracted_a1['time'][list_index[i7]].strftime('%H:%M:%S'))].index[0]
            main_df.loc[ind1, 'water'] = extracted_a1['water'][list_index[i7]]
            main_df.loc[ind1, 'alcohol-5%'] = extracted_a1['alcohol-5%'][list_index[i7]]
            main_df.loc[ind1, 'alcohol-10%'] = extracted_a1['alcohol-10%'][list_index[i7]]
            main_df.loc[ind1, 'alcohol-20%'] = extracted_a1['alcohol-20%'][list_index[i7]]
    elif method == str('ade_oxy'):
        file_ = file.rename(columns={'Unnamed: 0': 'date', 'Unnamed: 1': 'time', 'Unnamed: 2': 'animal',
                                     'Unnamed: 3': 'box', '[ml]': 'water', '[ml].1': 'alcohol-5%',
                                     '[ml].2': 'alcohol-10%', '[ml].3': 'alcohol-20%'})
        extracted_a1 = file_[file_['box'] == a_n]
        list_index = list(file_[file_['box'] == a_n].index)
        for i8 in range(len(extracted_a1)):
            ind2 = main_df.loc[(main_df['date'] == extracted_a1['date'][list_index[i8]].strftime('%Y-%m-%d')) &
                               (main_df['time'] == extracted_a1['time'][list_index[i8]].strftime('%H:%M:%S'))].index[0]
            main_df.loc[ind2, 'water'] = extracted_a1['water'][list_index[i8]]
            main_df.loc[ind2, 'alcohol-5%'] = extracted_a1['alcohol-5%'][list_index[i8]]
            main_df.loc[ind2, 'alcohol-10%'] = extracted_a1['alcohol-10%'][list_index[i8]]
            main_df.loc[ind2, 'alcohol-20%'] = extracted_a1['alcohol-20%'][list_index[i8]]
            main_df.loc[ind2, 'oxytocin'] = str('applied')
    elif method == str('dep_quinine'):
        file_ = file.rename(columns={'Unnamed: 0': 'date', 'Unnamed: 1': 'time', 'Unnamed: 2': 'animal',
                                     'Unnamed: 3': 'box', '[ml]': 'water'})
        extracted_a1 = file_[file_['box'] == a_n]
        list_index = list(file_[file_['box'] == a_n].index)
        for i9 in range(len(extracted_a1)):
            ind3 = main_df.loc[(main_df['date'] == extracted_a1['date'][list_index[i9]].strftime('%Y-%m-%d')) &
                               (main_df['time'] == extracted_a1['time'][list_index[i9]].strftime('%H:%M:%S'))].index[0]
            main_df.loc[ind3, 'water'] = extracted_a1['water'][list_index[i9]]
            main_df.loc[ind3, 'quinine'] = str('applied')
    elif method == str('ade_quinine'):
        file_ = file.rename(columns={'Unnamed: 0': 'date', 'Unnamed: 1': 'time', 'Unnamed: 2': 'animal',
                                     'Unnamed: 3': 'box', '[ml]': 'water', '[ml].1': 'alcohol-5%',
                                     '[ml].2': 'alcohol-10%', '[ml].3': 'alcohol-20%'})
        extracted_a1 = file_[file_['box'] == box]
        list_index = list(file_[file_['box'] == a_n].index)
        for i10 in range(len(extracted_a1)):
            ind4 = main_df.loc[(main_df['date'] == extracted_a1['date'][list_index[i10]].strftime('%Y-%m-%d')) &
                               (main_df['time'] == extracted_a1['time'][list_index[i10]].strftime('%H:%M:%S'))].index[0]
            main_df.loc[ind4, 'water'] = extracted_a1['water'][list_index[i10]]
            main_df.loc[ind4, 'alcohol-5%'] = extracted_a1['alcohol-5%'][list_index[i10]]
            main_df.loc[ind4, 'alcohol-10%'] = extracted_a1['alcohol-10%'][list_index[i10]]
            main_df.loc[ind4, 'alcohol-20%'] = extracted_a1['alcohol-20%'][list_index[i10]]
            main_df.loc[ind4, 'quinine'] = str('applied')
    else:
        print("{} is non of them".format(list_of_them[number]))
    return main_df


animal = 1003
box = 3
strain = str('Wistar')
date_i = date(2020, 2, 12)
date_f = date(2020, 11, 17)

delta = date_f - date_i
number_of_days = int(delta.days) + 1
print(number_of_days)
total_length = number_of_days * 1440
df = pd.DataFrame(index=range(total_length), columns=['date', 'time', 'day_index', 'hour_index', 'animal', 'box',
                                                      'strain', 'state', 'oxytocin', 'quinine', 'water', 'alcohol-5%',
                                                      'alcohol-10%', 'alcohol-20%', 'locomotive'])
df = state_(df, number_of_days)
df = day_and_hour_index(df, number_of_days)
df['animal'] = animal
df['box'] = box
df['strain'] = strain
df['date'] = pd.date_range("2020-02-12", periods=total_length, freq="T").strftime('%Y-%m-%d')
df['time'] = pd.date_range("2020-02-12", periods=total_length, freq="T").strftime('%H:%M:%S')
onlyfiles = [f for f in listdir("/Users/mehrd/Desktop/work/fun/run/")
             if isfile(join("/Users/mehrd/Desktop/work/fun/run/", f))]

df = writer_(df, onlyfiles, 0, str('dep_onlywater'), box)
df = writer_(df, onlyfiles, 1, str('ade_only'), box)
df = writer_(df, onlyfiles, 2, str('ade_only'), box)
df = writer_(df, onlyfiles, 3, str('ade_only'), box)
df = writer_(df, onlyfiles, 4, str('ade_only'), box)
df = writer_(df, onlyfiles, 5, str('dep_onlywater'), box)
df = writer_(df, onlyfiles, 6, str('dep_onlywater'), box)
df = writer_(df, onlyfiles, 7, str('ade_only'), box)
df = writer_(df, onlyfiles, 8, str('ade_only'), box)
df = writer_(df, onlyfiles, 9, str('ade_only'), box)
df = writer_(df, onlyfiles, 10, str('ade_only'), box)

df = writer_(df, onlyfiles, 11, str('dep_onlywater'), box)
df = writer_(df, onlyfiles, 12, str('dep_onlywater'), box)
df = writer_(df, onlyfiles, 13, str('ade_only'), box)
df = writer_(df, onlyfiles, 14, str('ade_only'), box)
df = writer_(df, onlyfiles, 15, str('ade_only'), box)
df = writer_(df, onlyfiles, 16, str('ade_only'), box)
df = writer_(df, onlyfiles, 17, str('dep_onlywater'), box)
df = writer_(df, onlyfiles, 18, str('dep_onlywater'), box)
df = writer_(df, onlyfiles, 19, str('ade_only'), box)
df = writer_(df, onlyfiles, 20, str('ade_only'), box)

df = writer_(df, onlyfiles, 21, str('ade_only'), box)
df = writer_(df, onlyfiles, 22, str('ade_only'), box)
df = writer_(df, onlyfiles, 23, str('dep_onlywater'), box)
df = writer_(df, onlyfiles, 24, str('dep_onlywater'), box)
df = writer_(df, onlyfiles, 25, str('ade_only'), box)
df = writer_(df, onlyfiles, 26, str('dep_onlywater'), box)
df = writer_(df, onlyfiles, 27, str('dep_onlywater'), box)
df = writer_(df, onlyfiles, 28, str('ade_quinine'), box)
df = writer_(df, onlyfiles, 29, str('ade_only'), box)
df = writer_(df, onlyfiles, 30, str('dep_onlywater'), box)

df = writer_(df, onlyfiles, 31, str('ade_quinine'), box)
df = writer_(df, onlyfiles, 32, str('ade_only'), box)
df = writer_(df, onlyfiles, 33, str('ade_only'), box)
df = writer_(df, onlyfiles, 34, str('dep_onlywater'), box)
df = writer_(df, onlyfiles, 35, str('ade_oxy'), box)

#df.to_csv(r'C:\Users\mehrd\Desktop\work\fun\run\drinkometer_df_w_1002_2_raw.csv', index=False, header=True)

df1 = pd.DataFrame(index=range(total_length), columns=['date', 'time', 'day_index', 'hour_index', 'animal', 'box',
                                                       'strain', 'state', 'oxytocin', 'quinine', 'water',
                                                       'alcohol-5%', 'alcohol-10%', 'alcohol-20%', 'locomotive'])
df1 = state_(df1, number_of_days)
df1 = day_and_hour_index(df1, number_of_days)

df1['animal'] = animal
df1['box'] = box
df1['strain'] = strain
df1['date'] = pd.date_range("2020-02-12", periods=total_length, freq="T").strftime('%Y-%m-%d')
df1['time'] = pd.date_range("2020-02-12", periods=total_length, freq="T").strftime('%H:%M:%S')

df1['quinine'] = df['quinine']
df1['oxytocin'] = df['oxytocin']
df1['state'] = df['state']


for hour in range(1, number_of_days * 24 + 1):
    df_extracted = df.loc[(df['hour_index'] == hour) & (df['water'].notnull())]
    list_ = np.array(df_extracted.water.index)
    if len(list_) > 1:
        for i in range(len(list_) - 1):
            temp_val = df.loc[list_[i + 1], 'water'] - df.loc[list_[i], 'water']
            if temp_val != 0.0:
                df1.loc[list_[i + 1], 'water'] = temp_val
    df_extracted = df.loc[(df['hour_index'] == hour) & (df['alcohol-5%'].notnull())]
    list_ = np.array(df_extracted.water.index)
    if len(list_) > 1:
        for i in range(len(list_) - 1):
            temp_val = df.loc[list_[i + 1], 'alcohol-5%'] - df.loc[list_[i], 'alcohol-5%']
            if temp_val != 0.0:
                df1.loc[list_[i + 1], 'alcohol-5%'] = temp_val
    df_extracted = df.loc[(df['hour_index'] == hour) & (df['alcohol-10%'].notnull())]
    list_ = np.array(df_extracted.water.index)
    if len(list_) > 1:
        for i in range(len(list_) - 1):
            temp_val = df.loc[list_[i + 1], 'alcohol-10%'] - df.loc[list_[i], 'alcohol-10%']
            if temp_val != 0.0:
                df1.loc[list_[i + 1], 'alcohol-10%'] = temp_val
    df_extracted = df.loc[(df['hour_index'] == hour) & (df['alcohol-20%'].notnull())]
    list_ = np.array(df_extracted.water.index)
    if len(list_) > 1:
        for i in range(len(list_) - 1):
            temp_val = df.loc[list_[i + 1], 'alcohol-20%'] - df.loc[list_[i], 'alcohol-20%']
            if temp_val != 0.0:
                df1.loc[list_[i + 1], 'alcohol-20%'] = temp_val


#df1.to_csv(r'C:\Users\mehrd\Desktop\work\fun\run\drinkometer_df_w_1002_2_consumption.csv', index=False, header=True)

threshold = 0.08
total_length_h = number_of_days * 24

df_h = pd.DataFrame(index=range(number_of_days * 24), columns=['date', 'time', 'day_index', 'hour_index', 'animal',
                                                               'box', 'strain', 'state', 'oxytocin', 'quinine',
                                                               'water', 'alcohol-5%', 'alcohol-10%', 'alcohol-20%', 'locomotive'])
df_h = m_day_and_hour_index(df_h, number_of_days)
df_h = state_hour(df_h, number_of_days)

df_h['animal'] = animal
df_h['box'] = box
df_h['strain'] = strain
df_h['date'] = pd.date_range("2020-02-12", periods=number_of_days * 24, freq="H").strftime('%Y-%m-%d')
df_h['time'] = pd.date_range("2020-02-12", periods=number_of_days * 24, freq="H").strftime('%H:%M:%S')

hours = sorted(set(np.array(df1.loc[(df1['quinine'] == str('applied'))].hour_index)))
for i in range(len(hours)):
    df_h.loc[hours[i]-1, 'quinine'] = str('applied')

hours = sorted(set(np.array(df1.loc[(df1['oxytocin'] == str('applied'))].hour_index)))
for i in range(len(hours)):
    df_h.loc[hours[i]-1, 'oxytocin'] = str('applied')


for hour in range(1, number_of_days*24+1):
    list_ = []
    ind = np.array(df_h.loc[(df_h['hour_index'] == hour)].index)
    df_extracted = df1.loc[(df1['hour_index'] == hour) & (df1['water'].notnull())]
    temp_arr = np.array(df_extracted['water'])
    if len(temp_arr[temp_arr > threshold]) > 1:
        df_h.loc[ind, 'water'] = np.nansum(temp_arr[temp_arr > threshold]) 

    list_ = []
    ind = np.array(df_h.loc[(df_h['hour_index'] == hour)].index)
    df_extracted = df1.loc[(df1['hour_index'] == hour) & (df1['alcohol-5%'].notnull())]
    temp_arr = np.array(df_extracted['alcohol-5%'])
    if len(temp_arr[temp_arr > threshold]) > 1:
        df_h.loc[ind, 'alcohol-5%'] = np.nansum(temp_arr[temp_arr > threshold])

    list_ = []
    ind = np.array(df_h.loc[(df_h['hour_index'] == hour)].index)
    df_extracted = df1.loc[(df1['hour_index'] == hour) & (df1['alcohol-10%'].notnull())]
    temp_arr = np.array(df_extracted['alcohol-10%'])
    if len(temp_arr[temp_arr > threshold]) > 1:
        df_h.loc[ind, 'alcohol-10%'] = np.nansum(temp_arr[temp_arr > threshold])

    list_ = []
    ind = np.array(df_h.loc[(df_h['hour_index'] == hour)].index)
    df_extracted = df1.loc[(df1['hour_index'] == hour) & (df1['alcohol-20%'].notnull())]
    temp_arr = np.array(df_extracted['alcohol-20%'])
    if len(temp_arr[temp_arr > threshold]) > 1:
        df_h.loc[ind, 'alcohol-20%'] = np.nansum(temp_arr[temp_arr > threshold])


#df_h.to_csv(r'C:\Users\mehrd\Desktop\work\fun\run\drinkometer_df_w_1002_2_hourly.csv', index=False, header=True)


df_d_light = pd.DataFrame(index=range(number_of_days), columns=['date', 'day_index', 'animal', 'box',
                                                                'strain', 'state', 'oxytocin', 'quinine', 'water',
                                                                'alcohol-5%', 'alcohol-10%', 'alcohol-20%', 'locomotive'])

df_d_dark = pd.DataFrame(index=range(number_of_days), columns=['date', 'day_index', 'animal', 'box',
                                                               'strain', 'state', 'oxytocin', 'quinine',
                                                               'water', 'alcohol-5%', 'alcohol-10%', 'alcohol-20%', 'locomotive'])

df_d_light = d_day_index(df_d_light, number_of_days)
df_d_dark = d_day_index(df_d_dark, number_of_days)

df_d_light['animal'] = animal
df_d_light['box'] = box
df_d_light['strain'] = strain
df_d_light['state'] = str('light')
df_d_light['date'] = pd.date_range("2020-02-12", periods=number_of_days, freq="D").strftime('%Y-%m-%d')

df_d_dark['animal'] = animal
df_d_dark['box'] = box
df_d_dark['strain'] = strain
df_d_dark['state'] = str('dark')
df_d_dark['date'] = pd.date_range("2020-02-12", periods=number_of_days, freq="D").strftime('%Y-%m-%d')


days = sorted(set(np.array(df1.loc[(df1['quinine'] == str('applied'))].day_index)))
for i in range(len(days)):
    df_d_dark.loc[days[i]-1, 'quinine'] = str('applied')
    df_d_light.loc[days[i]-1, 'quinine'] = str('applied')

days = sorted(set(np.array(df1.loc[(df1['oxytocin'] == str('applied'))].day_index)))
for i in range(len(days)):
    df_d_dark.loc[days[i]-1, 'oxytocin'] = str('applied')
    df_d_light.loc[days[i]-1, 'oxytocin'] = str('applied')


for day in range(1, number_of_days+1):
    list_ = []
    ind = np.array(df_d_light.loc[(df_d_light['day_index'] == day)].index)
    df_extracted = df1.loc[(df1['day_index'] == day) & (df1['state'] == str('light')) & (df1['water'].notnull())]
    temp_arr = np.array(df_extracted['water'])
    if len(temp_arr[temp_arr > threshold]) > 1:
        df_d_light.loc[ind, 'water'] = np.nansum(temp_arr[temp_arr > threshold])
    df_extracted = df1.loc[(df1['day_index'] == day) & (df1['state'] == str('dark')) & (df1['water'].notnull())]
    temp_arr = np.array(df_extracted['water'])
    if len(temp_arr[temp_arr > threshold]) > 1:
        df_d_dark.loc[ind, 'water'] = np.nansum(temp_arr[temp_arr > threshold])

    list_ = []

    df_extracted = df1.loc[(df1['day_index'] == day) & (df1['state'] == str('light')) & (df1['alcohol-5%'].notnull())]
    temp_arr = np.array(df_extracted['alcohol-5%'])
    if len(temp_arr[temp_arr > threshold]) > 1:
        df_d_light.loc[ind, 'alcohol-5%'] = np.nansum(temp_arr[temp_arr > threshold])
    df_extracted = df1.loc[(df1['day_index'] == day) & (df1['state'] == str('dark')) & (df1['alcohol-5%'].notnull())]
    temp_arr = np.array(df_extracted['alcohol-5%'])
    if len(temp_arr[temp_arr > threshold]) > 1:
        df_d_dark.loc[ind, 'alcohol-5%'] = np.nansum(temp_arr[temp_arr > threshold])

    list_ = []

    df_extracted = df1.loc[(df1['day_index'] == day) & (df1['state'] == str('light')) & (df1['alcohol-10%'].notnull())]
    temp_arr = np.array(df_extracted['alcohol-10%'])
    if len(temp_arr[temp_arr > threshold]) > 1:
        df_d_light.loc[ind, 'alcohol-10%'] = np.nansum(temp_arr[temp_arr > threshold])
    df_extracted = df1.loc[(df1['day_index'] == day) & (df1['state'] == str('dark')) & (df1['alcohol-10%'].notnull())]
    temp_arr = np.array(df_extracted['alcohol-10%'])
    if len(temp_arr[temp_arr > threshold]) > 1:
        df_d_dark.loc[ind, 'alcohol-10%'] = np.nansum(temp_arr[temp_arr > threshold])

    list_ = []

    df_extracted = df1.loc[(df1['day_index'] == day) & (df1['state'] == str('light')) & (df1['alcohol-20%'].notnull())]
    temp_arr = np.array(df_extracted['alcohol-20%'])
    if len(temp_arr[temp_arr > threshold]) > 1:
        df_d_light.loc[ind, 'alcohol-20%'] = np.nansum(temp_arr[temp_arr > threshold])
    df_extracted = df1.loc[(df1['day_index'] == day) & (df1['state'] == str('dark')) & (df1['alcohol-20%'].notnull())]
    temp_arr = np.array(df_extracted['alcohol-20%'])
    if len(temp_arr[temp_arr > threshold]) > 1:
        df_d_dark.loc[ind, 'alcohol-20%'] = np.nansum(temp_arr[temp_arr > threshold])


#df_d_dark.to_csv(r'C:\Users\mehrd\Desktop\work\fun\run\drinkometer_df_w_1002_2_daily_dark.csv', index=False, header=True)
#df_d_light.to_csv(r'C:\Users\mehrd\Desktop\work\fun\run\drinkometer_df_w_1002_2_daily_light.csv', index=False, header=True)


df.to_excel(r'C:\Users\mehrd\Desktop\work\fun\run\drinkometer_df_w_1003_3_raw.xlsx', index=False, header=True)
df1.to_excel(r'C:\Users\mehrd\Desktop\work\fun\run\drinkometer_df_w_1003_3_consumption.xlsx', index=False, header=True)
df_h.to_excel(r'C:\Users\mehrd\Desktop\work\fun\run\drinkometer_df_w_1003_3_hourly.xlsx', index=False, header=True)
df_d_dark.to_excel(r'C:\Users\mehrd\Desktop\work\fun\run\drinkometer_df_w_1003_3_daily_dark.xlsx', index=False, header=True)
df_d_light.to_excel(r'C:\Users\mehrd\Desktop\work\fun\run\drinkometer_df_w_1003_3_daily_light.xlsx', index=False, header=True)
