from faker import Faker
import pandas as pd
import random

fake = Faker()

rows = []
topics = ["Arrays","Strings","Tree","Graph","DP"]

for _ in range(500):
    rows.append([
        fake.user_name(),
        random.choice(topics),
        random.randint(10,200),
        random.choice(["Easy","Medium","Hard"]),
        fake.date_this_year()
    ])

pd.DataFrame(
    rows,
    columns=["User","Topic","Solved","Level","Date"]
).to_csv("data/dsa_progress.csv", index=False)

print("Dummy data generated")
