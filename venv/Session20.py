import os
"""
path = os.getcwd()
print("CWD is :",path)

os.chdir("/Users/My Pc/Downloads")

path=os.getcwd()
print("CWD NOW :",path)


os.mkdir("/Users/My Pc/Downloads/PythonToday")
print("Directory Created")

os.chdir("/Users/My Pc/Downloads")
os.rmdir("/Users/My Pc/Downloads/PythonToday")
print("Removed")
"""
"""
print("Os name :",os.name)
print("Users :",os.getlogin())
print("Process Id :",os.getppid())"""
"""
path = os.path.join("/Users/My Pc/Downloads" , "pdf")
path1=os.path.join("/Users/My Pc/Downloads" , "4.1 - Final - Troubleshooting Theory")
#print("Path is ",path)
#path = os.path.split(path)
#print("Path is ",path)
print("is Path existing : ",os.path.exists(path))
print("is it directory : ",os.path.isdir(path))
print("is it file : ",os.path.isfile(path))
print("is Path existing : ",os.path.exists(path1))
print("is it directory : ",os.path.isdir(path1))
print("is it file : ",os.path.isfile(path1))
"""

path = os.path.join("/Users/My Pc/Downloads")
if os.path.isdir(path):
    files =  os.walk(path)
    allFiles = list(files)
    print(allFiles)
    for f in allFiles :
        print(f)

