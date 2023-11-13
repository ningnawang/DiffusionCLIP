@echo off
python main.py --edit_one_image ^
               --config imagenet.yml ^
               --exp ./runs/test ^
               --t_0 401 ^
               --n_inv_step 40 ^
               --n_test_step 40 ^
               --n_iter 5 ^
               --img_path data/VCC_2023_x_gray/1x00002.JPG