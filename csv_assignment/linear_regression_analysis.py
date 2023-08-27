from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load CSV data
data = pd.read_csv('data.csv')

# Separate independent (X) and dependent (y) variables
X = data[['X']]
y = data['y']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Plot the original data and the regression line
plt.scatter(X, y, color='blue', label='Original Data')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.title('Linear Regression Analysis')
plt.show()

# Print the coefficient and intercept of the linear model
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
