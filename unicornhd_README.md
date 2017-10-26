# Modified and simplified README for unicorn HAT hd

# artnet-unicorn-hd-hat
Control Pimoroni Unicorn HD Hat LEDs using the Art-Net protocol.

Art-Net is a protocol for controlling lights over a network. Glediator
controls LEDs on one or more Art-Net nodes. An Art-Net node drives the
LEDs. In this example, Glediator runs on a laptop and controls a Pi with
a Unicorn HD Hat. The Pi is the Art-Net node. A Pimoroni Unicorn HD Hat is
an add-on board for a Raspberry Pi+/2 with an 16 by 16 grid of RGB LEDs.

The Unicorn HD HAT has a build in co-processor that listen on SPI and drive the LEDs. We use the Pimoroni python library to control the HAT.

http://www.solderlab.de/index.php/software/glediator
https://shop.pimoroni.com/products/unicorn-hat-hd
https://en.wikipedia.org/wiki/Art-Net

## Preliminary

The Unicorn HD Hat must be installed and working on the Pi with the
Pimoroni supplied Python software. Make sure this works before graduating
to Art-Net.

https://github.com/pimoroni/unicorn-hat-hd

## Install libraries on the Pi

Do this only once to install the Python twisted libraries.

```
sudo apt-get install python-twisted
```

## Run Art-Net server on the Pi
The following command runs the Art-Net server turning the Pi into an Art-Net node. 
Many programs can send LED values to an Art-Net node. Glediator is one such
program.

```
python unicornhd-artnet.py
```

## Glediator

See the Glediator download page to download and install Glediator.
If you see errors about missing binary RXTX, ignore them. In this case,
Glediator controls the LEDs using network packets, not serial communcations.

Glediator is designed to work with many different LED arrays so it must
be told the dimensions and arrangements of the LEDs. It must also be
told the IP address of the Pi with the Unicorn Hat.

### Change twice th IP address in patch file
Open the Glediator patch file unicornhd.gled in your
favorite editor. nano works fine. Change the IP address to the IP address
of the Pi. Please note that you have to do that twice as the bord is made of two universe.

This how the IP address 192.168.192.118 looks like in the file

```
Patch_Uni_ID_0_IP1=192
Patch_Uni_ID_0_IP2=168
Patch_Uni_ID_0_IP3=192
Patch_Uni_ID_0_IP4=118
...
Patch_Uni_ID_1_IP1=192
Patch_Uni_ID_1_IP2=168
Patch_Uni_ID_1_IP3=192
Patch_Uni_ID_1_IP4=118
```

Close and save the file.

### Set matrix size
In Glediator change the matrix size to 16 by 16.

At the Glediator main screen, select Options | Matrix Size

Size_X = 16 Size_Y = 16

### Set Art-Net mode
At the Glediator main screen, select Options | Output

At the Output Options screen:

```
Output Mode: Artnet
Mapping Mode: Single_Pixels
```

Ignore the rest in the top half of the screen. Ignore the left bottom options
which are for serial ports.

In the right bottom options click on Patch ArtNet/TMP2.Net

At the "Artnet & TPM2.Net Patcher" screen, load unicornhd.gled

Click on Done

Back at the Output Options screen, click on Apply Changes.

Click on "Open Socket". Glediator will start sending pixel values to the Pi.

Click on Done to get back to the main screen.

At this point, the control panel can be used to generate new patterns.

## PixelController

Unicorn HAT HD ArtNet has not been tested with PixelController

## Open Pixel Control Protocol

Support for Open Pixel Control protocol is not present for Unicorn HD Hat

# Files related to the Unicorn HD Hat implementation

README_unicornhd.md: This file
unicornhd-artnet.py: Artnet server (does not require sudo)
unicornhd.gled: Configuration for Glediator.
mk-unicornhd-gled.py: This generate the previous file (might be usefull if you want to customised the mapping.

