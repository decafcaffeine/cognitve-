import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.sequence import pad_sequences

# q1. text processing
print("--- q1. text processing ---")
paragraph = "i absolutely love artificial intelligence! it is changing the world rapidly. machine learning models are getting smarter every day. however, we must use them responsibly. what does the future hold?"

# 1. convert text to lowercase and remove punctuation using re
text_lower = paragraph.lower()
text_clean = re.sub(r'[^\w\s]', '', text_lower)
print("1. clean text:", text_clean)

# 2. tokenize into words and sentences
words = word_tokenize(text_clean)
sentences = sent_tokenize(text_lower)
print("\n2. sentences:", sentences)

# 3. compare split() and word_tokenize()
# word_tokenize handles punctuation better if we didn't remove it, but here both will look similar on clean text
py_split = text_clean.split()
print("\n3. python split:", py_split[:5])
print("   nltk tokenize:", words[:5])
print("   difference: split() just breaks by space. word_tokenize() can separate punctuation like 'it is' from 'it\\'s' if punctuation was present.")

# 4. remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = []
for w in words:
    if w not in stop_words:
        filtered_words.append(w)
print("\n4. without stopwords:", filtered_words)

# 5. word frequency distribution
freq_dist = nltk.FreqDist(filtered_words)
print("\n5. word frequency:")
for word, freq in freq_dist.items():
    print(f"{word}: {freq}")


# q2. stemming and lemmatization
print("\n--- q2. stemming and lemmatization ---")
# 1. extract all words with only alphabets
alpha_words = re.findall(r'\b[a-z]+\b', text_lower)

# 2. remove stop words
alpha_filtered = []
for w in alpha_words:
    if w not in stop_words:
        alpha_filtered.append(w)

# 3. perform stemming
porter = PorterStemmer()
stemmed_words = []
for w in alpha_filtered:
    stemmed_words.append(porter.stem(w))
print("3. stemmed:", stemmed_words)

# 4. perform lemmatization
lemma = WordNetLemmatizer()
lemmatized_words = []
for w in alpha_filtered:
    lemmatized_words.append(lemma.lemmatize(w))
print("4. lemmatized:", lemmatized_words)

# 5. compare outputs
print("\n5. comparison:")
print("stemmer cuts words roughly (e.g. 'responsibly' might become 'respons'). lemmatizer uses dictionary to find actual root words.")
print("i prefer lemmatization when i need real words for things like chatbots, and stemming for basic search engines where speed matters more.")


# q3. bag of words and tf-idf
print("\n--- q3. bag of words and tf-idf ---")
texts = [
    "this smartphone has a great camera and long battery life.",
    "the laptop screen is amazing but it gets too hot.",
    "i love these wireless headphones because the sound is clear."
]

# 1. countvectorizer (bag of words)
vectorizer_cv = CountVectorizer(stop_words='english')
bow = vectorizer_cv.fit_transform(texts)
print("1. bag of words features:", vectorizer_cv.get_feature_names_out())
print("   bow matrix:\n", bow.toarray())

# 2. tfidfvectorizer
vectorizer_tfidf = TfidfVectorizer(stop_words='english')
tfidf = vectorizer_tfidf.fit_transform(texts)
features = vectorizer_tfidf.get_feature_names_out()

# 3. top 3 keywords from each text
print("\n3. top 3 keywords per text using tf-idf:")
tfidf_array = tfidf.toarray()
for i, row in enumerate(tfidf_array):
    top_indices = row.argsort()[-3:][::-1]
    top_words = [features[idx] for idx in top_indices]
    print(f"text {i+1}: {top_words}")
print("interpretation: tf-idf gives higher scores to words that are unique to a specific sentence and ignores common words.")


# q4. similarity metrics
print("\n--- q4. similarity metrics ---")
text_ai = "artificial intelligence helps computers learn from large amounts of data to predict outcomes."
text_bc = "blockchain is a secure distributed ledger that stores data in connected blocks."

# 1. preprocess
words_ai = set(word_tokenize(re.sub(r'[^\w\s]', '', text_ai.lower())))
words_bc = set(word_tokenize(re.sub(r'[^\w\s]', '', text_bc.lower())))

# 2a. jaccard similarity
intersection = words_ai.intersection(words_bc)
union = words_ai.union(words_bc)
jaccard_sim = len(intersection) / len(union)
print(f"2a. jaccard similarity: {jaccard_sim:.4f}")

# 2b. cosine similarity
tfidf_sim = TfidfVectorizer().fit_transform([text_ai, text_bc])
cosine_sim = cosine_similarity(tfidf_sim[0], tfidf_sim[1])[0][0]
print(f"2b. cosine similarity: {cosine_sim:.4f}")

# 2c. analyze
print("2c. analysis: cosine similarity usually gives better insights for text because it looks at word frequencies and importance, while jaccard only looks at simple overlap.")


# q5. sentiment and word cloud
print("\n--- q5. sentiment and word cloud ---")
reviews = [
    "this phone is absolutely amazing and i love the fast processor!",
    "terrible experience, the battery dies in one hour.",
    "it is an average phone, nothing special but it works."
]

positive_text = ""

for i, rev in enumerate(reviews):
    # 1. textblob polarity and subjectivity
    blob = TextBlob(rev)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    # 2. classify
    if polarity > 0.1:
        label = "positive"
        positive_text += rev + " "
    elif polarity < -0.1:
        label = "negative"
    else:
        label = "neutral"
        
    print(f"review {i+1}: {label} (polarity: {polarity:.2f}, subjectivity: {subjectivity:.2f})")

# 3. create word cloud for positive reviews
# uncomment the last two lines to see the plot in colab/jupyter
print("\n3. generating word cloud for positive reviews...")
wordcloud = WordCloud(width=400, height=200, background_color='white').generate(positive_text)
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()


# q6. text generation
print("\n--- q6. text generation ---")
train_text = "deep learning is a subfield of artificial intelligence. it uses neural networks with many layers. these networks can learn patterns from massive amounts of data. we use deep learning for image recognition and self driving cars. the future of technology is very exciting."

# 1. tokenize
tokenizer = Tokenizer()
tokenizer.fit_on_texts([train_text])
total_words = len(tokenizer.word_index) + 1

# 2. create input sequences
input_sequences = []
token_list = tokenizer.texts_to_sequences([train_text])[0]
for i in range(1, len(token_list)):
    n_gram_sequence = token_list[:i+1]
    input_sequences.append(n_gram_sequence)

max_sequence_len = max([len(x) for x in input_sequences])
input_sequences = pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre')

x, y = input_sequences[:,:-1], input_sequences[:,-1]
y = to_categorical(y, num_classes=total_words)

# build simple model
model = Sequential()
model.add(Embedding(total_words, 10, input_length=max_sequence_len-1))
model.add(LSTM(50))
model.add(Dense(total_words, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

print("training model (this might take a few seconds)...")
# 3. train model (kept epochs low for quick execution)
model.fit(x, y, epochs=50, verbose=0)

# generate new text
seed_text = "deep learning"
next_words = 10

for _ in range(next_words):
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
    predicted_probs = model.predict(token_list, verbose=0)
    predicted_word_index = np.argmax(predicted_probs, axis=-1)[0]
    
    output_word = ""
    for word, index in tokenizer.word_index.items():
        if index == predicted_word_index:
            output_word = word
            break
    seed_text += " " + output_word

print("generated text:", seed_text)
