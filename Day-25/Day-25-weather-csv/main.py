
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
# print(data)

# just the temperature

print(data["temp"])