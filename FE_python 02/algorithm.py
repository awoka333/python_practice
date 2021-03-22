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
"""

"""
# バブルソート
def sort(data):
	for i in range(len(data)-1, 0, -1):
		for j in range(i):
			if data[j] > data[j+1]:
				data[j], data[j+1] = data[j+1], data[j]

data = [1, 3, 2, 5, 4, 2, 1]
sort(data)
print(data)
"""

"""
# 挿入ソート
def sort(data):
	for i in range(0, len(data)):
		for j in range(i-1, -1, -1):
			if data[j] > data[j+1]:
				data[j], data[j+1] = data[j+1], data[j]
			else:
				break # passじゃないのは、passだと完成コードっぽくないから？

data = [1, 3, 2, 5, 4, 2, 1]
sort(data)
print(data)
"""

"""
# 選択ソート
def sort(data):
	for i in range(0, len(data)-1):
		min_i = i
		for j in range(i+1, len(data)):
			if data[min_i] > data[j]:
				min_i = j
			data[min_i], data[i] = data[i], data[min_i]

data = [1, 3, 2, 5, 4, 2, 1]
sort(data)
print(data)
"""

"""
# シェルソート
def sort(data):
	gaps = [7, 3, 1] # それぞれのギャップを順に試行する
	for gap in gaps:
		for i in range(0, len(data), gap): # gapの幅離れたデータを挿入ソート
			for j in range(i-gap, 0, -gap):
				if data[j] > data[j+gap]:
					data[j], data[j+gap] = data[j+gap], data[j]
				else:
					break

data = [1, 3, 2, 5, 4, 2, 1]
sort(data)
print(data)
"""


# ヒープソート
from heapq import heappush, heappop

def sort(data):
	heap = []
	while data:
		heappush(heap, data.pop()) #dataの最後の要素を取り出して、eappushでheapに入れる
	while heap:
		data.append(heappop(heap)) # heapから最小値を取り出して、dataの最後に追加する

data = [1, 3, 2, 5, 4, 2, 1]
sort(data)
print(data)