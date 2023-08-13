import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

np.random.seed(42)
control_group = np.random.normal(loc=50, scale=10, size=100)
treatment_group = np.random.normal(loc=55, scale=10, size=100)

t_stat, p_value = stats.ttest_ind(control_group, treatment_group, equal_var=False)

print("t-statistic:", t_stat)
print("p-value:", p_value)

plt.figure(figsize=(10, 6))
plt.hist(control_group, alpha=0.5, label='Control Group (Placebo)')
plt.hist(treatment_group, alpha=0.5, label='Treatment Group (New Drug)')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Distribution of Data in Control and Treatment Groups')
plt.legend()
plt.show()
