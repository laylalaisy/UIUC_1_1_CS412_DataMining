
# coding: utf-8

# In[1]:


# Problem 1, 2, 3
import numpy as np
from numpy.linalg import norm

Midterm = np.array([95, 86, 78, 99, 84, 90, 88, 75, 96, 96])
Final = np.array([88, 88, 90, 95, 85, 77, 99, 80, 100, 80])


# ## Problem 1

# In[2]:


# 1(a) Max and Min
# Max
def getMax(array):
    max = 0
    for item in array:
        if item > max:
            max = item
    # return np.max(array)
    return max

Midterm_Max = getMax(Midterm)
print("Midterm Max:", Midterm_Max)
Final_Max = getMax(Final)
print("Final Max:", Final_Max)

# Min
def getMin(array):
    min = 1000
    for item in array:
        if item < min:
            min = item
    # return np.min(array)
    return min

Midterm_Min = getMin(Midterm)
print("Midterm Min:", Midterm_Min)
Final_Min = getMin(Final)
print("Final Min:", Final_Min)


# In[3]:


# 1(b) Mean, mode and median
# Mean
def getMean(array):
    sum = 0
    for item in array:
        sum = sum + item
    amount = len(array)
    mean = sum / amount
    return mean

Midterm_Mean = getMean(Midterm)
print("Midterm Mean:", Midterm_Mean)
Final_Mean = getMean(Final)
print("Fianl Mean:", Final_Mean)

# Mode
def getMode(array):
    counts = np.bincount(array)    # get frequncy
    max_count = getMax(counts)     # get highest frequency
    
    return np.where(counts==max_count)

Midterm_Mode = getMode(Midterm)
print("Midterm Mode:", Midterm_Mode)
Final_Mode = getMode(Final)
print("Final Mode:", Final_Mode)

# Median
def getMedian(array):
    return np.median(array)

Midterm_Median = getMedian(Midterm)
print("Midterm Median:", Midterm_Median)
Final_Median = getMedian(Final)
print("Final Median:", Final_Median)


# In[4]:


# 1(c)First Quartile, Third Quartile and Inter-quartile Range
# First Quartile
def getFirstQuartile(array):
    array = np.sort(array)    # sort array
    length = len(array)
    mid = (int)(length / 2)
    first = (int)(mid / 2)
    third = mid + first
    
    if length >= 4:    
        if mid % 2== 0:
            first_quartile = (array[first-1] + array[first]) / 2
            third_quartile = (array[third-1] + array[third+1]) / 2
        else:
            first_quartile = array[first]
            third_quartile = array[third]
    
    inter_quartile = third_quartile - first_quartile 
    
    return array, first_quartile, third_quartile, inter_quartile
    
[Midterm_Sorted, Midterm_First_Quartile, Midterm_Third_Quartile, Midterm_Inter_Quartile] = getFirstQuartile(Midterm)
print("Midterm Sorted Array:", Midterm_Sorted)
print("Midterm First Quartile:", Midterm_First_Quartile)
print("Midterm Third Quartile:", Midterm_Third_Quartile)
print("Midterm Inter Quartile:", Midterm_Inter_Quartile)
[Final_Sorted, Final_First_Quartile, Final_Third_Quartile, Final_Inter_Quartile] = getFirstQuartile(Final)
print("Final Sorted Array:", Final_Sorted)
print("Final First Quartile:",Final_First_Quartile)
print("Final Third Quartile:", Final_Third_Quartile)
print("Final Inter Quartile:", Final_Inter_Quartile)


# In[5]:


# 1(d)Variance (Sample & Population)
def getVariancePopulation(array):
    length = len(array)
    square_sum = 0
    mean = getMean(array)
    
    for item in array:
        square_sum = square_sum + (item - mean) * (item - mean)  
    
    population_var = round(square_sum / length, 3)
    
    # return np.var(array)
    return population_var

