with open("log.txt")as f:
    content=f.read()

if("python" in content):
    print("Python is present")
else:
    print("Python is not present")        