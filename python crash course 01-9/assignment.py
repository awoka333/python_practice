# 9-1
class Restaurant:
	def __init__(self, name, kind):
		self.name = name
		self.kind = kind

	def describe_restaurant(self):
		print(f"レストランの名前は{self.name}です。")
		print(f"{self.kind}を提供しています。")

	def open_restaurant(self):
		print(f"{self.name}がオープンしました！\n")

restaurant = Restaurant('レストラン', 'フレンチ')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2
# restaurant_a = Restaurant('レストランA', 'イタリアン')
# restaurant_b = Restaurant('レストランB', '和食')
# restaurant_c = Restaurant('レストランC', 'ブラジル')