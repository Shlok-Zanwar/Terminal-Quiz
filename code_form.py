def custom_form_lvl():

	file_name = input("\n\nEnter the name you want to give to your quiz (with .py extention)\n==>")
	save_data = input("\nEnter the name you want to get your quiz participants data (with .txt extention)\n==>")


	mainform = open(file_name, "w+")
	mainform.write("\n")
	mainform = open(file_name, "a+")

	print("\n\nHello you will be able to create a lvl up quiz in python language using this application.\nTo access quiz enter \" python3", file_name,"\".\nYou can see the data of the people who gave the test in \"",save_data,"\".\n\n")

	mainform.write("from classes.code_func import calculations_lvl\n")
	mainform.write("from classes.code_data import questions\n")

	title = input("Enter the title of your Quiz :)\n==>")

	mainform.write("print(\"")
	mainform.write(title)
	mainform.write("\")\n")
	mainform.write("\n")
	mainform.write("print(\"\")\n")
	mainform.write("print(\"\")\n")

	heading = input("\nEnter the heading of your Quiz (to break line enter backslash and the n, thenc ontinue writing) \n==>")

	mainform.write("print(\"")
	mainform.write(heading)
	mainform.write("\")\n")
	mainform.write("\n")
	mainform.write("print(\"\")\n")


	in_ques = 0

	while int(in_ques) < 3:
		in_ques = int(input("\nEnter the number of questions you want to display in quiz (minimum 3): "))
 
	ques_diff_0 = 0
	ques_diff_1 = 0
	ques_diff_2 = 0

	print("\nEnter the number of questions in difficulty 1 (minimum -", in_ques,")")
	while ques_diff_0 < in_ques:
		ques_diff_0 = int(input("> "))	

	print("Enter the number of questions in difficulty 2 (minimum -", in_ques-1,")")
	while ques_diff_1 < in_ques-1:
		ques_diff_1 = int(input("> "))	

	print("Enter the number of questions in difficulty 3 (minimum -", in_ques-2,")")
	while ques_diff_2 < in_ques-2:
		ques_diff_2 = int(input("> "))	


	no_ques = [ques_diff_0, ques_diff_1, ques_diff_2]

	marks_arr = []
	marks = int(input("\nEnter marks for difficulty lvl 1 : "))
	marks_arr.append(marks)
	marks = int(input("Enter marks for difficulty lvl 2 : "))
	marks_arr.append(marks)
	marks = int(input("Enter marks for difficulty lvl 3 : "))
	marks_arr.append(marks)
	  

	store = ""
	store_ques = "["
	
	for diff in range (0,3):
		store_ques = store_ques+"["

		for i in range (0,int(no_ques[diff])):

			print("\n\nEnter Question", i+1, "- Difficulty", diff+1, "==>")
			ques = input()

			option_A = input("A] : ")

			option_B = input("B] : ")

			option_C = input("C] : ")	

			option_D = input("D] : ")
	
			ans = input("Enter corrct option (capital) : ")

			store = "Q"+str(diff)+str(i)+" = questions(\""+ques+"\", \""+option_A+"\", \""+option_B+"\", \""+option_C+"\", \""+option_D+"\", \""+ans+"\", "+str(diff)+", "+str(marks_arr[diff])+")"

			mainform.write(store)
			mainform.write("\n")

			if i == int(no_ques[diff])-1:
				store_ques = store_ques+"Q"+str(diff)+str(i)
			else:
				store_ques = store_ques+"Q"+str(diff)+str(i)+", "

		if diff == 2:
			store_ques = store_ques+"]"
		else:
			store_ques = store_ques+"], "


	store_ques = store_ques+"]"

	mainform.write("\nstore_ques = ")
	mainform.write(store_ques)
	mainform.write("\n\n")

	mainform.write("ques_left = ")
	mainform.write(str(no_ques))
	mainform.write("\n\n")
		

	mainform.write("calculations_lvl(store_ques, ques_left, ")
	mainform.write(str(in_ques))
	mainform.write(", \"")
	mainform.write(save_data)
	mainform.write("\")\n")







def custom_form_simple():
	
	file_name = input("\n\nEnter the name you want to give to your quiz (with .py extention)\n==>")
	save_data = input("\nEnter the name you want to get your quiz participants data (with .txt extention)\n==>")


	mainform = open(file_name, "w+")
	mainform.write("\n")
	mainform = open(file_name, "a+")

	print("\n\nHello you will be able to create a quiz in python language using this application.\nTo access quiz enter \"python3", file_name,"\".\nYou can see the data of the people who gave the test in \"",save_data,"\".\n\n")

	mainform.write("from classes.code_func import calculations_simple\n")
	mainform.write("from classes.code_data import questions\n")

	title = input("Enter the title of your Quiz :)\n==>")

	mainform.write("print(\"")
	mainform.write(title)
	mainform.write("\")\n")
	mainform.write("\n")
	mainform.write("print(\"\")\n")
	mainform.write("print(\"\")\n")

	heading = input("\nEnter the heading of your Quiz (to break line enter backslash and the n, thenc ontinue writing)\n==>")

	mainform.write("print(\"")
	mainform.write(heading)
	mainform.write("\")\n")
	mainform.write("\n")
	mainform.write("print(\"\")\n")

	in_ques = int(input("\nEnter the number of questions : "))
	no_ques = in_ques

	i=0
	store = ""
	store_ques = "["
	while i < in_ques:
		print("\n\nEnter Question", i+1, "==>")
		ques = input()

		option_A = input("A] : ")

		option_B = input("B] : ")

		option_C = input("C] : ")	

		option_D = input("D] : ")
	
		ans = input("Enter corrct option (capital) : ")

		marks = input("Enter marks for this question : ")

		store = "Q"+str(i)+" = questions(\""+ques+"\", \""+option_A+"\", \""+option_B+"\", \""+option_C+"\", \""+option_D+"\", \""+ans+"\", "+str(0)+", "+marks+")"

		mainform.write(store)
		mainform.write("\n")

		if i == in_ques-1:
			store_ques = store_ques+"Q"+str(i)+"]"
		else:
			store_ques = store_ques+"Q"+str(i)+", "
		
		i = i+1

	mainform.write("\nstore_ques = ")
	mainform.write(store_ques)
	mainform.write("\n\n")

	mainform.write("ques_left = ")
	mainform.write(str(no_ques))
	mainform.write("\n\n")

	mainform.write("calculations_simple(store_ques, ques_left, \"")
	mainform.write(save_data)
	mainform.write("\")\n")
		



		 

	










