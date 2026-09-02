import pandas as pd
# 4 fixed FAQ entries
fixed_entries = [
    {
        "question": "what is the annual fee",
        "answer": "The annual fee is Rs 500.",
        "keywords": "fee cost price charge",
        "category": "billing"
    },
    {
        "question": "how to reset password",
        "answer": "Go to Settings > Reset Password.",
        "keywords": "password reset login",
        "category": "account"
    },
    {
        "question": "what are your working hours",
        "answer": "We are open 9 AM to 5 PM.",
        "keywords": "hours timing open time",
        "category": "general"
    },
    {
        "question": "how can i pay the fee",
        "answer": "You can pay via UPI, card, or net banking.",
        "keywords": "pay payment upi fee",
        "category": "billing"
    }
]

# Our roll number
roll_number = 1024170355

# Last 3 digits
last_three = str(roll_number)[-3:]

# Categories
categories = ["billing", "account", "general"]

# Create 2 entries using digits from our roll number
digit1 = int(last_three[0])   # 3
digit2 = int(last_three[1])   # 5

category1 = categories[digit1 % 3]
category2 = categories[digit2 % 3]

entry1 = {
    "question": "how do i pay my fee",
    "answer": "You can pay your fee using UPI or card.",
    "keywords": "fee payment pay",
    "category": category1
}

entry2 = {
    "question": "how can i update my details",
    "answer": "You can update your details from your account settings.",
    "keywords": "update details account",
    "category": category2
}

# Add the two new entries
all_entries = fixed_entries + [entry1, entry2]

# Create DataFrame
df = pd.DataFrame(all_entries)

print(df)






q2
def score_query(query, df):
    query_words = query.lower().split()

    results = []

    for i in range(len(df)):
        keywords = df.loc[i, "keywords"].lower().split()

        score = 0

        for word in query_words:
            if word in keywords:
                score = score + 1

        if score > 0:
            results.append((score, df.loc[i, "question"]))

    # Sort according to score
    results.sort(reverse=True)

    return results

q3

def same_category(category_name, df):
    result = []

    for i in range(len(df)):
        if df.loc[i, "category"] == category_name:
            result.append(df.loc[i, "question"])

    return result


q4

new_keyword = input("Enter a new keyword: ")

df.loc[0, "keywords"] = df.loc[0, "keywords"] + " " + new_keyword

print(df)

