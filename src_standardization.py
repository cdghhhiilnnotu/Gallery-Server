import os

src_name = 'audios'
src_dir = f'src\\{src_name}'

for i, item_file in enumerate(os.listdir(src_dir)):
    if os.path.isfile(os.path.join(src_dir,item_file)):
        extens_file = item_file.split(".")[-1]
        new_name = "{}{:010d}.{}".format(src_name[0], i, extens_file)
        os.rename(os.path.join(src_dir,item_file), os.path.join(src_dir,new_name))
        # print(new_name)

