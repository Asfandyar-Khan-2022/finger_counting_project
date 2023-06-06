from PIL import Image
import os


def resize(im, new_width):
    width, height = im.size
    ratio = height/width
    new_height = int(ratio*new_width)
    resized_img = im.resize((new_width, new_height))
    return resized_img

files = os.listdir('finger_images')
extentions = ['jpg', 'jped', 'png', 'gif']
for file in files:
    ext = file.split('.')[-1]
    if ext in extentions:
        im = Image.open('finger_images/'+file)
        im_resized = resize(im,200)
        filepath = f'finger_images/{file}'
        im_resized.save(filepath)

