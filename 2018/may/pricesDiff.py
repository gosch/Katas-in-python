def pricesDiff(retailItems, retailPrices, onlineItems, onlinePrices):
    products = {}
    count = 0
    for i, item in enumerate(retailItems):
        products[item] = retailPrices[i]

    for i, item in enumerate(onlineItems):
        if item in products:
            if products[item] != onlinePrices[i]:
                count += 1
    return count

retailItems = ["tomato", "bread", "salt"]
retailPrices = [15.99, 4.99, 5.99]
onlineItems = ["tomato", "bread", "salt", "water"]
onlinePrices = [15.89, 4.99, 6, 1.99]

print(pricesDiff(retailItems, retailPrices, onlineItems, onlinePrices))
