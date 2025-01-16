def rem(l,word):
    n=[]
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n        
    
l =["sk","jack","ani","shubham","mankan","rohan","an"]
print(rem(l,"an"))     