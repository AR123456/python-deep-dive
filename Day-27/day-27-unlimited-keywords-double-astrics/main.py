#
# def calculate(**kwargs):
#     # can pass in many keyword arguments -its a dictionary
#     #that represents keywords and values
#     # print(type(kwargs))
#     # print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     # print(kwargs["add"])
#
#
# calculate(add=3, multiply=5)


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# can pass in many keyword arguments -its a dictionary
# that represents keywords and values
# print(type(kwargs))
# print(kwargs)
# for key, value in kwargs.items():
#     print(key)
#     print(value)
# print(kwargs["add"])


calculate(2, add=3, multiply=5)