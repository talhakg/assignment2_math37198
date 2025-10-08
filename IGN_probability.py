import pandas as pd

df = pd.read_csv("ign.csv")

xbox = df[df["platform"] == "Xbox 360"] # filter only xbox games

ok_and_adv = xbox[ # choose 'okay and adventure' games only
    (xbox["score_phrase"] == "Okay") &
    (xbox["genre"].str.contains("Adventure", case=False, na=False))
]

count_matches = len(ok_and_adv)
total = len(xbox)

if count_matches < 2:
    prob = 0
else: # calculate for 'okay and adventure' probabiltiy
    prob = (count_matches / total) * ((count_matches - 1) / (total - 1))

print("Probability that both games picked are 'Okay' Adventure:", prob)