def make_dragon():
	print("")
	print("       \****__              ____          ")                                  
	print("         |    *****\_      --/ *\-__       ")                                 
	print("         /_          (_    ./ ,/----'      ")                                 
	print("           \__         (_./  /             ")                                 
	print("              \__           \___----^__    ")                                 
	print("               _/   _                  \   ")                                 
	print("        |    _/  __/ )\ \ _____         *\ ")                                 
	print("        |\__/   /    ^ ^       \_________| ")

number_of_dragons = input("How many dragons? ")

if number_of_dragons > 0:
	for x in range(0, number_of_dragons):
		make_dragon()
	print("")
else:
	print("There must be a valid number")
