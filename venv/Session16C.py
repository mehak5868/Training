cppCode =  """
 #include<iostream>
 using namespace std;
 int main()
 {
 return 0;
 }
"""
print(cppCode)
file = open("Hloo.cpp" ,"w")
file.write(cppCode)

print(">>data written in file ")

file.close()
