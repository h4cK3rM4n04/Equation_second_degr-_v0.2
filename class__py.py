from math import *

class EQ_2nd_degre:

	def __init__(self, a, b, c, Name_eq):

		self.a = a
		self.b = b
		self.c = c
		self.Name_eq = Name_eq

	def Delta_0(self):
		D = (self.b ** 2) - 4 * (self.a) * (self.c)

		if D < 0:
			return f"Delta = {D} comme il est négatif, il n'y a pas de solution possible pour {self.Name_eq}\n"

		elif D > 0:
			x_1 = -self.b - sqrt(D) / 2 * self.a
			x_2 = -self.b + sqrt(D) / 2 * self.a
			return f"Il y à deux solutions possible:	|x_1 = {x_1} et x_2 = {x_2}|	 car Delta = {D} pour {self.Name_eq}\n Demonstration: x_1 = -{self.b} - sqrt({D}) / 2 * {self.a}\n 				x_2 = -{self.b} + sqrt({D}) / 2 * {self.a}\n"

		elif D == 0:
			x_0 = -self.b / 2 * self.a
			return f"Comme Delta = 0 il n'y à qu'une seule solution possible x_0 = {x_0} pour {self.Name_eq}\n Demonstration: x_0 = -{self.b} / 2 * {self.a}\n"