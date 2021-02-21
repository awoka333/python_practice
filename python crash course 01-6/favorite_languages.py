favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
friends = ['phil', 'sarah']

# for name, language in favorite_languages.items():
# 	print(f"{name.title()}の好きなプログラミング言語は{language.title()}です。")

# for name in favorite_languages.keys():
# 	print(name.title())
# 	if name in friends:
# 		language = favorite_languages[name].title()
# 		print(f"\t{name.title()}、あなたの好きなプログラミング言語は{language}ですね！")

# for name in sorted(favorite_languages.keys()):
# 	print(f"{name.title()}、投票ありがとう。")

print("以下の言語が投票されました。")
for language in set(favorite_languages.values()):
	print(language.title())
	# setだと一意になり、重複をなくせる。