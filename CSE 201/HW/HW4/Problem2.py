

def main():
    item_price = float(input("Enter price of item: ")) #Gets price of item

    print("Enter weight of item in pounds and ounces seperately")

    weight_pound = float(input("\nEnter pounds: ")) #Gets pounds
    weight_ounce = float(input("\nEnter ounces: ")) #Gets ounces

    total_ounce = weight_pound*16+weight_ounce #Gets total ounces

    price_per_ounce = item_price/total_ounce

    print("Price per ounce: ${}".format(round(price_per_ounce,2)))
main()
