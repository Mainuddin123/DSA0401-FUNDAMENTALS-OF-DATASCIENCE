import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split  # Add this import

# Generate synthetic data
np.random.seed(0)
n_samples = 100
engine_size = np.random.uniform(1.0, 5.0, n_samples)
horsepower = np.random.uniform(50, 300, n_samples)
fuel_efficiency = np.random.uniform(10, 40, n_samples)
car_prices = 5000 + 1000 * engine_size + 30 * horsepower - 20 * fuel_efficiency + np.random.normal(0, 500, n_samples)


data = pd.DataFrame({'EngineSize': engine_size, 'Horsepower': horsepower, 'FuelEfficiency': fuel_efficiency, 'Price': car_prices})


selected_features = ['EngineSize', 'Horsepower', 'FuelEfficiency']
X = data[selected_features] 
y = data['Price']            


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')


coefficients = pd.DataFrame({'Feature': selected_features, 'Coefficient': model.coef_})
print(coefficients)


plt.scatter(X_test['EngineSize'], y_test, alpha=0.7)
plt.plot(X_test['EngineSize'], y_pred, color='red', linewidth=2)
plt.xlabel('Engine Size')
plt.ylabel('Car Price')
plt.title('Linear Regression: Engine Size vs. Car Price')
plt.show()
