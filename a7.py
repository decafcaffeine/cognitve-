import re
import nltk
import pandas as pd
from collections import Counter
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, LancasterStemmer, RegexpStemmer, WordNetLemmatizer
from nltk.corpus import stopwords, wordnet
from nltk.util import ngrams

# q1. preprocessing
print("--- q1. preprocessing ---")
ticket_numbers = []
sent_counts = []
token_counts = []
punct_counts = []
stop_counts = []
unique_counts = []
final_counts = []

all_tokens = []
all_final_tokens = []
all_no_punct = []

stop_words = set(stopwords.words('english'))

for i in range(len(tickets)):
    text = tickets[i]
    
    sentences = sent_tokenize(text)
    sent_counts.append(len(sentences))
    
    tokens = word_tokenize(text)
    token_counts.append(len(tokens))
    all_tokens.extend(tokens)
    
    punct_tokens = []
    for word in tokens:
        if word.isalnum() == False:
            punct_tokens.append(word)
    punct_counts.append(len(punct_tokens))
    
    stop_tokens = []
    for word in tokens:
        if word.lower() in stop_words:
            stop_tokens.append(word)
    stop_counts.append(len(stop_tokens))
    
    unique_tokens = set(tokens)
    unique_counts.append(len(unique_tokens))
    
    final_tokens = []
    for word in tokens:
        if word.isalnum() == True and word.lower() not in stop_words:
            final_tokens.append(word)
            all_final_tokens.append(word)
    final_counts.append(len(final_tokens))
    
    for word in tokens:
        if word.isalnum() == True:
            all_no_punct.append(word)
            
    ticket_numbers.append(i + 1)

df = pd.DataFrame({
    'ticket': ticket_numbers,
    'sentences': sent_counts,
    'tokens': token_counts,
    'punctuation': punct_counts,
    'stopwords': stop_counts,
    'unique_tokens': unique_counts,
    'final_tokens': final_counts
})

df.loc['total'] = df.sum(numeric_only=True)
df.at['total', 'ticket'] = 'total'
print(df.to_string(index=False))

print("\ndetails for ticket 1:")
sample_tokens = word_tokenize(tickets[0])
print("actual tokens:", sample_tokens[:10])
print("punctuation:", [w for w in sample_tokens if not w.isalnum()][:10])
print("stopwords:", [w for w in sample_tokens if w.lower() in stop_words][:10])
print("final tokens:", [w for w in sample_tokens if w.isalnum() and w.lower() not in stop_words][:10])


# q2. regex extraction and replacement
print("\n--- q2. regex extraction and replacement ---")
sample_text = test_lines[0]

long_words = re.findall(r'\b[a-zA-Z]{6,}\b', sample_text)
print("words longer than 5 letters:", long_words[:5])

numbers = re.findall(r'\b\d+(?:\.\d+)*\b', sample_text)
print("numbers and versions:", numbers[:5])

capitalized = re.findall(r'\b[A-Z][a-z]*\b', sample_text)
print("capitalized words:", capitalized[:5])

vowels = re.findall(r'\b[aeiouAEIOU][a-zA-Z]*\b', sample_text)
print("words beginning with a vowel:", vowels[:5])

