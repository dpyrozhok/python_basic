# -*- coding: utf-8 -*-
import random 

class Shop(object):
    """
    Shop class
    
    """

    def __init__(self):
        self.sweets = random.randint(0, 10)
        self.trout = random.randint(0, 2)
        self.halibut = random.randint(0, 2)
        self.sauce = random.randint(0, 5)
        self.lemons = random.randint(1, 5)
        self.milk = random.randint(0, 3)
        self.milkFreshness = random.choice([True, False])

    def print_shop_goods(self):
        print('')
        print('В магазине:')
        print('Сладостей:', self.sweets)
        print('Лосося:', self.trout)
        print('Окуня:', self.halibut)
        print('Соуса:', self.sauce)
        print('Лимонов:', self.lemons)
        print('Молока:', self.milk)
        print('Свежее молоко:', 'Да' if self.milkFreshness else 'Нет')
        
class Client(object):
    def __init__(self):
        self.sweets = 0
        self.trout = 0
        self.halibut = 0
        self.sauce = 0
        self.lemons = 0
        self.milk = 0
        self.milkFreshness = None
    
    
    def buy(self, class_shop):
        if class_shop.sweets > 2:
            self.sweets = 2
            class_shop.sweets -= 2
        if class_shop.trout > 0:
            self.trout += 1 
            class_shop.trout -= 1
        elif class_shop.halibut > 0:
            self.halibut += 1
            class_shop.halibut -= 1
        if self.trout or self.halibut:
            if class_shop.sauce > 0:
                self.sauce += 1
                class_shop.sauce -= 1
            else:
                self.lemons += 1
                class_shop.lemons -= 1
        if class_shop.milk > 0 and class_shop.milkFreshness:
            self.milk += 1
            self.milkFreshness = class_shop.milkFreshness
            class_shop.milk -= 1
        
    def print_client_recipe(self):
        print('')
        print('Клиент купил:')
        print('Сладостей:', self.sweets)
        print('Лосося:', self.trout)
        print('Окуня:', self.halibut)
        print('Соуса:', self.sauce)
        print('Лимонов:', self.lemons)
        print('Молока:', self.milk)
        print('Свежее молоко:', 'Да' if self.milkFreshness else 'Нет')

def main():
    #create shop
    shop = Shop()
    shop.print_shop_goods()
    
    #create client and choose shop
    client = Client()
    client.buy(shop)
    client.print_client_recipe()
    
    #what left in shop
    shop.print_shop_goods()

if __name__ == '__main__':
    main()