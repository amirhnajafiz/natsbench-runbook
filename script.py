# %%
# notebook variables
GROUP_A="normal-stats.26714" # change this
GROUP_B="normal-stats.eef72" # change this

P_VALUE_BOUND = 0.05

# %%
# import in-use libraries
import pandas as pd
from scipy.stats import ttest_ind

# %%
# read csv to create groups datasets
dfA = pd.read_csv(f'tmp/{GROUP_A}/dataset.csv')
dfB = pd.read_csv(f'tmp/{GROUP_A}/dataset.csv')

dfA.head()

# %%
# describe datasets
dfA.describe()

# %%
# a function for hypothesis testing
def hypo_test(groupA, groupB):
    t, p = ttest_ind(groupA, groupB)
    return p < P_VALUE_BOUND

# %%
# a function to compare two groups
def compare(avgA, avgB):    
    return 100 * float(avgA-avgB/avgA)

# %%
#  hypothesis for comparing pub stats
if hypo_test(dfA["pub-stats"], dfB["pub-stats"]):
    print('reject pub-stats hypothesis: the means are different')
    print(f'(A-B/A): {compare(dfA["pub-stats"].mean(), dfB["pub-stats"].mean())}')
else:
    print('fail to reject pub-stats hypothesis: the means are the same')

# %%
#  hypothesis for comparing sub stats
if hypo_test(dfA["sub-stats"], dfB["sub-stats"]):
    print('reject sub-stats hypothesis: the means are different')
    print(f'(A-B/A): {compare(dfA["sub-stats"].mean(), dfB["sub-stats"].mean())}')
else:
    print('fail to reject sub-stats hypothesis: the means are the same')

# %%
#  hypothesis for comparing overall stats
if hypo_test(dfA["overall-stats"], dfB["overall-stats"]):
    print('reject overall-stats hypothesis: the means are different')
    print(f'(A-B/A): {compare(dfA["overall-stats"].mean(), dfB["overall-stats"].mean())}')
else:
    print('fail to reject overall-stats hypothesis: the means are the same')


