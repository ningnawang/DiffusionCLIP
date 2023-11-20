@echo off
python main.py --compare_diff ^
               --config imagenet.yml ^
               --exp ./runs/ue_school_compare ^
               --t_0 601 ^
               --n_inv_step 40 ^
               --n_test_step 40 ^
               --n_iter 5 ^
               --folder_path data/ue_school

