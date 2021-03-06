# 9-6
class Restaurant:
	def __init__(self, name, kind):
		self.name = name
		self.kind = kind
		self.number_served = 0

	def describe_restaurant(self):
		print(f"レストランの名前は{self.name}です。")
		print(f"{self.kind}を提供しています。\n")

	def open_restaurant(self):
		print(f"{self.name}がオープンしました！\n")

	def set_number_served(self, number_served):
		self.number_served = number_served

	def increment_number_served(self, add_number):
		self.number_served += add_number

class IceCreamStand(Restaurant):
	def __init__(self, name, kind):
		super().__init__(name, kind)
		self.flavors = 'vanilla'

	def describe_flaver(self):
		print(self.flavors.title())

chocolate_ice = IceCreamStand('31', 'アイスクリーム')
chocolate_ice.flavors = 'chocolate'
chocolate_ice.describe_restaurant()
chocolate_ice.describe_flaver()