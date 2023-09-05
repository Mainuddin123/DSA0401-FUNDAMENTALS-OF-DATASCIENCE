import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


np.random.seed(0)
n_samples = 1000
n_features = 5

X = np.random.rand(n_samples, n_features)  
y = np.random.choice(['Good', 'Bad'], size=n_samples)  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


k = 3  
knn_classifier = KNeighborsClassifier(n_neighbors=k)


knn_classifier.fit(X_train, y_train)


y_pred = knn_classifier.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='binary', pos_label='Good')
recall = recall_score(y_test, y_pred, average='binary', pos_label='Good')
f1 = f1_score(y_test, y_pred, average='binary', pos_label='Good')


print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')
