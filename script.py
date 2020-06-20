import pandas as pd

#create dataframe from excel file
df = pd.read_excel("/home/martin/Downloads/logs_BCS37_20181103 (2).xlsx", index_col=None, na_values=['NA'], usecols = 'A:G', sheet_name="logs_BCS37_20181103 (2)")

#parse Time column to datetime
df_dates = pd.to_datetime(df['Time'])

all_unique_dates = df_dates.map(pd.Timestamp.date).unique()


with open('test1','w') as f:
    for single_date in all_unique_dates:
        pattern = 'The user with id \'(.*?)\' viewed'
        #print(single_date)
        
        sub_frame = df[df['Time'].str.contains('{}/{}/{}'.format(single_date.day,single_date.month,single_date.year - 2000), regex=True)]
        sub_frame['Description'] = sub_frame['Description'].str.extract(pattern)
        #print(sub_frame)
        mylist = sub_frame["Description"].tolist()
        mylist = list(dict.fromkeys(mylist))
        cleanlist = [x for x in mylist if str(x) != 'nan']
        if cleanlist:
            #print(single_date)
            #print(cleanlist)
            
            for listitem in cleanlist:
                f.write('%s ' % listitem)
            f.write('\n')
            
    
