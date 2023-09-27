from PIL import Image

import os

dir_path = ""


def remove_img( path, img_name):
    os.remove(path + '/' + img_name)
# check if file exists or not
    if os.path.exists(path + '/' + img_name) is False:
        # file did not exists
        return True

def beforeTheDot(file_name): # RETURNS ANYTHING BEFORE DOT EX. CAKE.PDF -> CAKE
    num = file_name.rfind(".")
    moded_text = file_name[:num]
    return moded_text

def convert_images():
    images_to_be_processed = []
    image_extensions = {"jpeg", "jpg", "png","PNG", "JPEG"}
    for root, subdirectories, files in os.walk(dir_path):
            for file in files:
                print(file)
                ending = file.rsplit('.')[-1]
                if ending in image_extensions:
                    save_name = beforeTheDot(file)
                    img = Image.open(f"{os.path.join(root, file)}").convert('RGB')
                    img.save(f"{os.path.join(root)}/{save_name}.pdf",format='pdf')
                    remove_img(root, file)
convert_images()
