import sys
import os

def read_data(dir, file_name):
	file_path = os.path.join(dir, file_name)
	file = open(file_path, 'r')
	lines = file.readlines()
	data = []
	for line in lines:
		data.append(line.split())
	return data

def get_counts(data):
	# calculate times of each class
	counts = {}		
	for x in data:
		if data[0] not in counts:
			counts[data[0]] = 1
		else:
			counts[data[0]] += 1
	
	return counts


def get_gini_index(data):
	counts = get_counts(data)




def build_decision_tree(data):
	# recursively build decision tree until current_gain == 0
	current_gain = get_gini_index(data)




if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Error input. Use: python3 DecisionTree.py train_file test_file]")

	train_file_name = sys.argv[1]
	test_file_name = sys.argv[2]

	# read in data
	dir = os.path.dirname(__file__)
	train_data = read_data(dir, train_file_name)
	test_data = read_data(dir, test_file_name)

	decision_tree = build_decision_tree(train_data)