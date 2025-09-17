import random
print("Choose among these : \n1. Rock\n2. Paper\n3. Scissors")
try:
    user = int(input("Enter your choice (enter the option number) : "))
except ValueError:
    user = -1 
print()
dic={1:'Rock',2:'Paper',3:'Scissors'}
comp=random.choice([1,2,3])
user_score=0
comp_score=0
while (user!=0):
    if user not in dic:
        print('Wrong choice entered! Please try again.')
    else : 
        print(f"User Choice : {dic[user]}")
        print(f'Computer Choice : {dic[comp]}')
        if comp==user:
            print("It's a tie!")
        else :
            flag=-1
            if user==1:
                if comp==2:
                    flag=1
                else:
                    flag=0
            elif user==2:
                if comp==1:
                    flag=0
                else:
                    flag=1
            elif user==3:
                if comp==1:
                    flag=1
                else :
                    flag=0
            if (flag!=1 and flag!=0):
                print('Wrong choice entered!')
            else :
                if flag==1:
                    comp_score+=1
                    print('Computer Wins!')
                elif flag==0:
                    user_score+=1
                    print("User wins!")
        print(f'User Score : {user_score}')
        print(f'Computer Score : {comp_score}')
        print()
    print("Choose among these : \n0. Quit the game \n1. Rock\n2. Paper\n3. Scissors\n")
    try:
        user = int(input("Enter your choice (enter the option number) : "))
    except ValueError:
        user = -1 
    print()
    dic={1:'Rock',2:'Paper',3:'Scissors'}
    comp=random.choice([1,2,3])
print("The final scores are : ")
print(f'User Score : {user_score}')
print(f'Computer Score : {comp_score}')
print('The Game Ends')
            
                
    
