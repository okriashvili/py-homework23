import unittest, main

class TestProcessOrders(unittest.TestCase):
    def setUp(self):
        self.stock = 100
        self.inventory = {"product": self.stock}
        self.orders = [
            {"product": "apple", "quantity": 5},
        ]
    # ა: order-ში გადმოცემული პროდუქტი არის თუ არა საწყობში
    def test_product_is_in_inventory(self):
        with self.assertRaises(ValueError):
            main.process_orders(self.orders, self.inventory)

    # ბ: order-ში გადმოცემული პროდუქტის ოდენობა არის თუ არა საწყობში
    def test_product_quantity_is_in_inventory(self):
        self.assertTrue(self.inventory["product"] > self.orders[0]["quantity"])

    # გ: თუ ყველაფერი სწორად გადმოეცა, საბოლოოდ სწორად აკლებს თუ არა საწყობში არსებული
    # პროდუქტის ოდენობას order-ში მოთხოვნილ ოდენობას
    def test_if_correctly_deducts_stock(self):
        self.assertEqual(self.inventory["product"] - self.orders[0]["quantity"], 95)


    # python test-main.py

if __name__ == "__main__":
    unittest.main()



















#
# class Test_process_orders(unittest.TestCase):
#     def setUp(self):
#         self.orders = [
#             {"product": "apple", "quantity": 5}
#         ]
#         self.inventory = {"product": 100}
#
#
#     #
#     # def test_process_order(self):
#     #     self.assertEqual(process_orders(self.orders), self.inventory)
#
#     def test_product_exists_in_inventory(self):
#         orders = [{"product": "apple", "quantity": 5}]
#         result = process_orders(orders, self.inventory.copy())
#         self.assertEqual(result, orders)
#
#         # with self.assertRaises(ValueError):
#         #     main.process_orders(self.orders, self.inventory)
#         # self.assertTrue(main.process_orders(5, 107), 102)
#
#
# if __name__ == '__main__':
#     unittest.main()


    # python test-main.py