q=['''1. Which mass movement started with Mahatma Gandhi's Dandi March ?

(A) Khilafat Movement
(B) Quit India Movement
(C) Non-cooperation movement
(D) Civil Disobedience Movement

''','''2. Where did Jai Prakash Narayan organize the All India Congress Socialist Conference in 1934 ?

(A) Gaya
(B) Calcutta
(C) Lucknow
(D) Patna

''','''3. Who assassinated Sir Curzon Willey in 1907 in London ?

(A) B. N. Dutta
(B) Sardar Ajit Patel
(C) S. C. Chatterjee
(D) M. L. Dhingra''','''4. Which train was launched on the occasion of 150th birth anniversary of Guru Dev Rabindranath Tagore ?

(A) Karmabhoomi Express
(B) Janmabhoomi Express
(C) Sanskriti Express
(D) Mathrubhumi Express

''','''5. When did the first Dutch fleet reach India ?

(A) 1498
(B) 1510
(C) 1595
(D) 1550

''']
ans=['d','c','d','c','c']
print(q[0])
u1=input('choose your answer:  ').lower()
score=0
if u1==ans[0]:
    print("correct answer\n")
    score+=5
else:
    print("Wrong answer\n")
print(q[1])
u2=input('choose your answer: ').lower()

if u2==ans[1]:
    print("correct answer\n")
    score+=5
else:
    print("Wrong answer\n")

print(q[2])
u3=input('choose your answer: ').lower()
 
if u3==ans[2]:
    print("correct answer\n")
    score+=5
else:
    print("Wrong answer\n")
print(q[3])
u4=input('choose your answer: ').lower()
 
if u4==ans[3]:
    print("correct answer\n")
    score+=5
else:
    print("Wrong answer\n")
print(q[4])
u5=input('choose your answer: ').lower()
 
if u5==ans[4]:
    print("correct answer \n")
    score+=5
else:
    print("Wrong answer\n")
print(f"your score is {score}")
if score>=15:
    print('you are qualified')
else:
    print('Try next time')