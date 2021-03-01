# 1.モジュールをインポートして、関数名そのままで利用する得
# import pizza

# pizza.make_pizza(16, 'ペパロニ')
# pizza.make_pizza(12, 'マッシュルーム', 'ピーマン', 'エクストラチーズ')


# 2.モジュールに別名をつける時
# import pizza as p

# p.make_pizza(16, 'ペパロニ')
# p.make_pizza(12, 'マッシュルーム', 'ピーマン', 'エクストラチーズ')



# 3.特定の関数をインポートする時
# from pizza import make_pizza

# make_pizza(16, 'ペパロニ')
# make_pizza(12, 'マッシュルーム', 'ピーマン', 'エクストラチーズ')


# 4.特定の関数をインポートかつ別名で利用する時
# from pizza import make_pizza as mp

# mp(16, 'ペパロニ')
# mp(12, 'マッシュルーム', 'ピーマン', 'エクストラチーズ')


# 5.モジュールのすべての関数をインポートする時
from pizza import *

make_pizza(16, 'ペパロニ')
make_pizza(12, 'マッシュルーム', 'ピーマン', 'エクストラチーズ')