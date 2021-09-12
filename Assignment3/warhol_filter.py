"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'


def main():

    # Get file and load image
    filename = get_file()

    # Show the original image
    original_image = SimpleImage(filename)
    original_image.show()

    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    final_image.show()

    for new_pixel in final_image:
        orj_pixel=original_image.get_pixel(new_pixel.x%PATCH_SIZE,new_pixel.y%PATCH_SIZE)
        if (0 <= new_pixel.x < PATCH_SIZE) and (0 <= new_pixel.y < PATCH_SIZE): # upperleft
            make_recolored_patch(orj_pixel, new_pixel, 1.5,0,1.5)
        if (PATCH_SIZE <= new_pixel.x < PATCH_SIZE*2) and (0 <= new_pixel.y < PATCH_SIZE): # uppermiddle
            make_recolored_patch(orj_pixel, new_pixel, 0,1.5,1.5)
        if (PATCH_SIZE*2 <= new_pixel.x < PATCH_SIZE*3) and (0 <= new_pixel.y < PATCH_SIZE): # upperright
            make_recolored_patch(orj_pixel, new_pixel, 1.5,1.5,0)
        if (0 <= new_pixel.x < PATCH_SIZE) and (PATCH_SIZE <= new_pixel.y < PATCH_SIZE*2): # lowerleft
            make_recolored_patch(orj_pixel, new_pixel, 1.5,1.5,1.5)
        if (PATCH_SIZE <= new_pixel.x < PATCH_SIZE*2) and (PATCH_SIZE <= new_pixel.y < PATCH_SIZE*2): # lowermiddle
            make_recolored_patch(orj_pixel, new_pixel, 0,0,1.5)
        if (PATCH_SIZE*2 <= new_pixel.x < PATCH_SIZE*3) and (PATCH_SIZE <= new_pixel.y < PATCH_SIZE*2): # lowerright
            make_recolored_patch(orj_pixel, new_pixel, 1.5,0,0)
    final_image.show()

def make_recolored_patch(org_pixel, final_pixel, red_scale, green_scale, blue_scale):
    final_pixel.red=org_pixel.red * red_scale
    final_pixel.green=org_pixel.green * green_scale
    final_pixel.blue=org_pixel.blue * blue_scale

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter): ')
    if filename == '':
        filename = PATCH_NAME
    return filename

if __name__ == '__main__':
    main()