import pandas as pd
from sklearn.linear_model import LinearRegression


data = {
    'x': [10, 12, 16, 11, 15, 14, 20, 22],
    'y': [15, 18, 23, 14, 20, 17, 25, 28]
}


df = pd.DataFrame(data)


df['x^2'] = df['x'] ** 2
df['y^2'] = df['y'] ** 2
df['x*y'] = df['x'] * df['y']


df.to_excel('data.xlsx', index=False)


data = pd.read_excel('data.xlsx')

x = data['x'].values.reshape(-1, 1)
y = data['y'].values.reshape(-1, 1)


regression_x_on_y = LinearRegression()
regression_x_on_y.fit(y, x)
slope_x_on_y = regression_x_on_y.coef_[0][0]
intercept_x_on_y = regression_x_on_y.intercept_[0]


regression_y_on_x = LinearRegression()
regression_y_on_x.fit(x, y)
slope_y_on_x = regression_y_on_x.coef_[0][0]
intercept_y_on_x = regression_y_on_x.intercept_[0]


print(f"Regression equation of x on y: x = {slope_x_on_y:.4f} * y + {intercept_x_on_y:.4f}")
print(f"Regression equation of y on x: y = {slope_y_on_x:.4f} * x + {intercept_y_on_x:.4f}")