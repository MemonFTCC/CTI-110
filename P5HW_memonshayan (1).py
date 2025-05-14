
# Shayan Memon
# 4/23/2025
# P5HW - Recruiting Game
# Elite prospects seek schools with a strong reputation.

import random

# Launching the Recruitment Simulator
print("The recruiting trail starts now, can you build a winning program?\n")

# Select your program and see if it's a powerhouse.
college = input("Enter your school's name: ").title()
elite_colleges = ["Alabama", "Florida", "The Ohio State"]
is_prestigious = college in elite_colleges

# Begin building your roster
team = []

# Scout and sign up to 3 athletes
for i in range(3):
    print(f"\nScouting Player #{i+1}")

    # Uncover a potential recruit
    recruit_name = random.choice(["Cam", "Jalen", "Travis", "Ashton", "Luther"])
    recruit_position = random.choice(["QB", "RB", "WR"])
    recruit_stars = random.randint(1, 5)  # Star rating from 1 to 5

    print(f"{recruit_name} - {recruit_position} - {recruit_stars}★")

    # Ready to make an offer to this athlete
    choice = input("Want to bring this athlete into your program? (yes/no): ").lower()
    if choice != "yes":
        print("You skipped this athlete.\n")
        continue

    # Star players want the spotlight—only big-name schools make the cut
    if recruit_stars >= 4 and not is_prestigious:
        print("Better luck next time, the prospect wants a more prestigious school. Denied.\n")
        continue

    # Place recruit on your roster
    print("Your recruiting efforts paid off, welcome aboard!!\n")
    team.append({"name": recruit_name, "position": recruit_position, "stars": recruit_stars})

# Display final team
print(f"\n{college} Final prospects:")
if team:
    for p in team:
        print(f"{p['name']} - {p['position']} - {p['stars']}★")
else:
    print("No players joined your team.")

print("\n🎓 Thanks for playing!")
