from umqtt.simple import MQTTClient

mq_server = 'broker.emqx.io'
mq_id = 'esp00001' 
mq_user=''
mq_pass=''
mqClient0 = MQTTClient(mq_id, mq_server, user=mq_user, password=mq_pass)
mqClient0.connect()

mq_topic= b'temp'
mq_message='25'
mqClient0.publish(mq_topic, mq_message)
# https://jimirobot.tw/esp32-micropython-mqtt-publish-tutorial-303/