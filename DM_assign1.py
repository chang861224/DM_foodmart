import DM_process as DM
import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori, fpgrowth, association_rules

transactions, customers, days = DM.load_dataset()
#print(customers)
#print(days[0])
print('=' * 50)



array, cols = DM.transaction_encode(transactions)
df = pd.DataFrame(array, columns=cols)
#print(df)
frequent_itemsets = fpgrowth(df, min_support=0.0001)
#print(frequent_itemsets)
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.9)
rules = DM.top10_rules(rules)
#print(DM.top10_rules(rules))

print('*' * 50)
print('Question 2\n')
#print(rules)
print('Minimum Support = 0.0001\nMinimum Confidence = 0.9')
for i in range(len(rules)):
    s1 = [str(x) for x in rules[i]['antecedents']]
    s2 = [str(x) for x in rules[i]['consequents']]
    print('({})\t->\t({})\t=> Support={}, Confidence={}'.format(', '.join(s1), ', '.join(s2), str(rules[i]['support']), str(rules[i]['confidence'])))

print('=' * 50)

#print(apriori(df, min_support=0.0001))



array, cols = DM.transaction_encode(customers)
df = pd.DataFrame(array, columns=cols)
#print(df)
frequent_itemsets = fpgrowth(df, min_support=0.05, use_colnames=True)
#print(frequent_itemsets)
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.9)
#rules = DM.top10_rules(rules)
#print(rules)

print('*' * 50)
print('Question 3\n')
print(rules)
"""
print('Minimum Support = 0.05\nMinimum Confidence = 0.9')
for i in range(len(rules)):
    s1 = rules[i]['antecedents']
    s2 = rules[i]['consequents']
    print('({})\t->\t({})\t=>Support={}, Confidence={}'.format(', '.join(s1), ', '.join(s2), str(rules[i]['support']), str(rules[i]['confidence'])))
"""
print('=' * 50)

