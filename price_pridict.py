import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
# 读取数据
data = pd.read_csv('./data/data1.csv')
X = data.drop(["price"], axis=1)
y = data['price']
# 分割数据集
x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.25)
#数据标准化处理 归一化
ss_x = StandardScaler()
x_train = ss_x.fit_transform(x_train)
x_test = ss_x.fit_transform(x_test)

# 调参
param_grid = [
    {
        'weights': ['uniform'],
        'n_neighbors': [i for i in range(1, 12)]

    },
    {
        'weights': ['distance'],
        'n_neighbors': [i for i in range(1, 12)],
        'p': [i for i in range(1, 6)]
    }
]
# 建立模型及训练
knnrgr = KNeighborsRegressor()
grid_search = GridSearchCV(knnrgr, param_grid)
grid_search.fit(x_train, y_train)
def Knn_predict(data):
    print(data)
    ss = StandardScaler()
    ss.fit(x_train)
    data = ss.transform(data)
    print(data)
    predict_values = grid_search.predict(data)
    return predict_values
d1 = pd.DataFrame(np.array([[233, 2005, 3, 1,3,1,0,1,1,1500,25]]),
                        columns=['area', 'buildtime', 'room_num','hall_num','floor','dire','exemption of business tax',
                                 'exemption of double tax','quality education','distance','loc'])
d2 = pd.DataFrame(np.array([[122, 2005, 3, 1,3,1,0,1,1,1500,1]]),
                        columns=['area', 'buildtime', 'room_num','hall_num','floor','dire','exemption of business tax',
                                 'exemption of double tax','quality education','distance','loc'])
print(Knn_predict(d1)) # for test
print('---------------------------------')
print(Knn_predict(d2))
print('----------------------------------')
print(grid_search.predict(x_test))