def getVarianceSample(array):
    length = len(array)
    square_sum = 0
    mean = getMean(array)
    
    for item in array:
        square_sum = square_sum + (item - mean) * (item - mean)  
    
    sample_var = round(square_sum / (length - 1) , 3)
    
    # return np.var(array)
    return sample_var

Midterm_Population_Variance = getVariancePopulation(Midterm)
print("Midterm Population Variance:", Midterm_Population_Variance)
Midterm_Sample_Variance = getVarianceSample(Midterm)
print("Midterm Sample Variance:", Midterm_Sample_Variance)
Final_Population_Variance = getVariancePopulation(Final)
Final_Sample_Variance = getVarianceSample(Final)
print("Final Population Variance:", Final_Population_Variance)
print("Final Sample Variance:", Final_Sample_Variance)                


# In[6]:


# 1(e)Standard Deviation
def getStandardDeviationPopulation(array):
    # return np.std(array)
    return round(np.sqrt(getVariancePopulation(array)),3)

def getStandardDeviationSample(array):
    # return np.std(array)
    return round(np.sqrt(getVarianceSample(array)), 3)

Midterm_Standard_Population_Deviation = getStandardDeviationPopulation(Midterm)
print("Midterm Standard Population Deviation:", Midterm_Standard_Population_Deviation)
Midterm_Standard_Sample_Deviation = getStandardDeviationSample(Midterm)
print("Midterm Standard Sample Deviation:", Midterm_Standard_Sample_Deviation) 
Final_Standard_Population_Deviation = getStandardDeviationPopulation(Final)
print("Final Standard Population Deviation:", Final_Standard_Population_Deviation)
Final_Standard_Sample_Deviation = getStandardDeviationSample(Final)
print("Final Standard Sample Deviation:", Final_Standard_Sample_Deviation)  


# ## Problem 2

# In[7]:


# 2(a) Min-Max Normalization
def getMinMaxNormalization(array):
    old_min = getMin(array)
    old_max = getMax(array)
    new_min = 0
    new_max = 1
    
    new_list = []
    for item in array:
        new_list.append(round((item-old_min)/(old_max-old_min)*(new_max-new_min)+new_min,3))
        
    new_array = np.array(new_list)
    return new_array

Midterm_MinMax_Normalization = getMinMaxNormalization(Midterm)

print("Midterm MinMax Normalization Student 1:", Midterm_MinMax_Normalization[0])
print("Midterm MinMax Normalization Student 2:", Midterm_MinMax_Normalization[1])
print("Midterm MinMax Normalization Student 3:", Midterm_MinMax_Normalization[2])


# In[8]:


# 2(b) Variance(Population) of Min-Max Normalization
def getVarianceMinMaxNormalization(array):
    new_array = getMinMaxNormalization(array)
    return getVariancePopulation(new_array)

Midterm_Variance_MinMax_Normalization = getVarianceMinMaxNormalization(Midterm)
print("Midterm Variance MinMax Normalization:", Midterm_Variance_MinMax_Normalization)


# In[9]:


# 2(c) Z-Score Normalizaion
def getZScoreNormalization(array):
    mean = getMean(array)
    std = getStandardDeviationPopulation(array)
    
    new_list = []
    for item in array:
        new_list.append(round((item-mean)/std,3))
    
    new_array = np.array(new_list)
    return new_array

Final_ZScore_Normalization = getZScoreNormalization(Final)
print("Final ZScore Normalization Student 4:", Final_ZScore_Normalization[3])
print("Final ZScore Normalization Student 5:", Final_ZScore_Normalization[4])
print("Final ZScore Normalization Student 6:", Final_ZScore_Normalization[5])


# In[10]:


# 2(d) Variance(Population) of Z-Score Normalization
def getVarianceZScoreNormalization(array):
    new_array = getZScoreNormalization(array)
    return getVariancePopulation(new_array)

Final_Variance_ZScore_Normalization = getVarianceZScoreNormalization(Final)
print("Final Variance ZScore Normalization:", Final_Variance_ZScore_Normalization)


# ## Problem 3

# In[11]:


