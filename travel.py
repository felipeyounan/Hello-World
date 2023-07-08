#1) If you're planning a 1-week long trip, which city should you visit to spend the least amount of money?
#2) How does the answer to the previous question chance if you change the duration of the trip to 4 days, 10 days or 2 weeks?
#3) If your total budget for the trip is $1000, wicth city should you visit to maximize the duratation of your trip? Which city should you visit if you want to minimize the duration?
#4) How does the answer to the previous question change if your budget is $600, $2000 or $1500
import pandas as pd
import numpy as np

data = pd.read_excel('Data Exercise 1.xlsx')
df = pd.DataFrame(data)
days = int(input('how many days will you travel? '))
budget = int(input('what is your budget for this trip? '))
#days = 10
#budget = 1000

def cost_of_trip(days, budget):
    df['Hotel per day($)'] = df['Hotel per day($)']*days
    rest_of_div = days % 7
    if rest_of_div >= 0:
        while rest_of_div >= 0:
            rest_of_div = days % 7
            if rest_of_div == 0:
                week = days / 7
                break
            days = days + 1
        if rest_of_div != 0:
            week = (days - 1) / 7
    df['Total Weekly Car Rental($)'] = df['Weekly Car Rental($)'] * week
    df['Sum($)'] = df['Return Flight($)'] + df['Hotel per day($)'] + df['Total Weekly Car Rental($)']
    mi = df[df['Sum($)'] == df['Sum($)'].min()]
    print('If you are planning to stay 1-week long, for the least cost, you will spend ${}  in {}'.format(mi['Sum($)'].to_string(index=False), mi['City'].to_string(index=False) ))
    print(f' é o valor de ',week)
cost_of_trip(days, budget)