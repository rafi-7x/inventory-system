import __main__
product_list = []
def add_product():
    products_temp = []
    answer = ""
    while answer != "exit":
        name = str(input("Enter product's name : "))
        quantity = int(input(f"Enter {name}'s quantity : "))
        product_collector = {"name": name,"quantity": quantity}
        products_temp.append(product_collector)
        answer = str(input("Type exit if you wanna leave : "))
    else:
       print("Exiting...")
    return products_temp   
def sell_product():
    search_product = str(input(("Enter the product's name : ")))
    while search_product != "exit":
        for product in product_list:
            if product["name"] == search_product:
               if(product["quantity"]) > 0:
                   product["quantity"] = product["quantity"] -1
                   print(f"The product {product['name']} has been sold")
                   print(f"The quantity has been updated : {product["quantity"]}")
                   search_product = str(input(("Type exit to leave : ")))
                   break
               else:
                   print("Out of stock")
                   search_product = str(input("Type exit or search for another product : "))
                   break
        else:
            print("Product no found")
            search_product = str(input("Type exit or search for another product : "))
def low_stock():
    print("Scanning all the products...")
    for product in product_list:
        if product["quantity"] < 5:
            print(f"The product : {product['name']}")
            print(f"Its quantity : {product['quantity']}")
                                    
def display_product():
       for product in product_list:
           print(f"The product : {product['name']}")
           print(f"The quantity : {product['quantity']}")

def main():
    print("  The Main Menu  ")
    options = ""
    while options != "exit":
        options = str(input("_Add a product\n_Sell a product\n_Display all the products\nDisplay low stock products\n_Exit\n"))
        if options == "Add a product" or options == "add a product":
             products = add_product()
             if products:
                product_list.extend(products)
        elif options == "Sell a product" or options == "sell a product":
            sell_product()
        elif options == "Display all the products" or options == "display all the products":
            display_product()
        elif options == "Display low stock products" or options == "display low stock products":
            low_stock()
        elif options == "Exit" or options == "exit":
            print("Exiting...")
            break     
if __name__ == "__main__":
    main()                       

                    