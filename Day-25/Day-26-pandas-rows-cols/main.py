
#
# weather_list = open("weather_data.csv", "r")
# print(weather_list.readlines())
#
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# # use pythons csv library https://docs.python.org/3/library/csv.html
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     #data is now an object
#     for row in data:
#         # print(row)
#         # print(row[1])
#         # dont print the temp row
#         if row[1] != "temp":
#             # temperatures.append(row[1])
#             # convert to int
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()
print(data_dict)

temp_list=data["temp"].to_list()
print(temp_list)

avg_temp= round(sum(temp_list)/len(temp_list))
print(avg_temp)

# using the mean method from the pandas library
avg_pandas_temp = data["temp"].mean()
print(avg_pandas_temp)
max_pandas_temp = data["temp"].max()
print(max_pandas_temp)
# using data.temp
print(data.temp)

#Get data from row
print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
print(monday.condition)
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)
print(data.columns)

#### create a csv from data in python
data_dict = {
    "students":["Amy", "James", "Brad"],
    "scores":[76,56,65]
}
data = pandas.DataFrame(data_dict)
# print(data)
data.to_csv("annes_data_csv")