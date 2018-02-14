import pandas
from math import isnan, fabs
from numpy import mean, median, array, sort
import re
data = pandas.read_csv('titanic.csv', index_col='PassengerId')
#1st
sex = data['Sex'].value_counts()
print sex['male'], sex['female']

#2nd
surv = data['Survived'].value_counts()
proc = float(surv[1])/sum(surv)*100
print round(proc, 2)

#3rd
cls = data['Pclass'].value_counts()
f_cl = float(cls[1])/sum(cls)*100
print round(f_cl, 2)

#4th
age = array([d for d in data['Age'] if not isnan(d)])
age = sort(age) 
print round(mean(age), 2), median(age)

#5th
""""
x = data['SibSp']
y = data['Parch']
sx = sum(x)
sy = sum(y)
sxy = sum(x*y)
sx2 = sum(x*x)
sy2 = sum(y*y)
n = len(x)
r_xy = (n*sxy - sx*sy)/((fabs(n*sx2 - sx*sx) * fabs(n*sy2 - sy*sy)))**0.5
print round(r_xy, 2)
"""
print round(data['SibSp'].corr(data['Parch']), 2)

#6th
def func(name):
    n = re.search(".*\\((.*)\\).*", name)
    if n is not None:
        return n.group(1)
    n1 = re.search(".*\\. ([A-Za-z]*)", name)
    return n1.group(1)

names = data[data['Sex'] == 'female']['Name']
print names.map(lambda name: func(name)).value_counts().idxmax()