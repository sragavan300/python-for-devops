import os

input = input("Enter the input values:").split(",")
print(input)

for folder in input:
    try:
        print("====" , input , "======")
        files = os.listdir(folder) 
    except FileNotFoundError:
        print("No files")
        break 
    for file in files:   
        print(file)


    
