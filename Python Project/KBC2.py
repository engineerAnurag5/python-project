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

''','''6.. Where was the first factory set up by the Dutch ?

(A) Machilipatnam
(B) Pulicat
(C) Negapatnam
(D) Surat

''' , '''7. In the modern periodic table, which of the following groups of elements have a complete outer shell ?

(A) 16th Group
(B) 17th Group
(C) 18th Group
(D) 15th Group'''  ,'''  8.According to the law of reflection of light ?

(A) The angle of incidence is greater than the angle of reflection
(B) The angle of incidence is equal to the angle of reflection
(C) The angle of incidence is smaller than the angle of reflection
(D) All the statements are true

''',''' 9. 
The International Literacy Day is observed on

A.	Sep 8
B.	Nov 28
C.	May 2
D.	Sep 22''', '''10:  
Who is the author of the epic 'Meghdoot"?

A.	
Vishakadatta

B.	
Valmiki

C.	
Banabhatta

D.	
Kalidas''' ]
ans=['d','c','d','c','c','a','c','b','a','d']
level=[1000,2000,5000,10000,40000,80000,160000,32000,48000,60000]
score=0
for i in range(0,len(q)) :
    questions=q[i]
    print(f"***Question for Rs. {level[i]}*** \n")
    print(q[i])
    user_ans=input("Choose your answer: ").lower()
    if user_ans==ans[i]:
        score+=level[i]
        print("SAHI JAWAAB\n")
    else:
        print("GALAT JAWAAB!\n")
print(f"At the END OF GAME Aap total  {score} jeet kar ja rahe h")