import re
import json
from time import process_time

t_start = process_time()



### Dataset Loading....
print('Dataset Loading....')

dataset = []

f = open('sales_fact_1998.csv', 'r')

count = 0

for line in f.readlines():
    if count != 0:
        data = re.split(',|\n', line)
        dataset.append({
                'No': count,
                'product_id': int(data[0]),
                'time_id': int(data[1]),
                'customer_id': int(data[2]),
                'promotion_id': int(data[3]),
                'store_id': int(data[4]),
                'store_sales': float(data[5]),
                'store_cost': float(data[6]),
                'unit_sales': int(data[7])
                })
    count += 1

f.close()

f = open('sales_fact_dec_1998.csv', 'r')
count1 = 0

for line in f.readlines():
    if count1 != 0:
        data = re.split(',|\n', line)
        dataset.append({
                'No': count + count1 - 1,
                'product_id': int(data[0]),
                'time_id': int(data[1]),
                'customer_id': int(data[2]),
                'promotion_id': int(data[3]),
                'store_id': int(data[4]),
                'store_sales': float(data[5]),
                'store_cost': float(data[6]),
                'unit_sales': int(data[7])
                })
    count1 += 1

f.close()

print('Dataset Loaded!!')
### Dataset Loaded!!


### Transaction List Building....
print('Transaction List Building....')

f = open('transaction.json', 'w')
#f = open('transaction.csv', 'w')

items = []
transactions = []

for i in range(len(dataset)):
    if [dataset[i]['time_id'], dataset[i]['customer_id'], dataset[i]['promotion_id'], dataset[i]['store_id']] not in items:
        items.append([dataset[i]['time_id'], dataset[i]['customer_id'], dataset[i]['promotion_id'], dataset[i]['store_id']])
        transactions.append({
                'customer': dataset[i]['customer_id'],
                'promotion': dataset[i]['promotion_id'],
                'store': dataset[i]['store_id'],
                'time': dataset[i]['time_id'],
                'products': [dataset[i]['product_id']]
                })
    else:
        index = items.index([dataset[i]['time_id'], dataset[i]['customer_id'], dataset[i]['promotion_id'], dataset[i]['store_id']])
        transactions[index]['products'].append(dataset[i]['product_id'])

    if i % 2000 == 0:
        print('Have built {} items!!'.format(str(i)))

for i in range(len(transactions)):
    transactions[i]['products'].sort()
    f.write(json.dumps(transactions[i]) + '\n')
    #f.write(','.join(str(x) for x in transactions[i]['products']) + '\n')

    if i % 2000 == 0:
        print('Have written {} transactions to the file'.format(str(i)))

f.close()

print('Transction List Built!!')
### Transaction List Built!!



### Customer List Building....
print('Customer Data Loading....')
f = open('customer.csv', 'r')

keys = []
customers = {}
firstline = True

for line in f.readlines():
    if firstline:
        keys = re.split(',|\n', line)
        firstline = False
    else:
        data = re.split(',|\n', line)
        income = re.split('\$|K', data[18])
        del income[0]
        del income[-1]
        if len(income) == 3:
            del income[1]
        for i in range(len(income)):
            income[i] = int(income[i]) * 1000
        customers[int(data[0])] = {
                keys[1]: int(data[1]), keys[2]: data[2], keys[3]: data[3], keys[4]: data[4], keys[5]: data[5],
                keys[6]: data[6], keys[7]: data[7], keys[8]: data[8], keys[9]: data[9], keys[10]: data[10],
                keys[11]: data[11], keys[12]: data[12], keys[13]: data[13], keys[14]: data[14], keys[15]: data[15],
                keys[16]: data[16], keys[17]: data[17], keys[18]: income, keys[19]: data[19], keys[20]: data[20],
                keys[21]: data[21], keys[22]: data[22], keys[23]: data[23], keys[24]: data[24], keys[25]: data[25],
                keys[26]: data[26], keys[27]: data[27]
                }

f.close()

print('Customer Data Loaded!!')

###

print('Customer List Building....')

f = open('customer.json', 'w')
f.write(json.dumps(customers))
f.close()

print('Customer List Built!!')
### Customer List Built!!



### Time-Day Transform Begin
print('Time-Day Data Loading....')
f = open('time_by_day.csv', 'r')

keys = []
times = {}
firstline = True

for line in f.readlines():
    if firstline:
        keys = re.split(',|\n', line)
        firstline = False
    else:
        data = re.split(',|\n', line)
        times[int(data[0])] = {
                keys[1]: data[1], keys[2]: data[2], keys[3]: data[3], keys[4]: data[4], keys[5]: data[5],
                keys[6]: data[6], keys[7]: data[7], keys[8]: data[8], keys[9]: data[9]
                }

f.close()

print('Time-Day Data Loaded!!')

###

print('Time-Day Transform Begin....')

f = open('time_day.json', 'w')
f.write(json.dumps(times))
f.close()

print('Time-Day Transform End!!')
### Time-Day Transform End!!



### Product Transform Begin
print('Product Data Loading....')
f = open('product.csv', 'r')

keys = []
products = {}
firstline = True

for line in f.readlines():
    if firstline:
        keys = re.split(',|\n', line)
        firstline = False
    else:
        data = re.split(',|\n', line)
        products[int(data[1])] = {
                keys[0]: data[0], keys[2]: data[2], keys[3]: data[3], keys[4]: data[4], keys[5]: data[5],
                keys[6]: data[6], keys[7]: data[7], keys[8]: data[8], keys[9]: data[9], keys[10]: data[10],
                keys[11]: data[11], keys[12]: data[12], keys[13]: data[13], keys[14]: data[14]
                }

f.close()

print('Product Data Loaded!!')

###

print('Product Transform Begin....')

f = open('product.json', 'w')
f.write(json.dumps(products))
f.close()

print('Product Transform End!!')
### Product Transform End!!



### Product Class Transform Begin
print('Product Class Data Loading....')
f = open('product_class.csv', 'r')

keys = []
product_classes = {}
firstline = True

for line in f.readlines():
    if firstline:
        keys = re.split(',|\n', line)
        firstline = False
    else:
        data = re.split(',|\n', line)
        product_classes[int(data[0])] = {
                keys[1]: data[1], keys[2]: data[2], keys[3]: data[3], keys[4]: data[4]
                }

f.close()

print('Product Class Data Loaded!!')

###

print('Product Class Transform Begin....')

f = open('product_class.json', 'w')
f.write(json.dumps(product_classes))
f.close()

print('Product Class Transform End!!')
### Product Class Transform End!!




### Print Information

t_stop = process_time()

print('================ Data Information ================')
print('Length of transactions:', len(transactions))
print('Length of customers:', len(customers))
print('Length of times:', len(times))
print('Length of products:', len(products))
print('Length of product classes:', len(product_classes))
print('==================================================')
print('Start time:', t_start)
print('Stop time:', t_stop)
print('Time duration (in second):', t_stop - t_start)

