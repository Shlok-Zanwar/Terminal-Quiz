def calculations_lvl(store_ques, ques_left, no_ques, save_data):
	import random

	save_data = save_data
	store_ques = store_ques
	ques_left = ques_left
	no_ques = no_ques

	save = open(save_data, "a+")

	name = input("Enter your name : ")

	player_marks = 0
	total_marks = 0 
	current_lvl = 0


	for i in range (1,int(no_ques)+1):

		ran = random.randrange(0,ques_left[current_lvl])
		print("\n\nQuestion", i, ":", store_ques[current_lvl][ran].question)
		print("A]", store_ques[current_lvl][ran].option_a)
		print("B]", store_ques[current_lvl][ran].option_b)
		print("C]", store_ques[current_lvl][ran].option_c)
		print("D]", store_ques[current_lvl][ran].option_d)
		ans = input("Enter your Choice : ") 

		ques_left[current_lvl] = ques_left[current_lvl] - 1	

#to check ans is within a,b,c,d,A,B,C,D
		if ans!="a" and ans!="A" and ans!="b" and ans!="B" and ans!="c" and ans!="C" and ans!="d" and ans!="D" :
			ans = input("Option didn't match, try again : ")

#if correct ans (capital or small)
		if ans == store_ques[current_lvl][ran].answer or ans == chr(ord(store_ques[current_lvl][ran].answer) + 32):
			player_marks = player_marks + store_ques[current_lvl][ran].marks
			total_marks = total_marks + store_ques[current_lvl][ran].marks	
			del store_ques[current_lvl][ran]					
			if current_lvl != 2:
				current_lvl += 1

		else :
			total_marks = total_marks + store_ques[current_lvl][ran].marks
			del store_ques[current_lvl][ran]
			if current_lvl != 0:
				current_lvl -= 1		




	score = str(player_marks) + "/" + str(total_marks)
	
	save.write(name)
	save.write(" ==> ")
	save.write(score)
	save.write("\n")	

	print ("\n\nYou scored", score, ":)\n\n") 




def calculations_simple(store_ques, ques_left, save_data):
	import random

	save_data = save_data
	store_ques = store_ques
	ques_left = int(ques_left)
	no_ques = ques_left


	save = open(save_data, "a+")

	name = input("Enter your name : ")

	player_marks = 0
	total_marks = 0 

	for i in range (1,int(no_ques)+1):
		ran = random.randrange(0,ques_left)
		print("\n\nQuestion", i, ":", store_ques[ran].question)
		print("A]", store_ques[ran].option_a)
		print("B]", store_ques[ran].option_b)
		print("C]", store_ques[ran].option_c)
		print("D]", store_ques[ran].option_d)
		ans = input("Enter your Choice : ") 

		ques_left = ques_left - 1

#to check ans is within a,b,c,d,A,B,C,D
		if ans!="a" and ans!="A" and ans!="b" and ans!="B" and ans!="c" and ans!="C" and ans!="d" and ans!="D" :
			ans = input("Option didn't match, try again : ")

		if ans == store_ques[ran].answer or ans == chr(ord(store_ques[ran].answer) + 32):
			player_marks = player_marks + store_ques[ran].marks
			total_marks = total_marks + store_ques[ran].marks	
			del store_ques[ran]					


		else :
			total_marks = total_marks + store_ques[ran].marks
			del store_ques[ran]
		
	score = str(player_marks) + "/" + str(total_marks)
	
	save.write(name)
	save.write(" ==> ")
	save.write(score)
	save.write("\n")	

	print ("\n\nYou scored", score, ":)\n\n") 














		
