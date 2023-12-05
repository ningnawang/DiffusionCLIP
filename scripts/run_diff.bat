@echo off
python main.py --compare_diff ^
               --config imagenet.yml ^
               --exp runs/ue_school_all ^
               --t_0 301 ^
               --n_inv_step 20 ^
               --n_test_step 20 ^
               --n_iter 1 ^
               --folder_path data/ue_school_all ^
               --n_precomp_img 559 ^
               --diff_type orig
             @REM    --diff_type xid
               @REM    --diff_is_forward 

