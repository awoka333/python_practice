"""
class Dog:
	def __init__(self, name, weight):
		self.name = name	   # self.nameはパブリック変数
		self.__weight = weight # self.__weightはプライベート変数

pochi = Dog('ポチ', 20)
print(pochi.name)
# print(pochi.__weight) エラーとなる
"""

class Dog:
	def __init__(self, name, weight):
		self.name = name
		self.__weight = weight

	def getWeight(self):		 # __weightのゲッター
		return self.__weight

	def setWeight(self, weight): # __weightのセッター
		self.__weight = weight

pochi = Dog('ポチ', 20)
print(pochi.getWeight())
pochi.setWeight(25)
print(pochi.getWeight())