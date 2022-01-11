from urlencode import urlencode

value1 = 100
value2 = "陳會安"
params = { "value1": value1,
           "value2": value2 }
print(urlencode(params))