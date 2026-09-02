import pandas as pd

roll_number = "1024170355"

print("q1")

categories = ["billing", "account", "general"]

fixed_entries = [
    {"question": "what is the annual fee", "answer": "the annual fee is rs 500.", "keywords": "fee cost price charge", "category": "billing"},
    {"question": "how to reset password", "answer": "go to settings > reset password.", "keywords": "password reset login", "category": "account"},
    {"question": "what are your working hours", "answer": "we are open 9 am to 5 pm.", "keywords": "hours timing open time", "category": "general"},
    {"question": "how can i pay the fee", "answer": "you can pay via upi, card, or net banking.", "keywords": "pay payment upi fee", "category": "billing"}
]

last_digit_1 = int(roll_number[-2])
last_digit_2 = int(roll_number[-1])

category_1 = categories[last_digit_1 % 3]
category_2 = categories[last_digit_2 % 3]

personal_entry_1 = {
    "question": "how can i change my email address",
    "answer": "you can change your email address from account settings.",
    "keywords": "email change account",
    "category": category_1
}

personal_entry_2 = {
    "question": "how can i update my profile",
    "answer": "you can update your profile from the settings page.",
    "keywords": "profile update settings",
    "category": category_2
}

all_entries = fixed_entries + [personal_entry_1, personal_entry_2]

df = pd.DataFrame(all_entries)

print(df)


print()
print("q2")

def score_query(query, df):
    query_words = query.lower().split()
    results = []

    for i in range(len(df)):
        text = df.loc[i, "question"] + " " + df.loc[i, "keywords"]
        text_words = text.lower().split()

        score = 0

        for word in query_words:
            if word in text_words:
                score = score + 1

        if score > 0:
            results.append([df.loc[i, "question"], score])

    results = sorted(results, key=lambda x: x[1], reverse=True)

    return results


query = input("enter your question: ")
results = score_query(query, df)

print(results)


print()
print("q3")

def same_category(category_name, df):
    result = df[df["category"] == category_name]
    return result


result = same_category(category_1, df)

print(result)


print()
print("q4")

new_keyword = input("enter a new keyword: ")

df.loc[0, "keywords"] = df.loc[0, "keywords"] + " " + new_keyword

df.to_csv(roll_number + "_faq_data.csv", index=False)

print(df)


print()
print("q5")

category_count = df.groupby("category").size()

print(category_count)


print()
print("q6")

query = "fee"

results = score_query(query, df)

highest_score = results[0][1]

print("tie query")

for result in results:
    if result[1] == highest_score:
        print(result)


query = "password"

results = score_query(query, df)

highest_score = results[0][1]

print("non tie query")

for result in results:
    if result[1] == highest_score:
        print(result)
