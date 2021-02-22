# 辞書
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# リスト
# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
# 	print(alien)

# エイリアンをか格納する空のリストを作成する
aliens = []

# 30匹のエイリアンを生成する
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

# 最初の5匹のエイリアンの情報を出力する
for alien in aliens[:5]:
	print(alien)
print("...")

# 生成されたエイリアンの数を出力する
print(f"全エイリアンの数：{len(aliens)}")