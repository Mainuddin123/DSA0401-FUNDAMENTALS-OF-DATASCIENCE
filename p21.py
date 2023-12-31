import numpy as np
from scipy import stats

def calculate_confidence_interval(sample, confidence_level):
    sample_mean = np.mean(sample)
    sample_stddev = np.std(sample, ddof=1)
    z_critical = stats.norm.ppf((1 + confidence_level) / 2)
    margin_of_error = z_critical * (sample_stddev / np.sqrt(len(sample)))
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
    return lower_bound, upper_bound

def main():
    sample_size = int(input("Enter sample size: "))
    confidence_level = float(input("Enter confidence level (between 0 and 1): "))
    desired_precision = float(input("Enter desired level of precision: "))
    
    np.random.seed(42)  
    concentration_data = np.random.uniform(0.1, 0.5, size=100)
    
    sample = np.random.choice(concentration_data, size=sample_size, replace=False)
    
    lower_bound, upper_bound = calculate_confidence_interval(sample, confidence_level)
    
    sample_mean = np.mean(sample)
    
    print("Sample Mean:", sample_mean)
    print("Confidence Interval:", (lower_bound, upper_bound))

if __name__ == "__main__":
    main()
