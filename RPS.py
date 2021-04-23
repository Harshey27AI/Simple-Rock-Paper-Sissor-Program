import random



print("Let's Play Rock,Paper,Scissor ")
print("for 1.Rock, 2. Scissor , 3. Paper")
user = int(input("Enter Number:"))
if user>41:
    print("invalid Input")


comp_pick = random.randint(1,3)

print("Computer choose",comp_pick)

if user == 1 and comp_pick == 2:
    print("\n \tUSER WINS")

elif comp_pick == 1 and user == 2:
    print("\n \tCOMPUTER WINS")
    
elif comp_pick == 1 and user == 3:    
    print("\n \tCOMPUTER WINS")
    
elif user == 1 and comp_pick == 3:    
    print("\n \tCOMPUTER WINS")    
    
elif user == 3 and comp_pick == 1:    
    print("\n \tUSER WINS")    

elif user == 2 and comp_pick == 3:    
    print("\n \tUSER WINS")    
        
elif user == 3 and comp_pick == 2:    
    print("\n \tCOMPUTER WINS")    


##SAME        
elif user == 1 and comp_pick == 1:
    print("Both Choose Same")

elif user == 2 and comp_pick == 2:
    print("Both Choose Same")

elif user == 3 and comp_pick == 3:
    print("Both Choose Same")
        