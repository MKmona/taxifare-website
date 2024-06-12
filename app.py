import streamlit as st
import requests
import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'


# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
#https://taxifare.lewagon.ai/predict?
#pickup_latitude=42.751210955038&pickup_longitude=-75.4652471468304&dropoff_latitude=40.72157&
# dropoff_longitude=-74.047455&passenger_count=1&pickup_datetime=2024-06-12%2019:21:48

# input user's pickup_datetime
pickup_date = st.date_input(
    "When's your pickup_datetime",
    datetime.date(2019, 7, 6))
st.write('The pickup_datetime:', pickup_date)

# inpu ttime

pickup_time = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('pickup_time', pickup_time)

pickup_datetime = f'{pickup_date} {pickup_time}'

# input user's pickup_longitude
pickup_longitude = st.number_input('Insert a pickup_longitude')
st.write('The user pickup_longitude is ', pickup_longitude)

# input user's pickup_latitude
pickup_latitude = st.number_input('Insert a pickup_latitude')
st.write('The user pickup_longitude is ', pickup_latitude)

# input user's dropoff_longitude
dropoff_longitude = st.number_input('Insert a dropoff_longitude')
st.write('The user dropoff_longitude is ', dropoff_longitude)

# input user's dropoff_latitude
dropoff_latitude = st.number_input('Insert a dropoff_latitude')
st.write('The user dropoff_latitude is ', dropoff_latitude)

# input user's passenger_count
passenger_count = st.number_input('Insert a passenger_count')
st.write('The number of passenger_count is ', passenger_count)

# a dictionary containing the parameters
params = {'pickup_datetime': pickup_datetime,
          'pickup_longitude': pickup_longitude,
          'pickup_latitude': pickup_latitude,
          'dropoff_longitude': dropoff_longitude,
          'dropoff_latitude': dropoff_latitude,
          'passenger_count': int(passenger_count)}

# retrieve the prediction from the **JSON** returned by the API


# Get fare button
if st.button('Get fare'):
    response = requests.get(url=url,
                        params=params).json()
    print(response)
    # print is visible in the server output, not in the page
    print('button clicked!')
    st.write('Click to get new fare')
    # st.write('Further clicks are not visible but are executed')
    # display the prediction to the user
    st.write('The predicted taxifare is', (response['fare']))
else:
    st.write('Click to get fare')
