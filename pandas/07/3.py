import pandas as pd

# visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

# set seaborn style 
sns.set_style("dark")
    
def load_data():
    tips = pd.read_csv('tips.csv')
    return tips

def plot1():
    load_data()
    ttbill = sns.distplot(tips.total_bill)
    # set lables and titles
    ttbill.set(xlabel = 'Value', ylabel = 'Frequency', title = "Total Bill")
    # take out the right and upper borders
    sns.despine()
    plt.show()

def plot2():
    tips=load_data()
    sns.jointplot(x ="total_bill", y ="tip", data = tips)
    plt.show()

def plot3():
    tips=load_data()
    sns.pairplot(tips)
    plt.show()

def plot4():
    tips=load_data()
    sns.stripplot(x = "day", y = "total_bill", data = tips, jitter = True)
    plt.show()

def plot5():
    tips=load_data()
    sns.stripplot(x = "tip", y = "day", hue = "sex", data = tips, jitter = True)
    plt.show()

def plot6():
    tips=load_data()
    sns.boxplot(x = "day", y = "total_bill", hue = "time", data = tips)
    plt.show()

def plot7():
    tips=load_data()
    sns.set(style = "ticks")

    # creates FacetGrid
    g = sns.FacetGrid(tips, col = "time")
    g.map(plt.hist, "tip")
    plt.show()

def plot8():
    tips=load_data()
    g = sns.FacetGrid(tips, col = "sex", hue = "smoker")
    g.map(plt.scatter, "total_bill", "tip", alpha =.7)

    g.add_legend()
    plt.show()
#plot1()
#plot2()
#plot3()
#plot4()
#plot5()
#plot6()
#plot7()
plot8()