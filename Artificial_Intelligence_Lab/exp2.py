
print("Career Path Suggestion Based on Student Interests")
print("Select any two subjects according to your interest from \nPhysics.\nMaths.\nChemistry.\nprogramming.\nBiology.\nCircuits.\nStatistics.\nAI Concepts.")
sub1 = input("Enter the first subject : ")
sub2 = input("Enter the second subject : ")
if((sub1=="Maths" and sub2=="Physics") or (sub1=="Physics" and sub2=="Maths")):
            print("Suggested path = Mechanical Engineering")
elif((sub1=="Maths" and sub2=="Programming") or (sub1=="Programming" and sub2== "Maths")):
            print("suggested path = Computer Engineering")
elif((sub1=="Circuits" and sub2=="Physics") or (sub1=="Physics" and sub2=="Circuits")):
            print("Suggested path = Electrical Engineering")
elif((sub1=="Chemistry" and sub2=="Biology") or (sub1=="Biology" and sub2=="Chemistry")):
            print("Suggested path = Biotechnology")
elif((sub1=="Statistics" and sub2=="Programming") or (sub1=="Programming" and sub2=="Statistics")):
            print("Suggested path = Artificial intilligence")
elif((sub1=="Programming" and sub2=="AI Concepts") or (sub1=="AI Concepts" and sub2=="programming")):
            print("Suggested path = Aritificial Intilligence and Machine Learning")
else:
            print("Enter valid input")
