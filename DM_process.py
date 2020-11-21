import json
from mlxtend.preprocessing import TransactionEncoder

def load_dataset():
    print('Transactions Loading....')

    f = open('transaction.json', 'r')
    lines = f.readlines()
    f.close()

    transaction = []

    for line in lines:
        transaction.append(json.loads(line)['products'])

    print('Transactions Loaded!!')

    print('Customers Information Loading....')

    f = open('customer.json', 'r')
    line = f.readline()
    f.close()
    customers = json.loads(line)
    customer = []

    for c in customers:
        customer.append([customers[c]['state_province'], customers[c]['gender'], str(customers[c]['yearly_income']),
                customers[c]['total_children'], customers[c]['num_children_at_home'], customers[c]['education'],
                customers[c]['occupation'], customers[c]['houseowner'], customers[c]['num_cars_owned']])

    print('Customers Information Loaded!!')

    print('Time-Day Information Loading....')

    f = open('time_day.json', 'r')
    line = f.readline()
    f.close()
    days = json.loads(line)
    day = []

    print('Time-Day Information Loaded!!')
    return transaction, customer, day


def transaction_encode(array_list):
    print('Transactions Encoding....')

    te = TransactionEncoder()
    te_array = te.fit(array_list).transform(array_list)
    
    #print(te_array)
    print('Size: {} x {}'.format(str(len(te_array)), str(len(te_array[0]))))

    print('Transactions Encoded!!')
    return te_array, te.columns_

def top10_rules(association_rules):
    print('Building Top 10 Rules....')

    rules = []

    for i in range(10):
        rules.append({
                'antecedents': get_frozenset_elements(dict(association_rules)['antecedents'][i]),
                'consequents': get_frozenset_elements(dict(association_rules)['consequents'][i]),
                'antecedent_support': dict(association_rules)['antecedent support'][i],
                'consequent_support': dict(association_rules)['consequent support'][i],
                'support': dict(association_rules)['support'][i],
                'confidence': dict(association_rules)['confidence'][i],
                'lift': dict(association_rules)['lift'][i],
                'leverage': dict(association_rules)['leverage'][i],
                'conviction': dict(association_rules)['conviction'][i]
                })

    print('Top 10 Rules Built!!')
    return rules

def get_frozenset_elements(fs):
    elements = []

    for x in fs:
        elements.append(x)

    return elements

