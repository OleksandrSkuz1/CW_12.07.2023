import json
if __name__ == '__main__':

    # with open("products.json", "r", encoding="utf-8") as file:
    #      products = json.load(file)


    # for item in products:
    #     for features in item['features']:
    #         if features['value'] == "A++":
    #             print(item['title'], features)

    for item in products:
        with open(f"single_product/{item['id']}.json", "w", encoding="cp1251") as file:
            json.dump(item, file)

        # id = 13
        # with open(f"single_product/{id}.json", "r") as file:
        #     product = json.load(file)
        #     print(product)









