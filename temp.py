import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go


df=pd.read_csv('data.csv')
data=df['temp'].tolist()
def randomsetofmeans(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return(mean)
    
#sd=statistics.stdev(dataset)
#print(mean,sd)

standarddeviations=statistics.stdev(data)
#print(population_mean,standarddeviation)
def showfig(meanlist):
    df=meanlist
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],['temp'],show_hist=False)
#    fig.add_trace(go.scatter(x=[mean,mean],y=[0,1],mode='lines',name='mean'))
    fig.show()
def setup():
    meanlist=[]    
    for i in range(0,1000):
        setofmeans=randomsetofmeans(100)
        meanlist.append(setofmeans)
    showfig(meanlist)
    mean=statistics.mean(meanlist)
    print(mean) 
setup()       
population_mean=statistics.mean(data)
print(population_mean)
def standarddevitions():
      meanlist=[]    
      for i in range(0,1000):
        setofmeans=randomsetofmeans(100)
        meanlist.append(setofmeans)
      standarddeviation=statistics.stdev(meanlist)
      print(standarddeviation)
      standarddeviations()    