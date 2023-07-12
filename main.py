if __name__ == '__main__':

    with open("products.json", "r", encoding="utf-8") as file:
        products = json.load(file)
        for item in products:
            price = item["price"].replace("NBSP", "").replace("", "")
            item["price"] = price





