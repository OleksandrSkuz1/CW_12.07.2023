import json
if __name__ == '__main__':

    with open("products.json", "r", encoding="utf-8") as file:
         products = json.load(file)

    # spysok = []
    # for item in products:
    #     spysok.append(item['title'])
    #  print(spysok)

    # products.sort(key=lambda x: x["title"])
    # print(products)

    # products.sort(key=lambda product: product["price"])
    # sorted_product = sorted(products, key=lambda product: product["price"], reveres=True)
    # print(sorted_product)

    with open("products.json", "w", encoding="utf-8") as file:
         json.dumps(products, file)


















