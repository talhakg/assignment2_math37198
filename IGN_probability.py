import pandas as pd

df = pd.read_csv("ign.csv")

# STEP 1 ---
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

# STEP 2 ---
sega = df[df["platform"].str.contains("Sega", case=False, na=False)] # filter only sega games
not_RPG = sega[sega["genre"].str.contains("RPG", case=False, na=False) == False] # check games that aren't rpg

not_RPG_count = len(not_RPG)
segas_total = len(sega)

not_RPG_prob = not_RPG_count / segas_total # calculate not RPG games for sega probability

print("Probability that a Sega game picked isn't an RPG:", not_RPG_prob)