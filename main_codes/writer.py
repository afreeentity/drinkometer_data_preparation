import numpy as np
import pandas as pd
import scipy as sc



def loco_writer2020(animal, dataframe, path):
    if animal == 1:
        file_skipped = pd.read_excel(
            "{}/loco/01/1 25.03 from 2000.Jan.03  00-52-32 to 2000.Feb.14  18-42-32 -- 1.xlsx".format(path),
            skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/01/1 from 2020.Mrz.25  13-21-39 to 2020.Mai.17  05-46-39 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/01/1 from 2020.Mai.19  14-19-16 to 2020.Jul.20  01-54-16 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/01/1 from 2020.Jul.22  13-10-11 to 2020.Sep.25  17-55-11 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/01/1 from 2020.Sep.30  14-52-56 to 2020.Nov.13  05-17-56 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 2):
        file_skipped = pd.read_excel(
            "{}/loco/02/2 from 2020.Feb.17  13-24-00 to 2020.Mrz.03  01-54-00 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/02/2 from 2020.Aug.17  09-59-23 to 2020.Sep.24  07-54-23 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/02/2 from 2020.Sep.30  14-53-19 to 2020.Okt.02  11-13-19 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 3):
        file_skipped = pd.read_excel(
            "{}/loco/03/3 from 2020.Feb.05  14-42-39 to 2020.Mai.27  11-32-39 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/03/3 from 2020.Jun.04  14-22-29 to 2020.Sep.26  08-17-29 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/03/3 from 2020.Sep.30  14-53-47 to 2020.Nov.18  19-03-47 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 4):
        file_skipped = pd.read_excel(
            "{}/loco/04/4 04.06 from 2000.Jan.03  00-50-54 to 2000.Apr.12  20-40-54 -- 1.xlsx".format(path),
            skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/04/4 from 2020.Jun.04  14-22-51 to 2020.Sep.26  08-17-51 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/04/4 from 2020.Sep.30  14-54-05 to 2020.Nov.18  19-04-05 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 5):
        file_skipped = pd.read_excel(
            "{}/loco/05/5 from 2020.Feb.05  14-42-42 to 2020.Apr.03  10-32-42 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/05/5 from 2020.Apr.15  15-54-52 to 2020.Jul.25  20-19-52 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/05/5 from 2020.Jul.30  09-42-19 to 2020.Nov.18  19-02-19 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 6):
        file_skipped = pd.read_excel(
            "{}/loco/06/6 from 2020.Feb.05  14-42-39 to 2020.Mai.29  08-37-39 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/06/6 from 2020.Jun.04  14-23-14 to 2020.Sep.17  20-03-14 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/06/6 from 2020.Sep.23  11-56-34 to 2020.Nov.18  19-01-34 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 8):
        file_skipped = pd.read_excel(
            "{}/loco/08/8 from 2020.Feb.05  14-42-50 to 2020.Apr.20  13-02-50 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/08/8 from 2020.Apr.21  14-03-12 to 2020.Aug.13  07-58-12 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/08/8 from 2020.Aug.17  09-59-46 to 2020.Nov.16  11-54-46 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 9):
        file_skipped = pd.read_excel(
            "{}/loco/09/9 from 2020.Feb.05  14-42-37 to 2020.Mrz.09  22-22-37 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/09/9 from 2020.Mai.19  14-18-57 to 2020.Jun.26  11-03-57 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/09/9 from 2020.Jun.29  10-19-28 to 2020.Okt.10  16-04-28 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/09/9 from 2020.Mrz.18  10-48-09 to 2020.Mai.18  17-18-09 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/09/9 from 2020.Okt.14  11-11-25 to 2020.Nov.18  18-56-25 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 10):
        file_skipped = pd.read_excel(
            "{}/loco/10/10 from 2020.Feb.05  14-42-45 to 2020.Mai.04  03-37-45 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/10/10 from 2020.Aug.11  17-00-25 to 2020.Aug.25  12-25-25 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/10/10 from 2020.Aug.31  11-35-38 to 2020.Nov.18  19-00-38 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/10/10 from 2020.Mai.06  14-57-14 to 2020.Aug.04  01-12-14 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity


    elif (animal == 11):
        file_skipped = pd.read_excel(
            "{}/loco/11/11 from 2020.Feb.05  14-43-04 to 2020.Mai.18  06-33-04 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/11/11 from 2020.Mai.19  14-18-39 to 2020.Jul.12  07-13-39 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/11/11 from 2020.Jul.22  13-10-30 to 2020.Nov.13  07-05-30 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 12):
        file_skipped = pd.read_excel(
            "{}/loco/12/12 from 2020.Feb.05  14-43-09 to 2020.Mai.05  17-33-09 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/12/12 from 2020.Jun.09  14-34-13 to 2020.Okt.01  08-29-13 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 13):
        file_skipped = pd.read_excel(
            "{}/loco/13/13 from 2020.Feb.05  14-43-05 to 2020.Mai.05  23-18-05 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/13/13 from 2020.Mai.06  14-57-32 to 2020.Mai.26  15-42-32 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/13/13 from 2020.Jun.04  14-23-31 to 2020.Aug.01  11-28-31 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/13/13 from 2020.Aug.11  17-00-43 to 2020.Nov.18  19-00-43 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 14):
        file_skipped = pd.read_excel(
            "{}/loco/14/14 from 2020.Feb.05  14-43-15 to 2020.Mai.06  03-38-15 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/14/14 Sw-7 - from 2020.Aug.12  10-08-25 to 2020.Nov.03  16-43-25 -- 1.xlsx".format(path),
            skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/14/14 Sw-7 - from 2020.Nov.05  16-41-53 to 2020.Nov.18  17-56-53 -- 1.xlsx".format(path),
            skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 15):
        file_skipped = pd.read_excel(
            "{}/loco/15/15 25.03 from 2000.Jan.03  00-50-15 to 2000.Feb.19  15-40-15 -- 1.xlsx".format(path),
            skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/15/15 from 2020.Mrz.25  13-21-06 to 2020.Jun.09  12-11-06 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/15/15 from 2020.Jun.09  14-34-34 to 2020.Jul.24  00-49-34 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/15/15 from 2020.Aug.04  09-54-00 to 2020.Nov.18  19-14-00 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 17):
        file_skipped = pd.read_excel(
            "{}/loco/17/17 from 2020.Feb.05  14-43-28 to 2020.Mai.04  06-03-28 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/17/17 from 2020.Mai.06  14-58-14 to 2020.Aug.28  08-53-14 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/17/17 from 2020.Sep.02  11-50-53 to 2020.Nov.18  19-10-53 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 18):
        file_skipped = pd.read_excel(
            "{}/loco/18/18 from 2020.Feb.05  14-43-17 to 2020.Mai.03  02-38-17 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/18/18 from 2020.Mai.06  14-58-34 to 2020.Mai.18  02-03-34 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/18/18 from 2020.Jun.01  11-18-03 to 2020.Sep.23  05-13-03 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/18/18 from 2020.Sep.30  14-54-25 to 2020.Nov.18  19-04-25 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 19):
        file_skipped = pd.read_excel(
            "{}/loco/19/19 from 2020.Feb.17  13-22-51 to 2020.Mai.21  18-32-51 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/19/19 from 2020.Jun.04  14-23-52 to 2020.Sep.24  15-03-52 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/19/19 from 2020.Sep.30  14-54-41 to 2020.Nov.18  19-04-41 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 20):
        file_skipped = pd.read_excel(
            "{}/loco/20/20 19.05 from 2000.Jan.03  00-48-52 to 2000.Apr.06  23-48-52 -- 1.xlsx".format(path),
            skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/20/20 from 2020.Mai.19  14-19-46 to 2020.Sep.10  08-14-46 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/20/20 from 2020.Sep.30  14-54-59 to 2020.Nov.18  18-59-59 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 21):
        file_skipped = pd.read_excel(
            "{}/loco/21/21 from 2020.Feb.05  14-43-18 to 2020.Mai.12  14-53-18 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/21/21 from 2020.Mai.19  14-20-11 to 2020.Sep.07  23-55-11 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/21/21 from 2020.Sep.14  13-47-21 to 2020.Nov.18  18-57-21 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 22):
        file_skipped = pd.read_excel(
            "{}/loco/22/22 from 2020.Aug.17  10-03-58 to 2020.Nov.11  22-28-58 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 23):
        file_skipped = pd.read_excel(
            "{}/loco/23/23 06.05 from 2000.Jan.03  00-45-00 to 2000.Mrz.22  08-45-00 -- 1.xlsx".format(path),
            skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/23/23 from 2020.Mai.06  14-59-11 to 2020.Jul.14  15-24-11 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/23/23 from 2020.Aug.04  10-31-07 to 2020.Nov.14  23-11-07 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 24):
        file_skipped = pd.read_excel(
            "{}/loco/24/24 from 2020.Feb.10  12-05-42 to 2020.Jun.03  06-00-42 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/24/24 from 2020.Jun.04  14-24-11 to 2020.Sep.10  18-34-11 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/24/24 from 2020.Sep.30  14-55-15 to 2020.Nov.18  19-05-15 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 25):
        file_skipped = pd.read_excel(
            "{}/loco/25/25 from 2020.Feb.05  14-43-59 to 2020.Apr.18  22-03-59 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/25/25 from 2020.Apr.21  14-03-37 to 2020.Aug.10  02-23-37 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/25/25 from 2020.Aug.11  17-01-04 to 2020.Nov.18  19-11-04 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 26):
        file_skipped = pd.read_excel(
            "{}/loco/26/26 from 2020.Feb.05  14-43-47 to 2020.Mai.22  12-13-47 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/26/26 from 2020.Jun.01  11-18-24 to 2020.Sep.23  05-13-24 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/26/26 from 2020.Sep.30  14-55-31 to 2020.Nov.18  19-00-31 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 27):
        file_skipped = pd.read_excel(
            "{}/loco/27/27 from 2020.Feb.05  14-43-49 to 2020.Mai.08  02-33-49 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/27/27 from 2020.Mai.14  11-50-42 to 2020.Sep.05  05-45-42 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/27/27 from 2020.Sep.30  14-55-45 to 2020.Nov.18  19-00-45 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 28):
        file_skipped = pd.read_excel(
            "{}/loco/28/28 from 2020.Apr.15  15-54-39 to 2020.Apr.28  12-44-39 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/28/28 from 2020.Aug.11  17-01-20 to 2020.Aug.26  00-11-20 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/28/28 from 2020.Aug.31  11-35-54 to 2020.Sep.14  10-50-54 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/28/28 from 2020.Jul.01  12-06-41 to 2020.Jul.15  19-01-41 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/28/28 from 2020.Jul.22  13-10-53 to 2020.Aug.03  09-50-53 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/28/28 from 2020.Jun.01  11-18-40 to 2020.Jun.17  03-43-40 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/28/28 from 2020.Mrz.05  15-00-42 to 2020.Mrz.19  09-20-42 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/28/28 from 2020.Mrz.25  13-21-23 to 2020.Apr.10  16-46-23 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/28/28 from 2020.Okt.22  14-15-16 to 2020.Nov.05  06-45-16 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/28/28 from 2020.Sep.23  11-56-54 to 2020.Okt.07  15-16-54 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 29):
        file_skipped = pd.read_excel(
            "{}/loco/29/29 from 2020.Feb.10  12-06-08 to 2020.Mai.31  09-26-08 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/29/29 from 2020.Jun.04  14-24-31 to 2020.Sep.25  20-19-31 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/29/29 from 2020.Sep.30  14-55-58 to 2020.Nov.18  19-00-58 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 30):
        file_skipped = pd.read_excel(
            "{}/loco/30/30 from 2020.Feb.10  12-06-17 to 2020.Mai.29  22-56-17 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/30/30 from 2020.Jun.04  14-24-45 to 2020.Aug.11  16-54-45 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 31):
        file_skipped = pd.read_excel(
            "{}/loco/31/31 from 2020.Feb.10  12-06-41 to 2020.Mai.26  00-31-41 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/31/31 from 2020.Jun.04  14-25-02 to 2020.Sep.26  08-20-02 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/31/31 from 2020.Sep.30  14-56-09 to 2020.Nov.18  19-01-09 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    elif (animal == 32):
        file_skipped = pd.read_excel(
            "{}/loco/32/32 from 2020.Feb.17  13-24-14 to 2020.Mai.22  02-44-14 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('{}-%m-%d'.format(str(2020)))
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/32/32 from 2020.Jun.04  14-25-16 to 2020.Sep.15  21-00-16 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

        file_skipped = pd.read_excel(
            "{}/loco/32/32 from 2020.Sep.22  10-16-38 to 2020.Nov.18  19-01-38 -- 1.xlsx".format(path), skiprows=18)
        reform_length = len(file_skipped)
        for index_ref in range(reform_length):
            lf_date = file_skipped['Date, Time'][index_ref].strftime('%Y-%m-%d')
            lf_time = file_skipped['Date, Time'][index_ref].strftime('%H:%M:{}'.format(str('00')))
            lf_activity = file_skipped['Activity (detection(s))'][index_ref]
            index_value = dataframe[(dataframe['date'] == lf_date) & (dataframe['time'] == lf_time)].index
            dataframe.loc[index_value, 'locomotive'] = lf_activity

    return (dataframe)