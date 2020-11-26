
from classes.data_func import sorter

n = input("Press 1 if you want to see the participants score-list, 0 to continue : ")

data = [['Shlok Zanwar', '21910163', '7011', '100.00'], ['Rohan', '21910000', '7030', '26.09']]
if n == "1":
	sorter(data)