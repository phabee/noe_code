from microbit import *
import neopixel

np = neopixel.NeoPixel(pin0, 10)    # Instatiate a NeoPixel Object with 10 LEDs

while True:
    if microphone.is_event(SoundEvent.LOUD):            
        for i in range(0,100,1):
            np[0] = (int(255*i/100), 0, 0)                 # Set first LED to Red (Tuple with R, G, B)
            np[1] = (int(249*i/100),int(153*i/100),int(8*i/100))                 # Set first LED to Red (Tuple with R, G, B)
            np[2] = (0, int(255*i/100), 0)                 # Set first LED to Green
            np[3] = (0, 0, int(255*i/100))                 # Set first LED to Blue
            np[4] = (int(255*i/100),0,int(230*i/100))
            np[5]=(int(129*i/100),int(9*i/100),int(228*i/100))
            np[6]=(int(249*i/100),int(220*i/100),int(3*i/100))
            np[7]=(int(255*i/100),int(255*i/100),0)
            np[8]=(int(255*i/100),int(255*i/100),int(255*i/100))
            np[9]=(int(182*i/100),int(97*i/100),int(13*i/100))
            np.show()                           # Now send the Data to the LED-Chain 
            sleep(100)
        
        sleep(10000)
        np[0] = (0,0,0)
        np[1] = (0,0,0)
        np[2] = (0,0,0)
        np[3] = (0,0,0)
        np[4] = (0,0,0)
        np[5] = (0,0,0)
        np[6] = (0,0,0)
        np[7] = (0,0,0)
        np[8] = (0,0,0)
        np[9] = (0,0,0)    
        np.show()
        sleep(10000)
