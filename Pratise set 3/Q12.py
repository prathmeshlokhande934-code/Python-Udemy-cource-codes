# Write a program that merges two dictionaries into one.
dict1={
    "Car":100000,
    "Bike":20000,
    "JCB":500000,
    "Teackter":520000
}
dict2={
    "Cycle":100000,
    "Scoter":50000,
    "E-bike":70000
}

dict3=dict1 | dict2
print(dict3)