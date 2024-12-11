class ShoppingCart:
    def __init__(self):
        self.products = {
            1: {"name": "商品1", "price": 10.0, "quantity": 5},
            2: {"name": "商品2", "price": 20.0, "quantity": 3},
            3: {"name": "商品3", "price": 30.0, "quantity": 2},
            4: {"name": "商品4", "price": 40.0, "quantity": 4},
        }
        self.user_balance = 100.0
        self.shopping_cart = []

    def add_to_cart(self, product_id):
        if product_id in self.products and self.products[product_id]['quantity'] > 0:
            # ** 為可變長度的字典參數，將會自動展開
            self.shopping_cart.append({"id": product_id, **self.products[product_id]})
            print(f"\n{self.products[product_id]['name']} 已加入購物車。")
        else:
            print("\n無效的商品編號或商品已售完。")

    def view_cart(self):
        if not self.shopping_cart:
            print("\n購物車是空的。")
        else:
            print("\n購物車內容:")
            total_price = 0
            for item in self.shopping_cart:
                print(f"{item['name']} - ${item['price']}")
                total_price += item['price']
            print(f"\n總價格: ${total_price}")

    def checkout(self):
        if not self.shopping_cart:
            print("\n購物車是空的，無法結帳。")
        else:
            total_price = sum(item['price'] for item in self.shopping_cart)
            if total_price > self.user_balance:
                print("\n餘額不足，無法完成付款。")
            else:
                for item in self.shopping_cart:
                    product_id = item['id']
                    self.products[product_id]['quantity'] -= 1

                self.user_balance -= total_price
                self.shopping_cart.clear()
                print(f"\n付款成功！剩餘餘額: ${self.user_balance}")

    # def checkBalance(self):
    #     if self.user_balance > 0:
    #         print(f"\n剩餘餘額: ${self.user_balance}")
    #     else:
    #         print("\n餘額不足")
    
    def delete_items_in_cart(self, product_id):
        flag = False
        for i in range(0, len(self.shopping_cart)):
            if self.shopping_cart[i]['id'] == product_id:
                delete_item = self.shopping_cart.pop(i)
                flag = True
                break
        if flag is True:
            print(f"\n{delete_item['name']} 已從購物車移除。")
        else:
            print("\n商品不在購物車中。")

if __name__ == '__main__':
    cart = ShoppingCart()

    while True:
        print("\n選項:\n")
        print("1. 加入商品到購物車")
        print("2. 顯示購物車內容")
        print("3. 付款")
        print("4. 離開")
        # print("5. 查看餘額")
        print("6. 移除購物車內商品")

        choice = input("\n請輸入選項 (1/2/3/4/6): ")

        if choice == "1":
            product_id = int(input("\n請輸入要加入購物車的商品編號: "))
            cart.add_to_cart(product_id)

        elif choice == "2":
            cart.view_cart()

        elif choice == "3":
            cart.checkout()

        elif choice == "4":
            print("\n謝謝光臨，再見！")
            break

        #   elif choice == "5":
        #       cart.checkBalance()
        
        elif choice == "6":
            product_id = int(input("\n請輸入要移除的商品編號: "))
            cart.delete_items_in_cart(product_id)

        else:
            print("\n無效的選項，請重新輸入。")
