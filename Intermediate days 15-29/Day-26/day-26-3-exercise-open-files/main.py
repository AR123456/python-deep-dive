file1 = open("file1.txt","r").read().splitlines()
file2 = open("file2.txt", "r").read().splitlines()
combined = [int(item) for item in file1 if item in file2]
print(combined)



# combined =[n + [n for n in file2]for n in file1 ]
# print(combined)

# Write your code above 👆

# print(result)

#
with open("file1.txt")as file1:
    file1_data = file1.readlines()
with open("file2.txt")as file2:
    file2_data = file2.readlines()
print(file1_data)
print(file2_data)

result =[ int(item) for item in file1_data if item in file2_data ]
print(result)