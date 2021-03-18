"""
# 線形探索
def search(data, target):
	for i in range(len(data)):
		if data[i] == target:
			return i
		# return -1

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
print(f"要素番号{search(data, target)}にデータ{target}を見つけました。")
"""

# 2分探索
def search(data, target):
	start, end = 0, len(data)
	while start <= end:
		i = (start + end) // 2
		if data[i] == target:
			return i
		elif data[i] < target:
			start = i + 1
		else:
			end = i - 1
		# return -1

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
print(f"要素番号{search(data, target)}にデータ{target}を見つけました。")