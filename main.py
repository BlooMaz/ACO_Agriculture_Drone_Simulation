import os




global filename
if __name__ == "__main__":
    if os.path.exists("image_split"):
        path_to_dir = 'image_split'  # path to directory you wish to remove
        files_in_dir = os.listdir(path_to_dir)  # get list of files in the directory

        for file in files_in_dir:  # loop to delete each file in folder
            os.remove(f'{path_to_dir}/{file}')  # delete file

        os.rmdir(path_to_dir)
    else:
        print("The file does not exist")
    #go to home page
    import page2