import sys
import os

threshold = 0.0

class DecisionTree:
	def __init__(self, attr=None, value=None, left=None, right=None, data=None):
		self.attr = attr
		self.value = value
		self.left = left
		self.right = right
		self.data = data


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
	# {class1: count1, class2: count2, class3:count3...}
	counts = {}		
	for x in data:
		if x[0] not in counts:
			counts[x[0]] = 1
		else:
			counts[x[0]] += 1

	return counts


def get_gini_index(data):
	# calculate gini index
	counts = get_counts(data)
	total = len(data)
	temp = 0.0

	for i in counts:
		temp += pow(counts[i]/total, 2)

	return 1-temp


def split_node(data, value, attribute_idx):
	child1 = []	
	child2 = []
	for sample in data:
		if sample[attribute_idx] == value:
			child1.append(sample)
		else:
			child2.append(sample)

	return child1, child2



def build_decision_tree(data):
	# recursively build decision tree until current_gain == 0
	attribute_len = len(data[0])-1
	sample_len = len(data)
	
	min_gain = float("inf")
	best_attr = None
	best_value = None
	best_left = None
	best_right = None

	for attribute_idx in range(1, attribute_len+1):
		# get value of each attribute
		attribute_set = set([sample[attribute_idx] for sample in data])
		for value in attribute_set:
			child1, child2 = split_node(data, value, attribute_idx)
			p = len(child1)/sample_len
			gain = p * get_gini_index(child1) + (1 - p) * get_gini_index(child2)
			if gain < min_gain:
				min_gain = gain
				best_attr = attribute_idx
				best_value = value
				best_left = child1
				best_right = child2

	if min_gain > threshold:
		left_tree = build_decision_tree(best_left)
		right_tree = build_decision_tree(best_right)
		return DecisionTree(attr=best_attr, value=best_value, left=left_tree, right=right_tree)
	else:
		return DecisionTree(data=data)



if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Error input. Use: python3 DecisionTree.py train_file test_file]")

	train_file_name = sys.argv[1]
	test_file_name = sys.argv[2]

	# read in data
	dir = os.path.dirname(__file__)
	train_data = read_data(dir, train_file_name)
	test_data = read_data(dir, test_file_name)

	# build decision tree
	decision_tree = build_decision_tree(train_data)
	print(decision_tree.value)