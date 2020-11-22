import pandas as pd 
def cat():
    data1 = {
            'Name':['Frank','Leo','Issac','Dav','Frank','Issac'],
            'Mark':[39,41,95,21,14,99],
            'Age':[12,14,15,11,12,14],
            'Class':[1,1,2,2,1,2]
            }
    data2 = {
            'Name':['Issac','Dav'],
            'Mark':[98,91],
            'Age':[12,11],
            'Class':[1,2]
            }
    df1 = pd.DataFrame(data1, index=[0,1,2,3,4,5])
    df2 = pd.DataFrame(data2, index=[2,3])
    print(pd.concat([df1, df2]))

    print('-'*10)
    print(df1.append(df2))

    print('-'*10)
    print(pd.concat([df1, df2], ignore_index=True))

def cat_join():
    data1 = {
            'Name':['Frank','Leo','Issac','Dav','Frank','Issac'],
            'Mark':[39,41,95,21,14,99],
            'Age':[12,14,15,11,12,14],
            'Class':[1,1,2,2,1,2]
            }
    data2 = {
        'Name':['Frank','Tim','Philip'],
        'Year':[2001,2002,2002]
    }
    df1 = pd.DataFrame(data1, index=[0,1,2,3,4,5])
    df2 = pd.DataFrame(data2, index=[0,6,7])
    print(pd.concat([df1, df2], axis=1, join='inner', sort=True))
    print(pd.concat([df1, df2], axis=1, join='outer', sort=True))

def cat_ser():
    data1 = {
            'Name':['Frank','Leo','Issac','Dav','Frank','Issac'],
            'Mark':[39,41,95,21,14,99],
            'Age':[12,14,15,11,12,14],
            'Class':[1,1,2,2,1,2]
            }
    df = pd.DataFrame(data1, index=[0,1,2,3,4,5])
    s1 = pd.Series([2001,2002,2002,2000,2002,1999], name='Year')
    print(pd.concat([df, s1], axis=1))

def merge():
    data1 = {
            'Name':['Frank','Leo','Issac','Dav','Iori','Potter'],
            'Mark':[39,41,95,21,14,99],
            'Age':[12,14,15,11,12,14],
            'Class':[1,1,2,2,1,2]
            }
    data2 = {
        'Name':['Frank','Paul','Gauss','Issac'],
        'Year':[2000,1999,2001,2002]
    }
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)

    # print('-'*10)
    # print(pd.merge(df1,df2,how='left', on=['Name']))
    # print('-'*10)
    # print(pd.merge(df1,df2,how='right', on=['Name']))
    # print('-'*10)
    # print(pd.merge(df1,df2,how='inner', on=['Name']))
    # print('-'*10)
    # print(pd.merge(df1,df2,how='outer', on=['Name']))
    print('-'*10)
    df3 = pd.DataFrame(data1, index=[0,1,2,3,5,6])
    df4 = pd.DataFrame(data2, index=[0,4,7,8])
    print(df3.join(df4, lsuffix='_left', rsuffix='_right', how='inner'))
    print(df3.join(df4, lsuffix='_left', rsuffix='_right', how='outer'))

#cat()
#cat_join()   
#cat_ser()
merge()