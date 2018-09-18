# Homework 1

Name: Shuyue Lai

NetID: shuyuel2



## Problem 1 Statistical Properties

##### (a) Max and min:

![1537246572900](shuyuel2_hw1.assets/1537246572900.png)

- Max: 
  - Midterm = 99
  - Final = 100
- Minx:
  - Midterm = 75
  - Final = 77

##### (b) Mean, mode and median:

![1537246604728](shuyuel2_hw1.assets/1537246604728.png)

- Mean:
  - Midterm:  88.7
  - Final: 88.2
- Mode:
  - Midterm: 96
  - Final: 80, 88
- Median:
  - Midterm: 89
  - Final: 88

##### (c) First quartile, third quartile and inter-quartile range:

![1537246629086](shuyuel2_hw1.assets/1537246629086.png)

- Midterm:

  ![1537059350850](shuyuel2_hw1.assets/1537059350850.png)

  - First Quartile:  84
  - Third Quartile: 96
  - Inter-Quartile: 12

- Final:

  ![1537059515656](shuyuel2_hw1.assets/1537059515656.png)

  - - First Quartile:  80
    - Third Quartile: 95
    - Inter-Quartile: 15

##### (d) Variance(sample & population):

![1537246653015](shuyuel2_hw1.assets/1537246653015.png)

- Population:

$$
Var = E((X-\overline{x})^2) = E(x^2) - [E(x)]^2
$$

$$
Var = \frac{1}{n}*\sum_{i=1}^{n}(x_i - \overline{x})^2
$$



- Sample:
  $$
  Var = \frac{1}{n-1}*\sum_{i=1}^{n}(x_i - \overline{x})^2
  $$


- Midterm: 
  - Population Variance: 58.610
  - Sample Variance: 65.122
- Final:
  - Population Variance: 57.560
  - Sample Variance: 63.956

##### (e) Standard Deviation (sample & population):

![1537246675453](shuyuel2_hw1.assets/1537246675453.png)

- Standard Deviation:
  $$
  Std = \sqrt{Var}
  $$


- Midterm: 
  - Population Standard Deviation: 7.656
  - Sample Standard Deviation: 8.070
- Final:
  - Population Standard Deviation: 7.587
  - Sample Standard Deviation: 7.997





## Problem 2 Normalize Data

##### (a) Min-Max Normalization:

![1537246838001](shuyuel2_hw1.assets/1537246838001.png)

- $$
  v' = \frac{v -min}{max - min}*(newMax - newMin )  + newMin
  $$

- Student 1: 0.833
- Student 2: 0.458
- Student 3: 0.125

##### (b) Variance(population) of min-max normalized midterm scored:

![1537246854553](shuyuel2_hw1.assets/1537246854553.png)

- Variance (Population):

  $$
  Var = \frac{1}{n}*\sum_{i=1}^{n}(x_i - \overline{x})^2
  $$

- Min-Max Normalization:

  $$
  v' = \frac{v -min}{max - min}*(newMax - newMin )  + newMin
  $$

- Midterm Variance Min-Max Normalization:0.102

##### (c) Z-Score Normalization of final scores:

![1537246869028](shuyuel2_hw1.assets/1537246869028.png)

- $$
  v' = \frac{v - \mu}{\sigma}
  $$

- Student 4: 0.896

- Student 5: -0.422

- Student 6: -1.476

##### (d) Variance(population) of z-score normalized final score:

![1537246891818](shuyuel2_hw1.assets/1537246891818.png)

- Variance (Population):
  $$
  Var = \frac{1}{n}*\sum_{i=1}^{n}(x_i - \overline{x})^2
  $$

- Z-Score Normalization:
  $$
  v' = \frac{v - \mu}{\sigma}
  $$

- Variance(population) of z-score normalized final score: 1.000



## Problem 3 Relationship between Midterm and Final

##### (a) Covariance(Population):

![1537246908132](shuyuel2_hw1.assets/1537246908132.png)
$$
Cov = E[(x_1-\mu_1)*(x_2=\mu_2)]=E(x_1*x_2)-\mu_1*\mu_2
$$

