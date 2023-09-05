import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.random.seed(0)
X = 2 * np.random.rand(100, 1)  
y = 3 + 4 * X + np.random.randn(100, 1)  


plt.scatter(X, y, alpha=0.7)
plt.xlabel('House Size')
plt.ylabel('House Price')
plt.title('Synthetic Data: House Size vs. House Price')
plt.show()


X_train, X_test, y_train, y_test = X[:80], X[80:], y[:80], y[80:]


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


plt.scatter(X_test, y_test, alpha=0.7)
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.xlabel('House Size')
plt.ylabel('House Price')
plt.title('Linear Regression: House Size vs. House Price')
plt.show()


from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')
