import pandas as pd
import numpy as np

data = {'이름' : ['a', 'b', 'c', 'd'], '나이': [25, 30, 35, 40], '성별':['여', '남', '여', '남']}

df=pd.DataFrame(data)

print(df.loc[0])

print(df.loc[1:2])

print(df[df['나이'] >= 30])
