dict = {
    "1": "one",
    "2": "Two"
}

print(dict["1"])  # One
# print(dict["5"])  # KeyError since no key named as 5

# Tp ignore the above error
print(type(dict.get("1")))


dict["3"] = "Three"

print(dict)
