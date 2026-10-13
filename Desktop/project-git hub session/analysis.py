import pandas as pd

insurance = pd.DataFrame({
    "Patient_ID": [101,102,103,104,105,106],
    "Insurance_Provider": [
        "Star Health",
        "HDFC Ergo",
        "ICICI Lombard",
        "Star Health",
        "HDFC Ergo",
        "Star Health"
    ],
    "Claim_Amount": [45000,30000,50000,40000,25000,50000]
})

print(insurance)

movies = ["Dangal", "3 Idiots", "Jawan", "Pathaan",]
ratings = [9, 10, 8, 7]

print("MOVIE RATING ANALYSIS")
print("---------------------")

for i in range(len(movies)):
    print(movies[i], ":", ratings[i])

average = sum(ratings) / len(ratings)

print("---------------------")
print("Average Rating:", average)

highest = ratings.index(max(ratings))

print("Highest Rated Movie:", movies[highest])
print("Highest Rating:", ratings[highest])