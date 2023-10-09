import random

Questions=["A","B","C","D","E","F"]
Answers=[1,2,3,4,5,6]

Q_A=dict(zip(Questions,Answers))
print (Q_A)

score=0

Questions_Attempt=int(input("How many Questions do you want to attempt : ? "))

for i in range((Questions_Attempt)):
    Q=random.choice(Questions)
    print (f"Question {i+1}")
    print (Q)
    A=input("Your Answer : ")
    if (str(A.lower())==str(Q_A[Q])):
        score+=1
    else:
        print ("Incorrect")

print (f"Score is {score}")
print (f"Score Percentage is {score/Questions_Attempt * 100}")