# 3(a) Covariance(population)
def getCovariancePopulation(array1, array2):
    mean1 = getMean(array1)
    mean2 = getMean(array2)
    length = len(array1)
    
    covariance = sum(array1 * array2) / length - mean1 * mean2
    return round(covariance, 3)

Covariance = getCovariancePopulation(Midterm, Final)
print("Covariance:", Covariance)


# In[12]:


# 3(b) Pearson's Correlation Coefficient
def getPearsonCorrelation(array1, array2):
    covariance = getCovariancePopulation(array1, array2)
    std1 = getStandardDeviationPopulation(array1)
    std2 = getStandardDeviationPopulation(array2)
    
    pearson = covariance / (std1 * std2)
    return round(pearson, 3)

PearsonCorrelation = getPearsonCorrelation(Midterm, Final)
print("Peasrson Correlation Coefficient:", PearsonCorrelation)


# In[13]:


# 3(d) Distance 
# Manhattan Distance
def getManhattan(array1, array2):
    length = len(array1)
    
    sum = 0
    for iter in range(length):
        sum = sum + abs(array1[iter] - array2[iter])
    
    return sum

Manhattan = getManhattan(Midterm, Final)
print("Manhattan Distance:", Manhattan)

# Euclidean Distance
def getEuclidean(array1, array2):
    length = len(array1)
    
    sum = 0
    for iter in range(length):
        sum = sum + pow((array1[iter] - array2[iter]),2)
    
    return round(pow(sum, 0.5), 3)

Euclidean = getEuclidean(Midterm, Final)
print("Euclidean Distance:", Euclidean)

# Supremum Distance
def getSupremum(array1, array2):
    length = len(array1)
    
    max = 0
    for iter in range(length):
        temp = abs(array1[iter] - array2[iter])
        if max < temp:
            max = temp
    
    return round(temp, 3)

Supremum = getSupremum(Midterm, Final)
print("Supremum Distance:", Supremum)

# Cosine Similarity
def getCosineSimilarity(array1, array2):
    cosine = np.dot(array1, array2) / (pow(sum(pow(array1, 2)), 0.5) * pow(sum(pow(array2, 2)),0.5))
    
    #return np.dot(array1, array2) / (norm(array1)*norm(array2))
    return round(cosine, 3)

Cosine = getCosineSimilarity(Midterm, Final)
print("Cosine Similarity:", Cosine)


# ## Problem 4

# In[14]:


Purchase = np.array([[200, 80], [20, 3000]])


# In[15]:


# 4(a) x^2 correlation
def getX2Correlation(array):
    length = array.shape[0]
    
    sum_row_0 = array[0][0] + array[0][1]
    sum_row_1 = array[1][0] + array[1][1]
    sum_col_0 = array[0][0] + array[1][0]
    sum_col_1 = array[0][1] + array[1][1]
    sum_total = sum_row_0 + sum_row_1
    
    new_array = np.zeros([2,2])
    new_array[0][0] = sum_row_0 * sum_col_0 / sum_total
    new_array[0][1] = sum_row_0 * sum_col_1 / sum_total
    new_array[1][0] = sum_row_1 * sum_col_0 / sum_total
    new_array[1][1] = sum_row_1 * sum_col_1 / sum_total
    
    sum = 0
    for i in range(length):
        for j in range(length):
            sum = sum + pow((array[i][j] - new_array[i][j]), 2) / new_array[i][j]
    return round(sum, 3)

X2Correlation = getX2Correlation(Purchase)
print("X2 Correlation:", X2Correlation)


# In[16]:


# 4(d) Kullback-Leibler Divergence
def getKL(p, q):
    length = len(p)
    sum = 0
    for iter in range(length):
        sum = sum + q[iter] *np.log(q[iter]/p[iter]) 
        
    return round(sum, 3)

p = np.array([0.061, 0.030, 0.909])
q = np.array([0.5, 0.3, 0.2])
KL = getKL(p, q)
print("Kullback Leibler Divergence:", KL)

