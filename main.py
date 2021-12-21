import numpy as np
from PIL import Image

mtl_text = open("LE07_L2SP_175023_20020721_20200916_02_T1_MTL.txt", "r")

corners = ['CORNER_UL_LAT_PRODUCT', 'CORNER_UL_LON_PRODUCT', 'CORNER_UR_LAT_PRODUCT', 'CORNER_UR_LON_PRODUCT',
           'CORNER_LL_LAT_PRODUCT', 'CORNER_LL_LON_PRODUCT', 'CORNER_LR_LAT_PRODUCT', 'CORNER_LR_LON_PRODUCT']

coordinates = []
lines = mtl_text.readlines()

for line in lines:
    line = line.strip()
    if line[0:21] in corners:
        coordinates.append(float(line[24:]))
array_coord = np.array([coordinates[0::2], coordinates[1::2]])
print(array_coord)


delta_y = abs(coordinates[0] - coordinates[4])
delta_x = abs(coordinates[1] - coordinates[3])
print(delta_x, delta_y)

x = 7991
y = 7351

density_x = delta_x/x
density_y = delta_y/y
print(density_x, density_y)

mich_lat = 52.893913
mich_lon = 40.498020

mich_dif_lat = coordinates[0] - mich_lat
mich_dif_lon = coordinates[1] - mich_lon
print(mich_dif_lat, mich_dif_lon)

pixel_lat = mich_dif_lat / density_y
pixel_lon = mich_dif_lon / density_x
print(pixel_lat, pixel_lon)

point_ul_x = 1160 - 120
point_ul_y = 6034 - 120
point_lr_x = 1160 + 120
point_lr_y = 6034 + 120

image = Image.open('LE07_L2SP_175023_20020721_20200916_02_T1_SR_B3.TIF')
cropped = image.crop((point_ul_x, point_ul_y, point_lr_x, point_lr_y))
cropped.save('C:\\Users\\katia\\PycharmProjects\\michurinsk\\cropped.TIF')

image1 = Image.open('LE07_L2SP_175023_20020721_20200916_02_T1_SR_B4.TIF')
cropped1 = image1.crop((point_ul_x, point_ul_y, point_lr_x, point_lr_y))
cropped1.save('C:\\Users\\katia\\PycharmProjects\\michurinsk\\cropped1.TIF')