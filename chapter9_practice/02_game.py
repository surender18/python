# def game():
#     a=int(input("Enter a number: "))
#     return a
# game()
# f=open("Hi-score.txt")
# print("Hi-score is: ",f.read())


# f.close()

# import random
# def game():
#     print("Welcome to the number guessing game")
#     score=random.randint(1,100)
#     with open("Hi-score.txt") as f:
#         hi_score=f.read()
#         if(hi_score!=""):
#             hi_score=int(hi_score)
#         else:
#             hi_score=0    
#     print(f"Your score:{score}")
#     if(score>hi_score):
#         with open("Hi-score.txt","w") as f:
#             f.write(str(score))
#     return score
# game()        

import random
def game():
    print("Welcome to the number guessing game")
    score=random.randint(1,100)
    with open("Hi-score.txt") as f:
        hi_score=f.read()
        if(hi_score!=""):
            hi_score=int(hi_score)
        else:
            hi_score=0    
    print(f"Your score:{score}")
    if(score>hi_score):
        with open("Hi-score.txt","w") as f:
            f.write(str(score))
    return score
game()        