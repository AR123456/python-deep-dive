import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


# based on Primary Fur Color  column create a new DataFrame csv file
# Fur Color , Count

# sum by Fur Color
cin_sum =0
black_sum =0
grey_sum =0
# # Cinnamon
cinnamon_list = data["Primary Fur Color"].to_list()
for i in cinnamon_list:
    if i == "Cinnamon":
        cin_sum +=1
print(cin_sum)
# Black
black_list = data["Primary Fur Color"].to_list()
for i in black_list:
    if i == "Black":
        black_sum +=1
print(black_sum)

# Gray
grey_list = data["Primary Fur Color"].to_list()
for i in grey_list:
    if i == "Gray":
        grey_sum +=1
print(grey_sum)

data_dic ={
    "Fur Color": ["Cinnamon", "Black", "Gray"],
    "count":[cin_sum,black_sum,grey_sum]
}
data = pandas.DataFrame(data_dic)
data.to_csv("annes_squrrel_count.csv")