file =open("idea.xml","r")
data =file.readlines()
for line in data:
    print(line)
file.close()



