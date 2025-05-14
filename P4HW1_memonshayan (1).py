# Shayan Memon
#4/6/2025
#P4HW1
#Scores 
# Pseudocode




#get number of scores from user
num_score = int(input("how many scores would you like to enter? "))

#create empty list
score = []

#loop scores

for num in range(1, 7):
    score = float(input(f"enter score {num}: "))
    if 0 <= score <= 100:
        score.append(score)
    else:
        print("invalid score entered!")
        print("score should be between 0 and 100")


#find lowest score
smallest = min(score)

#remove lowest score
score.remove(smallest)

#cal average
avg = sum(score) / len(score)

#grades
if avg >= 90:
    grade = 'a'
else:
    if avg >= 80:
        grade = 'b'
    else:
        if avg >= 70:
            grade = 'c'
        else:
            if avg >= 60:
                grade = 'd'
            else:
                grade = 'f'

#display results
print("--------------results--------------")
print(f"lowest score:{smallest}")
print(f"modified List:{score}")
print(f"scores average:{avg:.2f}")
print(f"grade:{grade}")
print("---------------------------------")