# %% [markdown]
# # Hypothesis Testing
# 
# In this notebook, we are going to represent the logic of our hypothesis testing for comparing NATS config changes. Everytime that we make a change, we benchmark the before and after change cases. After that, we change the groups names based on ```tmp``` directory names. Then we run this notebook in order to check the compare results.

# %%
import sys

# notebook variables
GROUP_A=sys.argv[1] # change this
GROUP_B=sys.argv[2] # change this

P_VALUE_BOUND = 0.05

# %%
# import in-use libraries
import pandas as pd
from scipy.stats import ttest_ind

# %%
# read csv to create groups datasets
dfA = pd.read_csv(f'../tmp/{GROUP_A}/dataset.csv')
dfB = pd.read_csv(f'../tmp/{GROUP_B}/dataset.csv')

# %%
# using a function for hypothesis testing logic
# which gets two columns data to compare
def hypo_test(groupA, groupB):
    # get mean values
    mean_a = groupA.mean()
    mean_b = groupB.mean()
    
    t_statistic, p_value = ttest_ind(groupA, groupB)
    
    print(f"\tmean of `{GROUP_A}`: {mean_a}")
    print(f"\tmean of `{GROUP_B}`: {mean_b}")
    print(f"\tt-statistic: {t_statistic}")
    print(f"\tp-value: {p_value}")
    
    if p_value < P_VALUE_BOUND:
        print("the difference is statistically significant at 95% confidence level.")
        if mean_a > mean_b:
            print(f"`{GROUP_A}` is better by {100 * float((mean_a-mean_b)/mean_a)}%.")
        else:
            print(f"`{GROUP_B}` is better by {100 * float((mean_b-mean_a)/mean_b)}%.")
    else:
        print("the difference is not statistically significant at 95% confidence level.")

# %%
# defining dataset columns
columns = ["pub-stats", "sub-stats", "overall-stats"]

# %%
#  hypothesis for comparing two groups
for column in columns:
    print(f"\ntesting `{column}` field:")
    hypo_test(dfA[column], dfB[column])
