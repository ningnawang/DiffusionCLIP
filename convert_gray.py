import os
from PIL import Image

ORIGIN_PATH = "./data/VCC_2023_x/"
DESTIN_PATH = "./data/VCC_2023_x_512/"
# ORIGIN_PATH = "./data/others/"
# DESTIN_PATH = "./data/others_gray/"

cnt = 0
for filename in os.listdir(ORIGIN_PATH):                                                                                                                                                                
    if cnt % 50 == 0:
        print("processed %d images" % cnt);
    cnt+=1
    img = Image.open(ORIGIN_PATH + filename)
    # img = Image.open(ORIGIN_PATH + filename).convert("L") 
    # img = img.resize((int(img.width), int(img.height))) 
    img = img.resize((512, 512))                                                                                                                                         
    img.save(DESTIN_PATH + filename) 


# python main.py --edit_one_image --config imagenet.yml --exp ./runs/star --t_0 401 --n_inv_step 40 --n_test_step 40 --n_iter 5 --img_path .\data\others_gray\star.png


# python main.py --unseen2unseen --config imagenet.yml --exp ./runs/test --t_0 500 --bs_test 4 --n_iter 10 --n_inv_step 40 --n_test_step 40 --img_path .\data\others_gray\star.png