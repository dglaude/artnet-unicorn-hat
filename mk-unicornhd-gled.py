# Glediator Patch File generator for the Pimoroni Unicorn Hat HD
# Create two universe for the top and bottom 8 rows of 16 pixels
# Usage:
#        python mk-unicornhd-gled.py > unicornhd.gled
#
# Make sure to set your IP address twice in the Patch_Uni_ID_x_IP lines.
#
# License: MIT
# Copyright 2017 David Glaude

mx=16
my=16
mmm=mx*my*3
mm=(mx*my*3)/2

print "#GLEDIATOR Patch File"
print "Patch_Matrix_Size_X=%d" % (mx)
print "Patch_Matrix_Size_Y=%d" % (my)
print "Patch_Num_Unis=2"
print "Patch_Uni_ID_0_IP1=192"
print "Patch_Uni_ID_0_IP2=168"
print "Patch_Uni_ID_0_IP3=192"
print "Patch_Uni_ID_0_IP4=118"
print "Patch_Uni_ID_0_Net_Nr=0"
print "Patch_Uni_ID_0_Sub_Net_Nr=0"
print "Patch_Uni_ID_0_Uni_Nr=1"
print "Patch_Uni_ID_0_Num_Ch=%d" % (mm)
print "Patch_Uni_ID_1_IP1=192"
print "Patch_Uni_ID_1_IP2=168"
print "Patch_Uni_ID_1_IP3=192"
print "Patch_Uni_ID_1_IP4=118"
print "Patch_Uni_ID_1_Net_Nr=0"
print "Patch_Uni_ID_1_Sub_Net_Nr=0"
print "Patch_Uni_ID_1_Uni_Nr=2"
print "Patch_Uni_ID_1_Num_Ch=%d" % (mm)

i = 0
x = 0
y = 15
while ((i < mm) and (y > 8)):
    print "Patch_Pixel_X_%d_Y_%d_Ch_R=%d" % (x, y, i)
    i += 1
    print "Patch_Pixel_X_%d_Y_%d_Ch_G=%d" % (x, y, i)
    i += 1
    print "Patch_Pixel_X_%d_Y_%d_Ch_B=%d" % (x, y, i)
    i += 1
    print "Patch_Pixel_X_%d_Y_%d_Uni_ID=0" % (x, y)
    x += 1
    if (x > 15):
        x = 0
        y -= 1
i = 0
while ((i < mm) and (y > 0)):
    print "Patch_Pixel_X_%d_Y_%d_Ch_R=%d" % (x, y, i)
    i += 1
    print "Patch_Pixel_X_%d_Y_%d_Ch_G=%d" % (x, y, i)
    i += 1
    print "Patch_Pixel_X_%d_Y_%d_Ch_B=%d" % (x, y, i)
    i += 1
    print "Patch_Pixel_X_%d_Y_%d_Uni_ID=1" % (x, y)
    x += 1
    if (x > 15):
        x = 0
        y -= 1
