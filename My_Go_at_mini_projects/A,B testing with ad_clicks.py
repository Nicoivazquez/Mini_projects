import codecademylib
import pandas as pd
import numpy as np

ad_clicks = pd.read_csv('ad_clicks.csv')

#print(ad_clicks.head(5))


most_views = ad_clicks.groupby('utm_source').user_id.count().reset_index()

#print(most_views)

# part 3. Checking if people actually clicked on the ad
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

#part4. checking the count people who clicked ad from each source
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

#part5. pivoting for better view

clicks_pivot = clicks_by_source.pivot(columns='is_click', index='utm_source', values= 'user_id').reset_index()

#print(clicks_pivot)

#part6. was there a difference in click rates for each source?

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
#print(clicks_pivot)


#part7. Analyzing the A/B ad Test
# make sure we have similar amounts of adds shown
ad_count_per_group= ad_clicks.groupby('experimental_group').user_id.count().reset_index()
#print(ad_count_per_group)

#part8. what percentage of users clicked on a or b 
more_popular_ad_pivot = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

#print(more_popular_ad_pivot)

#part 9 Trying to see if clicks changed by day in A/B test
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group =='B']

print(a_clicks)
#part 10. created two data frames to only cotain the results for each group
clicks_by_a_day = a_clicks.groupby(['is_click','day']).user_id.count().reset_index()

clicks_by_b_day = b_clicks.groupby(['is_click','day']).user_id.count().reset_index()

print(clicks_by_a_day)
# then pivoted the table to easily calculate the percent of users who clicked on the ad by day
clicks_by_a_day_pivot = clicks_by_a_day.pivot(columns='is_click', index='day', values= 'user_id').reset_index()

clicks_by_b_day_pivot = clicks_by_b_day.pivot(columns='is_click', index='day', values= 'user_id').reset_index()


clicks_by_a_day_pivot['Percent Clicked'] = clicks_by_a_day_pivot[True] / clicks_by_a_day_pivot[False] + clicks_by_a_day_pivot[True]

clicks_by_b_day_pivot['Percent Clicked'] = clicks_by_b_day_pivot[True] / clicks_by_b_day_pivot[False] + clicks_by_b_day_pivot[True]

print(clicks_by_a_day_pivot)

print(clicks_by_b_day_pivot)

#company should use ad A becuase it has higher click rates on most days