text_no_email = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', '<email>', sample_text)
text_no_url = re.sub(r'https?://\S+', '<url>', text_no_email)
text_no_phone = re.sub(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', '<phone>', text_no_url)
print("\nreplaced text:")
print(text_no_phone[:200])


# q3. custom tokenization
print("\n--- q3. custom tokenization ---")
def my_tokenize(text):
    pattern = r'https?://\S+|[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}|\b\d{3}[-.]?\d{3}[-.]?\d{4}\b|\b\d+(?:\.\d+)+\b|\b\w+(?:-\w+)+\b|\w+(?:[^\w\s]\w+)*'
    return re.findall(pattern, text)

my_tokens = my_tokenize(sample_text)
normal_tokens = word_tokenize(sample_text)

print("my tokens:", my_tokens[:10])
print("nltk tokens:", normal_tokens[:10])

print("\ndifferences explanation:")
print("1. my_tokenize keeps words like 'wi-fi' together, but word_tokenize splits them at the hyphen.")
print("2. my_tokenize keeps version numbers like '2.0.1' as one token.")
print("3. my_tokenize keeps emails and urls fully intact as single units.")


# q4. stemming and lemmatization
print("\n--- q4. stemming and lemmatization ---")
unique_final_words = list(set(all_final_tokens))

port = PorterStemmer()
lanc = LancasterStemmer()
regex_stemmer = RegexpStemmer('ing$|ed$', min=4)
lemma = WordNetLemmatizer()

def get_simple_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    if tag == 'J':
        return wordnet.ADJ
    elif tag == 'V':
        return wordnet.VERB
    elif tag == 'R':
        return wordnet.ADV
    else:
        return wordnet.NOUN

words_list = []
porter_list = []
lanc_list = []
regex_list = []
lemma_list = []

for word in unique_final_words[:50]:
    p = port.stem(word)
    l = lanc.stem(word)
    r = regex_stemmer.stem(word)
    lem = lemma.lemmatize(word, get_simple_pos(word))
    
    if p != l or p != r or p != lem:
        words_list.append(word)
        porter_list.append(p)
        lanc_list.append(l)
        regex_list.append(r)
        lemma_list.append(lem)

diff_df = pd.DataFrame({
    'word': words_list,
    'porter': porter_list,
    'lancaster': lanc_list,
    'regexp': regex_list,
    'lemma': lemma_list
})
print("suffix choice for regex: 'ing' and 'ed' because it support tickets use verbs like 'working' or 'crashed'.")
print(diff_df.head(10).to_string(index=False))


# q5. corpus statistics
print("\n--- q5. corpus statistics ---")
s1 = all_tokens
s2 = all_no_punct
s3 = all_final_tokens

s4 = []
for word in s3:
    s4.append(port.stem(word))

def print_stats(name, token_list):
    total = len(token_list)
    unique = len(set(token_list))
    ttr = unique / total if total > 0 else 0
    print(f"{name} - total tokens: {total}, unique tokens: {unique}, ttr: {ttr:.4f}")

print_stats("s1 (all tokens)", s1)
print_stats("s2 (no punctuation)", s2)
print_stats("s3 (final tokens)", s3)
print_stats("s4 (s3 after porter stemmer)", s4)

print("\ntop 10 words of s1:")
print(Counter(s1).most_common(10))

print("\ntop 10 words of s3:")
print(Counter(s3).most_common(10))

print("\ntop 5 bigrams of s1:")
print(Counter(ngrams(s1, 2)).most_common(5))

print("\ntop 5 bigrams of s3:")
print(Counter(ngrams(s3, 2)).most_common(5))


# q6. interpretation
print("\n--- q6. interpretation ---")
print("(a) why does ttr change from s1 to s4 in your dataset?")
print("answer: removing stopwords and punctuation lowers the total count. stemming reduces different words (like 'fail' and 'failing') to one root word, which lowers the unique count, changing the final ratio.")

print("\n(b) give one example where word_tokenize() and your tokenizer differ. explain the difference.")
print("answer: word_tokenize splits 'state-of-the-art' into multiple parts. my tokenizer keeps it as a single token because of the hyphen regex rule.")

print("\n(c) give one example where stemming produces an undesirable result.")
print("answer: porter stemmer cuts 'universal' to 'univers', which loses meaning and looks like 'universe'.")

print("\n(d) give one example where pos-aware lemmatization preserves meaning better than stemming.")
print("answer: lemmatization turns 'better' into 'good' because it knows it is an adjective, preserving the true base word. a stemmer just cuts it to 'bet', losing the meaning.")
