import numpy as np

student_scores=np.array([[85,90,78,92],[72,88,95,81],[91,87,89,76],[78,85,80,94]])

average_scores = np.mean(student_scores,axis=0)

highest_avg_subject_index = np.argmax(average_scores)

subject_names = ['Math', 'Science', 'English', 'History']

for i, subject in enumerate(subject_names):
    print(f"Average score for {subject}: {average_scores[i]}")

print(f"The subject with the highest average score is: {subject_names[highest_avg_subject_index]}")
