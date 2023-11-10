import pandas
import numpy

my_index = numpy.array([1, 2, 3])
data = ['a', 'b', 'c']
my_series = pandas.Series(data, index=my_index)
print(my_series)

import pandas as pd

data = pd.Series([10, 20, 30, 40, 50])

print(data)

data = {
    '이름': ['Alice', 'Bob', 'charlie', 'David'],
    '나이': [25, 30, 35, 28],
    '성별': ['여', '남', '남', '여']
}
my_index = ['one', 'two', 'three', 'four']
df = pd.DataFrame(data, index=my_index,)

print(df)

import pandas as pd
import numpy
my_index = ['one', 'two', 'three', 'four']
my_columns = ['이름', '나이', '성별']
my_data = numpy.array([['Alice', 'Bob', 'charlie', 'David'],
                        [25, 30, 35, 28], ['여', '남', '남', '여']]).transpose()
df = pd.DataFrame(data, index=my_index, columns=my_columns)

print(df)

import pandas as pd

dir = "./data/"
filename = "08_pima-indians-diabetes.data.csv"
filepath = dir + filename

data_columns = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi','age','class']
data = pd.read_csv(filepath, names=data_columns)

print(data.head(5))

df = pd.read_csv("./data/08_pima-indians-diabetes.data.csv")
