p1="Make money"
p2="buy now"
message=input("enter your message:")
if((p1 in message) or (p2 in message)):
    print("this is spam",message)
else:
    print("nice comment:",message) 