
import pandas as pd

inventory = pd.read_csv('inventory.csv')
print(inventory.head(10))

staten_island = inventory.iloc[:10]

product_request = staten_island.product_description 

seed_request = inventory[inventory['location'] == 'Brooklyn' & inventory['product_type'] == 'seeds']

inventory['in_stock'] = inventory.apply(lambda row: False if row[quantity] = 0 else True)

inventory['total_value'] = inventory.apply( row['price'] * row['quantity'])

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)


inventory['full_description'] = inventory.apply(combine_lambda , axis=1)


