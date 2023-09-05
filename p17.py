import matplotlib.pyplot as plt
from collections import Counter
import string
import nltk
from nltk.corpus import stopwords

feedback_data = [
    "Great service and friendly staff!",
    "The product quality is excellent.",
    "I had a terrible experience with this company.",
    "Fast delivery but the product was damaged.",
    "The customer support team was helpful.",
    "Highly recommended for their professionalism.",
    "I will never buy from them again.",
]

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

feedback_tokens = [preprocess_text(feedback) for feedback in feedback_data]

all_words = [word for tokens in feedback_tokens for word in tokens]
word_freq = Counter(all_words)

N = int(input("Enter the number of top words to display: "))

top_words = word_freq.most_common(N)
print(f"Top {N} Most Frequent Words:")
for word, freq in top_words:
    print(f"{word}: {freq}")

top_words_df = pd.DataFrame(top_words, columns=['Word', 'Frequency'])
plt.figure(figsize=(10, 6))
plt.bar(top_words_df['Word'], top_words_df['Frequency'])
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title(f'Top {N} Most Frequent Words')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
