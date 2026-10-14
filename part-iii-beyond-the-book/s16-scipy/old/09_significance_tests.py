# SciPy Statistical Significance Tests
#
# What is Statistical Significance Test?
# In statistics, statistical significance means that the result that was produced has a reason behind it.
#   It was not produced randomly, or by chance.
# SciPy provides us with a module called scipy.stats, which has functions for performing statistical significance tests.
# Here are some techniques and keywords that are important when performing such tests:

# Hypothesis in Statistics
# Hypothesis is an assumption about a parameter in population.

# Null Hypothesis
# It assumes that the observation is not statistically significant.

# Alternate Hypothesis
# It assumes that the observations are due to some reason.
# It's the alternate to the Null Hypothesis.
# Example:
#     For an assessment of a student we would take:
#     "student is worse than average" - as a null hypothesis, and:
#     "student is better than average" - as an alternate hypothesis.

# One tailed test
# When our hypothesis is testing for one side of the value only, it is called "one tailed test".
# Example:
#     For the null hypothesis:
#     "the mean is equal to k", we can have alternate hypothesis:
#     "the mean is less than k", or:
#     "the mean is greater than k"

# Two tailed test
# When our hypothesis is testing for both side of the values.
# Example:
#     For the null hypothesis:
#     "the mean is equal to k", we can have alternate hypothesis:
#     "the mean is not equal to k"
#     In this case the mean is less than, or greater than k, and both sides are to be checked.

# Alpha value
# Alpha value is the level of significance.
# Example:
#     How close to extremes the data must be for null hypothesis to be rejected.
#     It is usually taken as 0.01, 0.05, or 0.1.

# P value
# P value tells how close to extreme the data actually is.
# P value and alpha values are compared to establish the statistical significance.
# If p value <= alpha we reject the null hypothesis and say that the data is statistically significant.
#   Otherwise we accept the null hypothesis.

import numpy as np

# T-Test
# T-tests are used to determine if there is significant deference between means of two variables
#   and let us know if they belong to the same distribution.
# It is a two tailed test.
# The function ttest_ind() takes two samples of same size and produces a tuple of t-statistic and p-value.

from scipy.stats import ttest_ind

# Find if the given values v1 and v2 are from same distribution:
v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)
res = ttest_ind(v1, v2)
print(res)
print()

# Return only the p-value, use the pvalue property
res = ttest_ind(v1, v2).pvalue
print(res)
print()

# KS-Test
# KS test is used to check if given values follow a distribution.
# The function takes the value to be tested, and the CDF as two parameters.
# A CDF can be either a string or a callable function that returns the probability.
# It can be used as a one tailed or two tailed test.
# By default it is two tailed.
# We can pass parameter alternative as a string of one of two-sided, less, or greater.
from scipy.stats import kstest

# Find if the given value follows the normal distribution
v = np.random.normal(size=100)
res = kstest(v, 'norm')
print(res)
print()

# Statistical Description of Data
# In order to see a summary of values in an array, we can use the describe() function.
# It returns the following description:
#   1. number of observations (nobs)
#   2. minimum and maximum values = minmax
#   3. mean
#   4. variance
#   5. skewness
#   6. kurtosis

from scipy.stats import describe

# Show statistical description of the values in an array
v = np.random.normal(size=100)
res = describe(v)
print(res)
print()

# Normality Tests (Skewness and Kurtosis)
# Normality tests are based on the skewness and kurtosis.
# The normaltest() function returns p value for the null hypothesis:
# "x comes from a normal distribution".

# Skewness:
# A measure of symmetry in data.
# For normal distributions it is 0.
# If it is negative, it means the data is skewed left.
# If it is positive it means the data is skewed right.

# Kurtosis:
# A measure of whether the data is heavy or lightly tailed to a normal distribution.
# Positive kurtosis means heavy tailed.
# Negative kurtosis means lightly tailed.

from scipy.stats import skew, kurtosis, normaltest

v = np.random.normal(size=100)

# Find skewness and kurtosis of values in an array
print(skew(v))
print(kurtosis(v))
print()

# Find if the data comes from a normal distribution
print(normaltest(v))
