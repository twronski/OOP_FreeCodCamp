from item import Item
from phone import Phone


if __name__ == '__main__':
    Item.instantiate_from_csv()
    print(Item.all)
    phone1 = Phone('Iphone', 10.23, 100, 13)
    phone1.apply_discount()
    print(phone1)
    print(Phone.all)
    print(Item.is_integer(2.3))
    print(Item.is_integer(3.0))
    print(Item.is_integer(8))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
