import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#정확한 선을 따라서 그래프
def f(size):
    x = np.linspace(0, 5, size)#0과 5사이에서 size만큼의 숫자를 생성
    y = x + np.sin(x**2) + 1
    return (x,y)

#해당 그래프에서 랜덤숫자를 더해줌으로써 샘플 데이터를 생성
def sample(size):
    x = np.linspace(0, 5, size)
    y = x + np.sin(x**2) + 1 + np.random.randn(x.size)*0.5
    return (x, y)

#샘플데이터 확인
x,y = sample(1000)
plt.scatter(x,y,s=3,c='black')

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
x = x.reshape(-1,1)
y = y.reshape(-1,1)
lr.fit(x,y)

f_x, f_y = f(1000)
plt.plot(f_x, f_y)
plt.scatter(x.flatten(), y.flatten(), s=3, c='black')
plt.plot(x.flatten(), lr.predict(x).flatten())#여기서 주황색으로 표시되는 내용은 1차 선형 회귀분석 결과

#polynominal regression 적용
from sklearn.preprocessing import PolynomialFeatures

poly_features = PolynomialFeatures(degree = 2)
x_poly = poly_features.fit_transform(x)
x_poly[:10]

lr = LinearRegression()
lr.fit(x_poly, y)

f_x, f_y = f(1000)
plt.plot(f_x, f_y)
plt.scatter(x.flatten(), y.flatten(), s=3, c='black')
plt.plot(x.flatten(), lr.predict(x_poly).flatten())#여기서 주황색으로 표시되는 내용은 2차 폴리노미널 회귀분석 결과를 보여줌

#가장 좋은 모델은 무엇일지... rmse 최소화 시키는 모델로 찾아봄

#rmse 를 구하는 함수 def
def rmse(predictions, targets):
    return np.sqrt(((predictions - targets)**2).mean())

#10차부터 50차 까지 시도
poly_range = list(range(10,50))
rmse_lr_list = []
rmse_lasso_list = []
rmse_ridge_list = []

from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

for poly_value in poly_range:
    poly_features = PolynomialFeatures(degree = poly_value)
    x_poly = poly_features.fit_transform(x)
    lr = LinearRegression()
    lr.fit(x_poly, y)

    rmse_lr_list.append(rmse(lr.predict(x_poly),y))

    lasso = Lasso()
    lasso.fit(x_poly, y)
    rmse_lasso_list.append(rmse(lasso.predict(x_poly), y))

    ridge = Ridge()
    ridge.fit(x_poly, y)
    rmse_ridge_list.append(rmse(ridge.predict(x_poly),y))



import pandas as pd
from pandas import DataFrame

data = {"poly_range":poly_range, "lr_rmse": rmse_lr_list,
        "lasso_rmse": rmse_lasso_list, "ridge_rmse": rmse_ridge_list}

df = DataFrame(data).set_index("poly_range")

df.min()

df["ridge_rmse"].sort_values().head()

poly_features = PolynomialFeatures(degree=22)
x_poly = poly_features.fit_transform(x)
ridge = Ridge(fit_intercept = False)
ridge.fit(x_poly, y)

f_x, f_y = f(1000)
plt.plot(f_x, f_y)
plt.scatter(x.flatten(), y.flatten(), s=3, c='black')
plt.plot(x.flatten(), ridge.predict(x_poly).flatten())#여기서 주황색으로 표시되는 내용은 22차 polynominal regression 값을 보여줌
