from game_objects.Items.Chestplate import Chestplate

from game_objects.Utils.Math import Math

math = Math()

class LeatherLamellar(Chestplate):
	def __init__(self):
		self.name = "Leather Lamellar Chestplate"
		self.defense = 1.2
		self.weight = math.convert_kg_lb(5)
		self.desc = "Body armour, made from small rectangular plates of  leather laced into horizontal rows."
		
		super().__init__(self.name, self.defense, self.weight)