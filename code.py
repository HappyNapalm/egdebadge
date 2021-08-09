from adafruit_pybadger import PyBadger

pybadger = PyBadger()

pybadger.auto_dim_display(delay=30)

first_display = True



while True:
    if pybadger.button.a:
        pybadger.show_business_card(image_name="supercon.bmp", name_string="Changeme in code.py", name_scale=1,
                                    email_string_one="myemail@hackaday.io",
                                    email_string_two="https://hackaday.io/")
    elif pybadger.button.b:
        pybadger.show_qr_code(data="https://hackaday.io/superconference/")
    elif pybadger.button.start or first_display:
        
        #check if we are accelerating.
        display_x = str(pybadger.acceleration.x)
        display_y = str(pybadger.acceleration.y)
        display_z = str(pybadger.acceleration.z)

        #format the info to print
        name = display_x + " " + display_y + " " + display_z


        pybadger.show_badge(name_string=name, hello_scale=1, my_name_is_scale=1, name_scale=1)
        first_display = False