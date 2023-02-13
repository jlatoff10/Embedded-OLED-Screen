from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf,sys
import imgfile
import time
from math import sin, cos, pi


pix_res_x  = 128 # SSD1306 horizontal resolution
pix_res_y = 64   # SSD1306 vertical resolution

i2c_dev = I2C(1,scl=Pin(27),sda=Pin(26),freq=200000)  # start I2C on I2C1 (GPIO 26/27)
i2c_addr = [hex(ii) for ii in i2c_dev.scan()] # get I2C address in hex format
if i2c_addr==[]:
    print('No I2C Display Found') 
    sys.exit() # exit routine if no dev found
else:
    print("I2C Address      : {}".format(i2c_addr[0])) # I2C device address
    print("I2C Configuration: {}".format(i2c_dev)) # print I2C params


oled = SSD1306_I2C(pix_res_x, pix_res_y, i2c_dev) # oled controller





while True:
    x=0
    while x<23:
        buffer,img_res = imgfile.get_img(x) # get the image byte array
        # frame buff types: GS2_HMSB, GS4_HMSB, GS8, MONO_HLSB, MONO_VLSB, MONO_HMSB, MVLSB, RGB565
        fb = framebuf.FrameBuffer(buffer, img_res[0], img_res[1], framebuf.MONO_HMSB) # MONO_HLSB, MONO_VLSB, MONO_HMSB
        
        oled.fill(0) # clear the OLED
        oled.blit(fb, 0, 0) # show the image at location (x=0,y=0)
        oled.show()
        x=x+1
        #time.sleep_ms(100)
    time.sleep_ms(1000)

# oled.fill(0) # clear the OLED
# oled.blit(fb, 0, 0) # show the image at location (x=0,y=0)
    


# start_x = 65 # start point for text in x-dir
# start_y = 12 # start point for text in y-dir
# lineskip = 15 # space between text in y-dir
# txt_array = ['Longeviti','Neuro','Solutions'] # text array
# 
# for iter_ii,txt in enumerate(txt_array):
#     oled.text(txt,start_x,start_y+(iter_ii*lineskip)) # add text at (start_x,start_y)

#oled.show() # show the new text and image

# other functions
# oled.poweron() # power on the OLED
# oled.poweroff() # power off the OLED (save power)
# oled.invert(1) # invert the colors from dark -> light, and light -> dark
# oled.contrast(1) # lower brightness
# oled.contrast(255) # increase brightness