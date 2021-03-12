# try:
# 	print(5/0)
# except ZeroDivisionError:
# 	print('ゼロで割ることはできません！')

print("数を2つ教えて下さい。割り算します。")
print("終了するには'q'を入力してください。")

while True:
	first_number = input("\n1番目の数：")
	if first_number == 'q':
		break
	second_number = input("\n2番目の数：")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("ゼロで割る事はできません！")
	else:
		print(answer)