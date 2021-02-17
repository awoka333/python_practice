import requests

# API呼び出しを作成してそのレスポンスを格納する
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"ステータスコード： {r.status_code}")

# APIレスポンスを変数に格納する
response_dict = r.json()

# 結果を処理する
print(response_dict.keys())

print(f"全リポジトリ数： {response_dict['total_count']}")

# リポジトリに関する情報を調べる
repo_dicts = response_dict['items']
print(f"情報が返されたリポジトリの数： {len(repo_dicts)}")

# 1つ目のリポジトリを調査する
repo_dict = repo_dicts[0]
print(f"\nキーの数： {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
# 	print(key)

print("\n1つ目のリポジトリの情報抜粋：")
print(f"名前： {repo_dict['name']}")
print(f"所有者： {repo_dict['owner']['login']}")
print(f"スターの数： {repo_dict['stargazers_count']}")
print(f"リポジトリURL： {repo_dict['html_url']}")
print(f"作成日時： {repo_dict['created_at']}")
print(f"最終更新日時： {repo_dict['updated_at']}")
print(f"説明文： {repo_dict['description']}")