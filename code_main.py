import random
from classes.code_data import questions
from classes.code_data import storeques
from code_form import custom_form_lvl
from code_form import custom_form_simple

print("\033[91m"+"Welcome the project created by ;\nShlok Zanwar\nAditya Gambhir\nSairaj Pokale\nRishi Shrimali"+"\033[0m")

manual = input("\n\nTo read project manual press 1, else 0 : ")

if manual == "1":
	print("\nThis project lets you create your own quiz in a python syntax and lets you save the data of all the participants in a .txt file\nYou can create two types of quiz :\n\nI) Level-up quiz :- This lets you create a quiz with quesions of different level, everytime the participant answers a question correctly the level of question rises similarly if he/she could'nt guess the correct answer the level of question drops down. You can set the marks of every level while creating the quiz. Also in this quiz type there is a minimum question criteria for each level. You can obviously add extra questions.\nOur QUIZ is a level up quiz, you can attempt our quiz to get a clear idea about Level-up quiz.\n\nII) Basic quiz :- This is lets you create a simple quiz in python syntax. You have to specify the number of questions and then  enter them one by one. There is no minimum criteria for this quiz. You can allot marks to every quesion indivisually.\n\nThank You !!!")

choose = input("\n\nWelcome to the application.\n    1) Try our Level-up quiz\n    2) Create a Level-up quiz\n    3) Create a basic quiz\nEnter your choice : ")

 
if choose == "1":
	print("\nBefore entering into the quiz you can once check our points table.")
	import ourquizdata
	print("\n\nWelcome to our quiz, you will be given 10 questions to answer, the level of your question depends on the answer of your previous question.\nAll the best !!! :)\n\n")

	name = input("Enter your details ==>\nName : ")
	gr_no = input("GR Number : ")
	roll_no = input("Roll Number : ")
	

	player_marks = 0
	total_marks = 0
	current_lvl = 0
	ques_left = [10, 5, 5, 5, 6]


	for i in range(1,11):


		ran = random.randrange(0,ques_left[current_lvl])
		print("\n\nQuestion", i, ":", storeques.final_store[current_lvl][ran].question, "( level -", storeques.final_store[current_lvl][ran].lvl, ")\n" )
		print("A]", storeques.final_store[current_lvl][ran].option_a)
		print("B]", storeques.final_store[current_lvl][ran].option_b)
		print("C]", storeques.final_store[current_lvl][ran].option_c)
		print("D]", storeques.final_store[current_lvl][ran].option_d)
		ans = input("Enter your Choice : ") 

		ques_left[current_lvl] = ques_left[current_lvl] - 1	

	#to check ans is within a,b,c,d,A,B,C,D
		if ans!="a" and ans!="A" and ans!="b" and ans!="B" and ans!="c" and ans!="C" and ans!="d" and ans!="D" :
			ans = input("Option didn't match, try again : ")

	#if correct ans (capital or small)
		if ans == storeques.final_store[current_lvl][ran].answer or ans == chr(ord(storeques.final_store[current_lvl][ran].answer) + 32):
			player_marks = player_marks + storeques.final_store[current_lvl][ran].marks
			total_marks = total_marks + storeques.final_store[current_lvl][ran].marks	
			del storeques.final_store[current_lvl][ran]					
			if current_lvl != 4:
				current_lvl += 1
		else :
			total_marks = total_marks + storeques.final_store[current_lvl][ran].marks
			del storeques.final_store[current_lvl][ran]
			if current_lvl != 0:
				current_lvl -= 1

	


	player_percent = (player_marks/total_marks)*100
	player_percent = "{:.2f}".format(player_percent)
	print ("\n\nYou have complted your quiz :) Your score is", str(player_marks),"/",str(total_marks), "which is", str(player_percent),"%") 
	
	#temp = "[\""+name+"\", "+str(gr_no)+", "+str(roll_no)+", "+str(player_percent)+"]"
	#print (temp)
	
	temp =[]
	temp.append(name)	
	temp.append(gr_no)
	temp.append(roll_no)
	temp.append(player_percent)
	
	data_store = ourquizdata.data
	data_store.append(temp)	
	
	writeclr = open("ourquizdata.py", "w+")
	writeclr.write("\n")
	writeapp = open("ourquizdata.py", "a+")
	writeapp.write("from classes.data_func import sorter\n\n")
	writeapp.write("n = input(\"Press 1 if you want to see the participants score-list, 0 to continue : \")\n\n") 
	writeapp.write("data = ")
	writeapp.write(str(data_store))
	writeapp.write("\nif n == \"1\":")
	writeapp.write("\n	sorter(data)")
	 


elif choose == "2":
	custom_form_lvl()

elif choose == "3":
	custom_form_simple()

 
import ourquizfeedback

feed_new = int(input("\n\nThanks for using our application, please enter your feedback (0, 10) : "))
feed_old = int(ourquizfeedback.feedback)
number = int(ourquizfeedback.no_people)
feed_old = feed_old*number
number = number + 1 
feed_old = feed_old + feed_new
feed_old = feed_old/number

feedclr = open("ourquizfeedback.py", "w+")
feedclr.write("\n")
feedapp = open("ourquizfeedback.py", "a+")
feedapp.write("feedback = ")
feedapp.write(str(feed_old))
feedapp.write("\nno_people = ")
feedapp.write(str(number))







