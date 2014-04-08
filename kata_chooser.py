import random

class KataChooser():
	LANG = {1:"JAVA", 2:"Python", 3:"Ruby", 4:"Golang", 5:"PHP", 6:"C++", 7:"Objective-C"}
	KATA = {1:"Args", 2:"Bank OCR", 3:"Bowling Game", 4:"FizzBuzz", 5:"Game of Life", 6:"Glided Rose", 7:"Leap Years", 8:"Medicine Clash", 9:"Minesweeper", 10:"Monty Hall", 11:"Phone Numbers", 12:"Poker Hands", 13:"Potter", 14:"Prime Factors", 15:"Reversi", 16:"Roman Numerals", 17:"String Calculator", 18:"Tennis", 19:"Train Reservation", 20:"Trivia", 21:"Yatzy"}
	
	def __init__(self):
		pass

	def chooser(self):
		question = self.choose_question()
		lang = self.choose_language()
		return "Kata: %s \nWith: %s" % (question, lang)

	def random_language(self):
		return random.randint(1, 7)

	def random_question(self):
		return random.randint(1, 21)

	def choose_language(self):
		idx = self.random_language()
		return self.LANG[idx]

	def choose_question(self):
		idx = self.random_question()
		return self.KATA[idx]

if __name__ == "__main__":
    print(KataChooser().chooser())