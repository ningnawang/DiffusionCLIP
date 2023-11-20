@echo off
python main.py --edit_one_image ^
               --config imagenet.yml ^
               --exp ./runs/ue_schoolA ^
               --t_0 601 ^
               --n_inv_step 40 ^
               --n_test_step 40 ^
               --n_iter 5 ^
               --img_path data/ue_school_gray/A/0021.png
            @REM    --img_path data/compare_gray/crop/21_x0454_15x00719_crop.JPG

