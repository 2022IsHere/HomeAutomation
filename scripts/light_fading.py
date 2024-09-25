entity_id = data.get("entity_id")
sleep_time = data.get("sleep_time")

states = hass.states.get(entity_id)
current_brightness = states.attributes.get('brightness')

desired_brightness = 0
sleep_time_seconds = sleep_time * 60 # convert minutes to seconds
sleep_delay = sleep_time_seconds / current_brightness # 60 / 255 0.2 sec

while desired_brightness < current_brightness:
    current_brightness = current_brightness - 1
    logger.info( 'Setting brightness of ' + str(entity_id) + ' to ' + str(current_brightness) )
    data = { "entity_id": entity_id, "brightness": current_brightness }
    hass.services.call('light','turn_on', data)
    time.sleep(sleep_delay)
logger.info( 'Brightness of'+ str(entity_id) + ' is ' + str(current_brightness) )

