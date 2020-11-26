class questions:
	def __init__(self, question, option_a, option_b, option_c, option_d, answer, lvl, marks):
		self.question = question
		self.option_a = option_a
		self.option_b = option_b
		self.option_c = option_c
		self.option_d = option_d
		self.answer = answer
		self.lvl = lvl
		self.marks = marks


class storeques:
	L0_Q0 = questions("If A + B means A is the mother of B; A - B means A is the brother B; A % B means A is the father of B and A x B means A is the sister of B, which of the following shows that P is the maternal uncle of Q?", "Q - N + M x P", "P + S x N - Q", "P - M + N x Q", "Q - S % P", "C", 0, 10)
	L0_Q1 = questions("In the following questions choose the word which is the exact OPPOSITE of the given word : RELINQUISH", "Abdicate", "Renounce", "Possess", "Deny", "C", 0, 10)
	L0_Q2 = questions("Alfred buys an old scooter for Rs. 4700 and spends Rs. 800 on its repairs. If he sells the scooter for Rs. 5800, his gain percent is:", "4.57%", "5.45%", "10%", "12%", "B", 0, 10)
	L0_Q3 = questions("For which of the following disciplines is Nobel Prize awarded?", "Physics and Chemistry", "Physiology or Medicine", "Literature, Peace and Economics", "All of the above", "D", 0, 10)
	L0_Q4 = questions("Hitler party which came into power in 1933 is known as", "Labour Party", "Nazi Party", "Ku-Klux-Klan", "Democratic Party", "B", 0, 10)
	L0_Q5 = questions("Friction can be reduced by changing from", "sliding to rolling", "rolling to sliding", "potential energy to kinetic energy", "dynamic to static", "A", 0, 10)
	L0_Q6 = questions("A right triangle with sides 3 cm, 4 cm and 5 cm is rotated the side of 3 cm to form a cone. The volume of the cone so formed is:", "12(pi) cm3", "15(pi) cm3", "16(pi) cm3", "20(pi)", "A", 0, 10)
	L0_Q7 = questions("In a shower, 5 cm of rain falls. The volume of water that falls on 1.5 hectares of ground is:", "75 cu. m", "750 cu. m", "7500 cu. m", "75000 cu. m", "B", 0, 10)
	L0_Q8 = questions("In the question below a sentence has been given in Active/Passive voice. From the given alternatives, choose the one which best expresses the given sentence in Passive/Active voice :\nAfter driving professor Kumar to the museum she dropped him at his hotel.", "After being driven to the museum, Professor Kumar was dropped at his hotel.", "Professor Kumar was being driven dropped at his hotel.", "After she had driven Professor Kumar to the museum she had dropped him at his hotel.", "After she was driven Professor Kumar to the museum she had dropped him at his hotel.", "A", 0, 10)
	L0_Q9 = questions("The problem consists of three statements. Based on the first two statements, the third statement may be true, false, or uncertain.\nTanya is older than Eric.\nCliff is older than Tanya.\nEric is older than Cliff.\nIf the first two statements are true, the third statement is", "True", "False", "Uncertain", "Not enough data", "B", 0, 10)


	L1_Q0 = questions("Father is aged three times more than his son Ronit. After 8 years, he would be two and a half times of Ronit's age. After further 8 years, how many times would he be of Ronit's age?", "2 times", "2.5 times", "2.75 times", "3 times", "A", 1, 15)
	L1_Q1 = questions("Extreme old age when a man behaves like a fool", "Imbecility", "Senility", "Dotage", "Superannuation", "C", 1, 15)
	L1_Q2 = questions("In each question below is given a statement followed by two conclusions numbered I and II. You have to assume everything in the statement to be true, then consider the two conclusions together and decide which of them logically follows beyond a reasonable doubt from the information given in the statement.\nStatements: In a one day cricket match, the total runs made by a team were 200. Out of    these 160 runs were made by spinners.\nConclusions:\nI. 80% of the team consists of spinners.\nII. The opening batsmen were spinners.", "Only conclusion I follows", "Only conclusion II follows", "Neither I nor II follows", "Both I and II follow", "C", 1, 15)
	L1_Q3 = questions("Which scientist discovered the radioactive element radium?", "Isaac Newton", "Albert Einstein", "Benjamin Franklin", "Marie Curie", "D", 1, 15)
	L1_Q4 = questions("A motorboat, whose speed in 15 km/hr in still water goes 30 km downstream and comes back in a total of 4 hours 30 minutes. The speed of the stream (in km/hr) is:", "4", "5", "6", "10", "B", 1, 15)



	L2_Q0 = questions("Statements: All bags are cakes. All lamps are cakes.\nConclusions:\nI. Some lamps are bags.\nII. No lamp is bag.", "Only conclusion I follows", "Only conclusion II follows", "Either I or II follows", "Neither I nor II follows", "C", 2, 20)
	L2_Q1 = questions("A man standing at a point P is watching the top of a tower, which makes an angle of elevation of 30° with the man's eye. The man walks some distance towards the tower to watch its top and the angle of the elevation becomes 60°. What is the distance between the base of the tower and the point P?", "43 units", "8 units", "12 units", "Data inadequate", "D", 2, 20)
	L2_Q2 = questions("A bag contains 2 red, 3 green and 2 blue balls. Two balls are drawn at random. What is the probability that none of the balls drawn is blue?", "10/21", "11/21", "2/7", "5/7", "A", 2, 20)
	L2_Q3 = questions("What is the probability of getting a sum 9 from two throws of a dice?", "1/6", "1/8", "1/9", "1/12", "C", 2, 20)
	L2_Q4 = questions("Who is largely responsible for breaking the German Enigma codes, created a test that provided a foundation for artificial intelligence?", "Alan Turing", "Jeff Bezos", "George Boole", "Charles Babbage", "A", 2, 20)


	L3_Q0 = questions("In this series, you will be looking at both the letter pattern and the number pattern. Fill the blank in the middle of the series or end of the series:\nB2CD, B5CD, BC6D _____, BCD4, ", "B2C2D", "BC3D", "B2C3D", "BCD7", "B", 3, 25)
	L3_Q1 = questions("What is laughing gas?", "Nitrous Oxide", "Carbon monoxide", "Sulphur dioxide", "Hydrogen peroxide", "A", 3, 25)
	L3_Q2 = questions("David gets on the elevator at the 11th floor of a building and rides up at the rate of 57 floors per minute. At the same time, Albert gets on an elevator at the 51st floor of the same building and rides down at the rate of 63 floors per minute. If they continue travelling at these rates, then at which floor will their paths cross ?", "19", "28", "30", "37", "C", 3, 25)
	L3_Q3 = questions("Some proverbs/idioms are given below together with their meanings. Choose the correct meaning of proverb/idiom, If there is no correct meaning given, E (i.e.) 'None of these' will be the answer. :\nTo beg the question", "To refer to", "To take for granted", "To raise objections", "To be discussed", "B", 3, 25)
	L3_Q4 = questions("What was the day of the week on 28th May, 2006?", "Thursday", "Friday", "Saturday", "Sunday", "D", 3, 25)



	L4_Q0 = questions("Mycobacterium leprae causes leprosy, Corynebacterium diphtheria causes diphtheria and Vibrio comma causes ?", "tetanus", "influenza", "cholera", "typhoid", "C", 4, 30)
	L4_Q1 = questions("A, B, C, D and E are sitting on a bench. A is sitting next to B, C is sitting next to D, D is not sitting with E who is on the left end of the bench. C is on the second position from the right. A is to the right of B and E. A and C are sitting together. In which position A is sitting ?", "Between B and D", "Between B and C", "Between E and D", "Between C and E", "B", 4, 30)
	L4_Q2 = questions("What is RISC?", "Remodeled Interface System Computer", "Remote Intranet Secured Connection", "Runtime Instruction Set Compiler", "Reduced Instruction Set Computer", "D", 4, 30)
	L4_Q3 = questions("The half life period of an isotope is 2 hours. After 6 hours what fraction of the initial quantity of the isotope will be left behind?", "1/6", "1/3", "1/8", "1/4", "C", 4, 30)
	L4_Q4 = questions("The calendar for the year 2007 will be the same for the year:", "2014", "2015", "2017", "2018", "D", 4, 30)
	L4_Q5 = questions("How many 4-letter words with or without meaning, can be formed out of the letters of the word, 'LOGARITHMS', if repetition of letters is not allowed?", "40", "400", "5040", "2520", "C", 4, 30)



	final_store = [
			[L0_Q0, L0_Q1, L0_Q2, L0_Q3, L0_Q4, L0_Q5, L0_Q6, L0_Q7, L0_Q8, L0_Q9],
			[L1_Q0, L1_Q1, L1_Q2, L1_Q3, L1_Q4],
			[L2_Q0, L2_Q1, L2_Q2, L2_Q3, L2_Q4],
			[L3_Q0, L3_Q1, L3_Q2, L3_Q3, L3_Q4],
			[L4_Q0, L4_Q1, L4_Q2, L4_Q3, L4_Q4, L4_Q5]
		      ]


