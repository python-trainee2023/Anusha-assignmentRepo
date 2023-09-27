#Create a file ‘student.txt’ that contains students’ name, gender, and grade.
# Write a program to read individual lines and copy each line of the file and write in another file using for loop.
# The content should be in uppercase. Use context manager.

with open("student1.txt","r") as firstfile:
    
    with open("student2.txt",'w') as secondfile:
      
        for line in firstfile:
            uppercase_line=line.upper()
            secondfile.write(uppercase_line)
            
print("Content copied ")