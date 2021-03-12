filename = 'programming.txt'

# 作成・書き込み（上書き）
# with open(filename, 'w') as file_object:
# 	file_object.write("I love programming.\n")
# 	file_object.write("I love creating new games.\n")

with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large database.\n")
	file_object.write("I love creating apps that can run in browser.\n")