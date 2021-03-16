print(pow(10, 3))
# powは階乗
print(pow(3, -2))

drinklist = ['coffee', 'tea', 'water']
print(list(enumerate(drinklist)))
for i, drink in enumerate(drinklist):
	print(i, drink)

# 引数全てに処理をかけるmap
numlist = [1, 3, 6, 8]
def double(x):
	return x * 2
print(list(map(double, numlist)))

# 条件に合うものだけ取り出すfilter
def even_three_div(x):
	return x % 3 == 0
print(list(filter(even_three_div, numlist)))