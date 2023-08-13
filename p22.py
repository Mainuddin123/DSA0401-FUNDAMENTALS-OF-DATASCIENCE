import pandas as pd
import numpy as np
from scipy import stats

def calculate_confidence_interval(data, confidence_level):
    sample_mean = np.mean(data)
    sample_stddev = np.std(data, ddof=1)
    sample_size = len(data)
    z_critical = stats.norm.ppf((1 + confidence_level) / 2)
    margin_of_error = z_critical * (sample_stddev / np.sqrt(sample_size))
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
    return lower_bound, upper_bound

if __name__ == "__main__":
    confidence_level = 0.95  
    
    csv_path = r"C:\Users\mainu\Downloads\customer_reviews.csv"
    data = pd.read_csv(csv_path)
    
    product_ratings = data['rating']
    
    lower_bound, upper_bound = calculate_confidence_interval(product_ratings, confidence_level)
    
    sample_mean = np.mean(product_ratings)
    
    print("Sample Mean Rating:", sample_mean)
    print(f"Confidence Interval for Population Mean Rating (at {confidence_level:.0%} confidence level): ({lower_bound:.2f}, {upper_bound:.2f})")
