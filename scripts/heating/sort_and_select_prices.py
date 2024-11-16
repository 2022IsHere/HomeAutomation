# Name: sort_and_select_prices.py
# Author: Sebastian Sopola @ https://www.linkedin.com/in/sebastiansopola/
# Description: This file containts the example python script to create a list and sort it

# Imports
#from datetime import datetime as datetime

# Pass nordpool sensor | Example how to read sript dictionary field data
#entity_id = data.get('entity_id')

# Check data availability & validity | Example how to declare variables with parameters. Notice default declaration!
#if entity_id:
#    today = hass.states.get(entity_id).attributes.get('today', [])
#    tomorrow = hass.states.get(entity_id).attributes.get('tomorrow', [])
#    tomorrow_valid = hass.states.get(entity_id).attributes.get('tomorrow_valid', False)
#else:
    # Handle missing input | Notice how to handle when data field is empty i.e. no input entity given
#    today = []
#    tomorrow = []
#    tomorrow_valid = False

# Init variables
#initial_price_list = []
#current_hour = datetime.now().hour

#for index in range(8):
#    hour = (current_hour + index) % 24
#    if hour < 24:
#        price = today[hour]
#    else:
#        if (len(tomorrow)) > 0:
#            price = tomorrow[hour - 24]
#        else:
#            price = 100
#     
#    initial_price_list.append(price)

# Calculate the result of X | Example how to initialize function
#def function_something(variable_something):
#   something = something_2 * something_3
#    return something

# result = function_something(variable_something)

# Update homeassistant entity's state | Examplöe how to update entity in home assistant
# hass.services.call('entity_type', 'service', {'entity_id': f'entity_type.{parameter}_rest_of_the_name} )

# How to include the python script in blueprint or automation
#action:
#  - service: script.turn_on
#    data:
#      entity_id: !input python_script
#      variables:
#        entity_id: !input nordpool_sensor