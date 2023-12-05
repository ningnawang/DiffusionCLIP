import shutil
import os

def pick_and_save_files(source_folder, destination_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # for mode in ['A', 'B']:
    mode = 'B'
    for num in range(11, 97):
        # Construct the filename based on the specified format
        filename = f"{mode}_{num}_0orig.png"
        # filename = f"{mode}_{num}_3gen_it0_t301_ninv20_ngen20.png"

        # Full path to the source file
        source_path = os.path.join(source_folder, filename)

        # Full path to the destination file
        destination_path = os.path.join(destination_folder, filename)

        # Check if the file exists in the source folder
        if os.path.exists(source_path):
            # Copy the file to the destination folder
            shutil.copy(source_path, destination_path)
            print(f"File '{filename}' copied to '{destination_folder}'")

# Replace these paths with your actual source and destination folder paths
# source_folder_path = "D:/ninwang/DiffusionCLIP/runs/ue_school_all_CD_IMAGENET_ue_school_all_nit1_t301_ninv20_ngen20/image_samples_11_96"
source_folder_path = "D:/ninwang/DiffusionCLIP/runs/ue_school_all_CD_IMAGENET_ue_school_all_nit1_t301_ninv20_ngen20/B_image_samples_11_96"
# destination_folder_path = "D:/ninwang/DiffusionCLIP/runs/ue_school_all_CD_IMAGENET_ue_school_all_nit1_t301_ninv20_ngen20/orig_gray_11_96"
destination_folder_path = "D:/ninwang/DiffusionCLIP/runs/ue_school_all_CD_IMAGENET_ue_school_all_nit1_t301_ninv20_ngen20/B_orig_gray_11_96"

# Call the function
pick_and_save_files(source_folder_path, destination_folder_path)
print('done')