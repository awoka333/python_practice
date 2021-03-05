# 9-1, 9-4
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

# restaurant = Restaurant('レストラン', 'フレンチ')
# print(restaurant.name)
# print(restaurant.kind)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# 9-2
# restaurant_a = Restaurant('レストランA', 'イタリアン')
# restaurant_b = Restaurant('レストランB', '和食')
# restaurant_c = Restaurant('レストランC', 'ブラジル料理')
# restaurant_a.describe_restaurant()
# restaurant_b.describe_restaurant()
# restaurant_c.describe_restaurant()

# 9-3, 9-5
class User:
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempt = 0

	def describe_user(self):
		print(f"名前：{self.last_name} {self.first_name}")

	def greet_user(self):
		print(f"こんにちは、{self.last_name} {self.first_name}さん！")

	def increment_login_attempts(self, add_attempt):
		self.login_attempt += add_attempt

	def reset_login_attempts(self):
		self.login_attempt = 0

# lily = User('Lily', 'Brown')
# lily.describe_user()
# lily.greet_user()

# 9-4
# restaurant_d = Restaurant('レストランD', 'タイ料理')
# restaurant_d.describe_restaurant()
# print(restaurant_d.number_served)
# restaurant_d.number_served = 100
# print(restaurant_d.number_served)

# restaurant_d.set_number_served(500)
# print(restaurant_d.number_served)

# restaurant_d.increment_number_served(50)
# print(restaurant_d.number_served)

# 9-5
user_a = User('太郎', '山田')
print(user_a.login_attempt)
user_a.increment_login_attempts(3)
print(user_a.login_attempt)
user_a.reset_login_attempts()
print(user_a.login_attempt)