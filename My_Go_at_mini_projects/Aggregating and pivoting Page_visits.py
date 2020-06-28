
import pandas as pd

user_visits = pd.read_csv('page_visits.csv')

# Part 1. check data structure
print(user_visits.head(10))

# Part 2. calculating visits from each diff source
click_source = user_visits.groupby('utm_source').id.count().reset_index()

#Part 3. check results
print(click_source)

#Part 4. check by month to see differences in source traffic
click_source_by_month = user_visits.groupby(['utm_source', 'month']).id.count().reset_idex()

#park 5. pivot the info to make readable
click_source_by_month_pivot = click_source_by_month.pivot(column= 'month', index= 'utm_source', values= 'id').reset_index()

#part 6. print to check results
print(click_source_by_month_pivot)


