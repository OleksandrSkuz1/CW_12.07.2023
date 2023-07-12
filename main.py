import json
if __name__ == '__main__':

    with open("products.json", "r", encoding="utf-8") as file:
         products = json.load(file)

    new_list_product = []
    for item in products:
        print(item['value'])

        for value in item['value']:
            if value.lower() == "A++":
                 new_list_product.append(item)










