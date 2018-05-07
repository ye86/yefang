
from engine_eazy import *

########################################################################

class App(App_):
	def make_obj(self):
		for x in range(3):
			for y in range(3):
				for z in range(3):
					self.obj.append2(square,(P(x*2,y*2,z*2),P(1,0,0),P(0,1,0),P(0,0,1)))
				
	

if __name__ == "__main__":
	app = App()
	app.main()





