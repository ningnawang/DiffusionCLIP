@echo off
python main.py --compare_diff ^
               --config imagenet.yml ^
               --exp ./runs/ue_school_compare ^
               --t_0 301 ^
               --n_inv_step 20 ^
               --n_test_step 20 ^
               --n_iter 3 ^
               --folder_path data/ue_school ^
               --diff_type xid
            @REM    --diff_is_forward 

