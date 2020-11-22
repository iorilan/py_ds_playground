import pandas as pd
import matplotlib.pyplot as plt

def desc():
    data =pd.read_csv('1.csv', index_col='CustomerId')
    print('-'*10)
    print(data.describe())
    print(data.shape)
    print(data.columns.tolist())
    print('-'*10)
    print(data.head())
    print('-'*10)
    print(data.tail())

def calc():
    data =pd.read_csv('1.csv', index_col='CustomerId')
    print('-'*10)
    print(data['Age'].max())
    print('-'*10)
    print(data['Age'].argmax())
    print('-'*10)
    print(data['Balance'].sum())
    print('-'*10)
    print(data['NumOfProducts'].value_counts())
    

def df_sel_row():
    data =pd.read_csv('1.csv', index_col='CustomerId')
    print('-'*10)
    print(data.loc[15647311]) # customer id == 15647311
    print('-'*10)
    print(data.iloc[3]) # the 4th row
    print('-'*10)
    print(data.iloc[1:3])

def df_add_row():
    df =pd.read_csv('1.csv')
        # 
        # 0,0000001,Hill,608,Spain,Female,41,1,83807.86,1,0,1,112542.58,0
    print(df.head(3))
    print('-'*10)
    new_row = pd.DataFrame({
        "RowNumber":0,"CustomerId":"11223344","Surname":"Frank","CreditScore":393,
        "Geography":"Germany","Gender":"Male","Age":56,"Tenure":0,"Balance":391023,
        "NumOfProducts":3,"HasCrCard":0,"IsActiveMember":1,"EstimatedSalary":38493.23,
        "Exited":0
    }, index=[0])
    df1=pd.concat([new_row, df]).reset_index(drop=True)

    print(df1.head(3))

def df_del_row():
    df =pd.read_csv('1.csv', index_col='CustomerId')
    print(df.head(3))
    print('-'*10)
    df.drop([15634602,15619304], inplace=True)
    print(df.head(3))

def plot():
    data =pd.read_csv('1.csv', index_col='CustomerId')
    ax = data['EstimatedSalary'].plot.hist(bins=20)
    ax.set_xlabel('EstimatedSalary')
    plt.show()


#desc()
#calc()
#df_sel_row()
#df_add_row()
#df_del_row()
plot()