- Covariance: 18.160

##### (b)Pearson's Correlation Coefficient(population standard deviation and covariance):

![1537246923005](shuyuel2_hw1.assets/1537246923005.png)

- $$
  Pearson = \frac{cov(x_1, x_2)}{\sigma_{x_1} * \sigma_{x_2}}
  $$

  Pearson Correlation Coefficient: 0.313

##### (c) Independent?

- Since the Pearson Correlation Coefficient is 0.313, which means M which denotes midterm scores and F denotes final scores are not independent and are positive related. 

##### (d)  Distance 

![1537246995759](shuyuel2_hw1.assets/1537246995759.png)

![1537247014050](shuyuel2_hw1.assets/1537247014050.png)

- Minkowski Distance:
  $$
  d_{ij} = \sqrt[p]{|x_{i1}-x_{j1}|^{p}+|x_{i2}-x_{j2}|^{p}+L+|x_{il}-x_{jl}|^{p}}
  $$






- Manhattan Distance:

  - 

  $$
  d_{ij} = |x_{i1}-x_{j1}|+|x_{i2}-x_{j2}|+L+|x_{il}-x_{jl}|
  $$

  - Midterm & Final: 75

- Euclidean Distance:

  - 

  $$
  d_{ij} = \sqrt[2]{|x_{i1}-x_{j1}|^{2}+|x_{i2}-x_{j2}|^{2}+L+|x_{il}-x_{jl}|^{2}}
  $$

  - Midterm & Final: 28.302

- Supremum Distance:

  - 

  $$
  d_{ij} = lim_{p\rightarrow \infty}\sqrt[p]{|x_{i1}-x_{j1}|^{p}+|x_{i2}-x_{j2}|^{p}+L+|x_{il}-x_{jl}|^{p}} = max_{f=1}^{l}|x_{if} - x_{jf}|
  $$

  - Midterm & Final: 16

- Cosine Similarity of m and f:

  - 

  $$
  CosineSimilarity = \frac{A\cdot B}{||A|| * ||B||}= \frac{\sum_{i=1}^{n}A_i * B_i}{\sqrt{\sum_{i=1}^{n}(A_i)^2}*\sqrt{\sum_{i=1}^{n}(B_i)^2}}
  $$

  - Midterm & Final: 0.995

##### (e)
Manhattan Distance: Means the difference of each student between midterm and final.  The distance is always positive and the larger value means the difference is larger. In the scenario, the larger value means students perform different in midterm and final.

##### (f) Kullback-Leibler Divergence / Jaccard Coefficient

I don't think using Kullback-Leibler Divergence is a good choice since the model is discrete and some of the p(x) will be zero which will lead mistake when taking log. Besides, I also don't think using Kullback-Leibler Divergence is a good choice since the attribute is binary while it's not appropriate to separate Midterm and Final in this way.

- KL:
  $$
  D_{kL}(p(x)||q(x))=\sum q(x) * ln\frac{p(x)}{q(x)}
  $$


- Jaccard:
  $$
  Jaccard= \frac{|a\cap b|}{|A| + |B| - |A \cap B|)}
  $$


## Problem 4 

##### (a) X^2 correlation value:

$$
X^2=\sum_{i=1}^{n}\frac{(O_i-E_i)^2}{E_i}
$$

![1537244525600](shuyuel2_hw1.assets/1537244525600.png)

##### (b) 
	We can reject the null hypothesis of independence at a confidence level of 0.001. Therefore, "purchasing beer" and "purchasing diaper" are correlated.

##### (c)

	p = [200 : 80+20 : 3000] = [2 : 1 : 30] = [0.061 : 0.030 : 0.909]

##### (d) Kullback-Leibler Divergence

![1537247055014](shuyuel2_hw1.assets/1537247055014.png)
$$
D_{kL}(p(x)||q(x))=\sum q(x) * ln\frac{p(x)}{q(x)}
$$
  	p = [0.061 0.030 0.909]

	q = [0.5 0.3 0.2 ]

	KL = 1.440


