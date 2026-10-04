# Given a dictionary of products and their prices, find the product with the highest price.

dict={
    "Car":100000,
    "Bike":20000,
    "JCB":500000,
    "Teackter":520000
}
higest_price=0
product=""
for i in dict:
    if dict[i]>higest_price:
        higest_price=dict[i]
        product=i
    else:
        continue

print(dict)
print("Higest price product and price is:",product,"-",higest_price)
