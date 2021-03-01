def make_pizza(size, *toppings):
	"""注文されたトッピングの一覧を出力する"""
	print(f"\n{size}インチのピザを、以下のトッピングのピザを作ります。")
	for topping in toppings:
		print(f"- {topping}")

# make_pizza(16, 'ペパロニ')
# make_pizza(12, 'マッシュルーム', 'ピーマン', 'エクストラチーズ')