
numbers = [1,2,3]
# new_numbers = [new_item for item in list ]
new_numbers = [n + 1 for n in numbers ]

name = "Anne"
new_list = [letter for letter in name]
start = range(1,5)
new_range = [n*2 for n in start]
newer_range = [n*2 for n in range(1,5)]
names =["Samantha","Becky", "Alicia","Tom", "Paul"]
short_names = [name for name in names if len(name)<5]
long_all_caps = [ name.upper() for name in names if len(name)>5]