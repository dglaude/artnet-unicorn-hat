# Art-Net protocol for Pimoroni Unicorn Hat
# Open Pixel Control protocol for Pimoroni Unicorn Hat
# License: MIT

# To minimise changes, unicornhathd is imported as unicorn
import unicornhathd as unicorn
from twisted.internet import protocol, endpoints
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

# Adjust the LED brightness as needed.
# WARNING this is set to very bright.
unicorn.brightness(1)

class ArtNet(DatagramProtocol):

    def datagramReceived(self, data, (host, port)):
        if ((len(data) > 18) and (data[0:8] == "Art-Net\x00")):
            rawbytes = map(ord, data)
            opcode = rawbytes[8] + (rawbytes[9] << 8)
            protocolVersion = (rawbytes[10] << 8) + rawbytes[11]
            if ((opcode == 0x5000) and (protocolVersion >= 14)):
                sequence = rawbytes[12]
                physical = rawbytes[13]
                sub_net = (rawbytes[14] & 0xF0) >> 4
                universe = rawbytes[14] & 0x0F
                net = rawbytes[15]
                rgb_length = (rawbytes[16] << 8) + rawbytes[17]
                #print "seq %d phy %d sub_net %d uni %d net %d len %d" % \
                #(sequence, physical, sub_net, universe, net, rgb_length)
                idx = 18
                x = 0
# universe == 1 is assumed and correspond to y from 0 to 7 (top lines)
                y = 0
# if universe == 2 then we are with y from 8 to 15 (bottom lines)
                if (universe == 2):
                    y = 8
                while ((idx < (rgb_length+18)) and (y < 16)):
                    r = rawbytes[idx]
                    idx += 1
                    g = rawbytes[idx]
                    idx += 1
                    b = rawbytes[idx]
                    idx += 1
# Something fishy, why (15-y) rather than y... mirror effect?
                    unicorn.set_pixel(x, 15-y, r, g, b)
                    x += 1
                    if (x > 15):
                        x = 0
                        y += 1
# This assume both universe 1 and 2 will be updated in a raw in that order
                if (universe == 2):
                    unicorn.show()

# Non ArtNet code has been removed

reactor.listenUDP(6454, ArtNet())
reactor.run()
