import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def run():
    raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
            'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 
            'female': [0, 1, 1, 0, 1],
            'age': [42, 52, 36, 24, 73], 
            'preTestScore': [4, 24, 31, 2, 3],
            'postTestScore': [25, 94, 57, 62, 70]}

    df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'female', 'preTestScore', 'postTestScore'])
    #plt.scatter(df.preTestScore, df.postTestScore, s=df.age)
    plt.scatter(df.preTestScore, df.postTestScore, s= df.postTestScore * 4.5, c = df.female)

    #set labels and titles
    plt.title("preTestScore x postTestScore")
    plt.xlabel('preTestScore')
    plt.ylabel('preTestScore')
    plt.show()

run()
