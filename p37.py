import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(0)
study_time = np.random.randint(1, 10, 50)
exam_scores = 50 + 5 * study_time + np.random.normal(0, 5, 50)

data = pd.DataFrame({
    'Study_Time (hours)': study_time,
    'Exam_Scores': exam_scores
})

plt.figure(figsize=(8, 6))
plt.scatter(data['Study_Time (hours)'], data['Exam_Scores'], c='blue', marker='o')
plt.title('Scatter Plot of Study Time vs. Exam Scores')
plt.xlabel('Study Time (hours)')
plt.ylabel('Exam Scores')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(data['Study_Time (hours)'], data['Exam_Scores'], c='green', marker='o', linestyle='-')
plt.title('Line Plot of Study Time vs. Exam Scores')
plt.xlabel('Study Time (hours)')
plt.ylabel('Exam Scores')
plt.grid(True)
plt.show()

correlation = data['Study_Time (hours)'].corr(data['Exam_Scores'])
print(f'Correlation between Study Time and Exam Scores: {correlation:.2f}')
