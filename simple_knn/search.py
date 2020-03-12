import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


data = pd.read_excel('C:/Users/18263/Desktop/Information.xlsx')
# print(data)
info_Y = data['normal']
x = [0, 5, 8]
info_X = data.drop(data.columns[x],axis=1)
# print(info_X)
X_train,X_test,y_train,y_test = train_test_split(
    info_X, info_Y, test_size=0.3)
# print(y_train)

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
# print(knn.predict(X_test))
y_pre = knn.predict(X_test)
mse = mean_squared_error(y_test, y_pre)
print(mse)

