from random import choice

class RandomWalk():
	'''Generate randome data class'''
	
	def __init__(self, num_points = 5000):
		self.num_points = num_points
		
		self.x_values = [0]
		self.y_values = [0]
		
	def fill_walk(self):
		'''Compute all random points'''
		
		#go ahead untill reach to the target
		while len(self.x_values) < self.num_points:
			
			#decide the distance and dirction 
			x_direction = choice([1,-1])
			x_distance =choice([0,1,2,3,5,10])
			x_step = x_direction * x_distance
			
			y_direction = choice([1,-1])
			y_distance = choice([0,1,2,3,4])
			y_step = y_direction * y_distance
			
			if x_step == 0 and y_step == 0:
				continue
			
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step
			
			self.x_values.append(next_x)
			self.y_values.append(next_y)