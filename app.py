import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

#st.markdown('''
#Remember that there are several ways to output content into your web page...

#Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
#''')

#'''
### Here we would like to add some controllers in order to ask the user to select the parameters of the ride

#1. Let's ask for:
#- date and time
#- pickup longitude
#- pickup latitude
#- dropoff longitude
#- dropoff latitude
#- passenger count
#'''

date =st.date_input('Date:')
time =  st.time_input('Time of your ride:')
pickup_longitude = st.text_input('Pickup longitude:')
pickup_latitude = st.text_input('Pickup latitude:')
dropoff_longitude = st.text_input('Dropoff longitude:')
dropoff_latitude = st.text_input('Dropoff latitude:')
passenger_count = st.number_input('Passenger count:', min_value=1, max_value=8)

#'''
### Once we have these, let's call our API in order to retrieve a prediction

#See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

#🤔 How could we call our API ? Off course... The `requests` package 💡
#'''

url = 'https://taxifare.lewagon.ai/predict'

#if url == 'https://taxifare.lewagon.ai/predict':
#
#    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

#'''

#2. Let's build a dictionary containing the parameters for our API...

#3. Let's call our API using the `requests` package...

#4. Let's retrieve the prediction from the **JSON** returned by the API...

### Finally, we can display the prediction to the user
#'''

date_time = f'{date} {time}'

def get_fare():
    user_request = {
        'pickup_datetime':date_time,
        'pickup_longitude':pickup_longitude,
        'pickup_latitude':pickup_latitude,
        'dropoff_longitude':dropoff_longitude,
        'dropoff_latitude':dropoff_latitude,
        'passenger_count':passenger_count
        }

    response = requests.get(url, params=user_request)

    prediction = response.json()

    predicted_fare = prediction['fare']

    return predicted_fare

predicted_fare = get_fare()

st.header(f'fare = {predicted_fare} dollars')
