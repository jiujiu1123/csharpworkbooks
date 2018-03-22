import glob,shutil 

filenames = [f for f in glob.glob("*") if ".workbook" in f]
for old_file_name in filenames:
    new_file_name = old_file_name.replace(".workbook", ".md")
    shutil.copyfile(old_file_name, new_file_name)  
