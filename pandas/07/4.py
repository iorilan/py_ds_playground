import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

titanic = pd.read_csv('train.csv')
def plot1():
    males = (titanic['Sex'] == 'male').sum()
    females = (titanic['Sex'] == 'female').sum()

    # put them into a list called proportions
    proportions = [males, females]

    # Create a pie chart
    plt.pie(
        # using proportions
        proportions,
        
        # with the labels being officer names
        labels = ['Males', 'Females'],
        
        # with no shadows
        shadow = False,
        
        # with colors
        colors = ['blue','red'],
        
        # with one slide exploded out
        explode = (0.15 , 0),
        
        # with the start angle at 90%
        startangle = 90,
        
        # with the percent listed as a fraction
        autopct = '%1.1f%%'
        )

    # View the plot drop above
    plt.axis('equal')

    # Set labels
    plt.title("Sex Proportion")

    # View the plot
    plt.tight_layout()
    plt.show()

def plot2():
    lm = sns.lmplot(x = 'Age', y = 'Fare', data = titanic, hue = 'Sex', fit_reg=False)

    # set title
    lm.set(title = 'Fare x Age')

    # get the axes object and tweak it
    axes = lm.axes
    axes[0,0].set_ylim(-5,)
    axes[0,0].set_xlim(-5,85)
    plt.show()

def plot3():
    df = titanic.Fare.sort_values(ascending = False)
    # create bins interval using numpy
    binsVal = np.arange(0,600,10)
    binsVal

    # create the plot
    plt.hist(df, bins = binsVal)

    # Set the title and labels
    plt.xlabel('Fare')
    plt.ylabel('Frequency')
    plt.title('Fare Payed Histrogram')

    # show the plot
    plt.show()
#plot1()
#plot2()
plot3()