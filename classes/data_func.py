def sorter(data):
	data = data

	print("\nEnter the way you want to sort\n    1)GR Number\n    2)Roll Number\n    3)Percentage")
	in1 = input("Enter your choice : ")
	
	data.sort(key=lambda x: x[int(in1)])
	print(data)
	if in1 == "3":
		data.reverse()


	print("\n\nSr.No    Name                GR Number      Roll Number    Percentage\n")

	i = 0
	while i<len(data):
		p = i+1 

		store = str(p)
		while len(store) < 9:
			store = store + " "		

		store = store + str(data[i][0])
		while len(store) < 29:
			store = store + " "


		store = store + str(data[i][1])
		while len(store) < 44:
			store = store + " "

		store = store + str(data[i][2])
		while len(store) < 59:
			store = store + " "

		store = store + str(data[i][3])+"%"
		while len(store) < 67:
			store = store + " "
		
		print(store)
		i = i+1
		
	
