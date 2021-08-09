from adafruit_pybadger import PyBadger

pybadger = PyBadger()

pybadger.auto_dim_display(delay=30)

first_display = True

# establish vars for "biggest" compare
big_x = pybadger.acceleration.x
big_y = pybadger.acceleration.y
big_z = pybadger.acceleration.z

#compare two vars and return the largest
def larger_compare(oldValue,newValue):
    if(oldValue > newValue):
        return oldValue
    else:
        return newValue

while True:
    # if pybadger.button.a:
    #     pybadger.show_business_card(image_name="supercon.bmp", name_string="Changeme in code.py", name_scale=1,
    #                                 email_string_one="myemail@hackaday.io",
    #                                 email_string_two="https://hackaday.io/")
    # elif pybadger.button.b:
    #     pybadger.show_qr_code(data="https://hackaday.io/superconference/")
    # elif pybadger.button.start or first_display:

        #update the biggest accelerations 
        big_x = larger_compare(big_x,pybadger.acceleration.x)
        big_y = larger_compare(big_y,pybadger.acceleration.y)
        big_z = larger_compare(big_z,pybadger.acceleration.z)
        

        #format the info to print
        display_x = str(big_x)
        display_y = str(big_y)
        display_z = str(big_z)
        name = display_x + " " + display_y + " " + display_z


        pybadger.show_badge(name_string=name, hello_scale=1, my_name_is_scale=1, name_scale=1)
        first_display = False