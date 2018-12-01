import sys
import os
import random
import threading

lock = threading.Lock()
prediction_list = []

class DecisionTree:
	def __init__(self, attr=None, value=None, left=None, right=None, data=None, label=None):
		self.attr = attr
		self.value = value
		self.left = left
		self.right = right
		self.data = data
		self.label = label


def read_data(dir, file_name):
	file_path = os.path.join(dir, file_name)
	file = open(file_path, 'r')
	lines = file.readlines()
	data = []
	for line in lines:
		data.append(line.split())

	return data


def get_attr_num(data):
	attr_num = 0
	attribute_len = len(data[0])-1
	for attribute_idx in range(1, attribute_len+1):
		# get value of each attribute
		attribute_set = set([sample[attribute_idx] for sample in data])
		attr_num = attr_num + len(attribute_set)

	return attr_num


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


def vote_majority(data):
	counts = get_counts(data)
	label = max(counts, key=counts.get)

	return label


def build_decision_tree(data, threshold, attr_num):
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
		if attr_num > 0 and len(best_left) != 0 and len(best_right) != 0:
			left_tree = build_decision_tree(best_left, threshold, attr_num-1)
			right_tree = build_decision_tree(best_right, threshold, attr_num-1)
			return DecisionTree(attr=best_attr, value=best_value, left=left_tree, right=right_tree)
		else:
			label = vote_majority(data)
			return DecisionTree(data=data, label=label)
	else:
		label = vote_majority(data)
		return DecisionTree(data=data, label=label)



def predict(test_data, decision_tree):
	prediction = []
	for sample in test_data:
		node = decision_tree

		# predict
		while node.label == None:
			if sample[node.attr] == node.value:
				node = node.left
			else:
				node = node.right
		prediction.append(node.label)

	return prediction


def get_confusion_matrix(data, prediction):
	label_set = set([sample[0] for sample in data])
	label_num = len(label_set)

	# initialize
	matrix = []
	for i in range(label_num):
		line = []
		for j in range(label_num):
			line.append(j)
		matrix.append(line)

	for i in range(len(data)):
		true = int(data[i][0])-1
		predict = int(prediction[i])-1
		matrix[true][predict] = matrix[true][predict] + 1

	return label_num, matrix

class Thread(threading.Thread):
	def __init__(self, ID, train_data, test_data, threshold, idx_num):
		threading.Thread.__init__(self)
		self.ID = ID
		self.train_data = train_data
		self.test_data = test_data
		self.threshold = threshold
		self.idx_num = idx_num

	def run(self):
		total_idx = []
		for i in range(1, len(self.train_data[0])):
			total_idx.append(i)
		cur_idx = random.sample(total_idx, self.idx_num)

		new_train_data = []
		for i in range(len(self.train_data)):
			sample = []
			sample.append(self.train_data[i][0])
			for j in range(self.idx_num):
				sample.append(self.train_data[i][cur_idx[j]])
			new_train_data.append(sample)

		new_test_data = []
		for i in range(len(self.test_data)):
			sample = []
			sample.append(self.test_data[i][0])
			for j in range(self.idx_num):
				sample.append(self.test_data[i][cur_idx[j]])
			new_test_data.append(sample)

		# get label number
		attr_num = get_attr_num(new_train_data)

		# build decision tree
		decision_tree = build_decision_tree(new_train_data, self.threshold, attr_num)

		# predict testing data
		prediction = predict(new_test_data, decision_tree)

		lock.acquire()
		prediction_list.append(prediction)
		lock.release()

def vote(prediction_list):
	iter_num = len(prediction_list)
	sample_num = len(prediction_list[0])
	prediction = []
	for i in range(sample_num):
		temp = []
		for j in range(iter_num):
			temp.append(prediction_list[j][i])
		counts = get_counts(temp)
		label = max(counts, key=counts.get)
		prediction.append(label)

	return prediction


if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Error input. Use: python3 DecisionTree.py train_file test_file]")

	train_file_name = sys.argv[1]
	test_file_name = sys.argv[2]

	# read in data
	dir = os.path.dirname(__file__)
	train_data = read_data(dir, train_file_name)
	test_data = read_data(dir, test_file_name)

	if train_file_name == "balance.scale.train":
		threshold = 0.1
		idx_num = 4
		iter = 30
	elif train_file_name == "nursery.train":
		threshold = 0.0
		idx_num = 8
		iter = 30
	elif train_file_name == "led.train":
		threshold = 0.2
		idx_num = 7
		iter = 30
	elif train_file_name == "synthetic.social.train":
		threshold = 0.1
		idx_num = 100
		iter = 10
	else:
		threshold = 0.0
		iter = 10		# iter times
		idx_num = random.randint(int((len(test_data[0])-1)/2), len(test_data[0])-1)	# attribute number

	thread_list = []
	for i in range(iter):
		thread = Thread(i, train_data, test_data, threshold, idx_num)
		thread.start()
		thread_list.append(thread)

	for t in thread_list:
		t.join()

	prediction = vote(prediction_list)

	# get confusion_matrix
	label_num, confusion_matrix = get_confusion_matrix(test_data, prediction)

	# output confusion_matrix
	for i in range(label_num):
		for j in range(label_num):
			sys.stdout.write(str(confusion_matrix[i][j]) + " ")
		sys.stdout.write("\n")


	# # get accuray
	# accurate = 0
	# for i in range(len(test_data)):
	# 	if test_data[i][0] == prediction[i]:
	# 		accurate = accurate + 1
	# accuracy = float(accurate) / len(test_data)
	# print(accuracy)

	# # get F-1 score
	# for i in range(label_num):
	# 	TP = confusion_matrix[i][i]
	# 	FN = sum(confusion_matrix[i]) - TP
	# 	FP = 0
	# 	for j in range(label_num):
	# 		FP = FP + confusion_matrix[j][i]
	# 	FP = FP - TP
	# 	F1 = float(2*TP/(2*TP+FN+FP))
	# 	print(F1)



