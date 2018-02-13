import os


# import maktrans

def renamefiles():
    file_list = os.listdir(r'D:\1marabcoders\full stack\prank\\')
    # print(file_list)
    # saved_path = os.getcwd()
    # print('current path is : ' + saved_path)
    os.chdir(r'D:\1marabcoders\full stack\prank')
    for file_name in file_list:
        os.rename(file_name, file_name.translate(str.maketrans('', '', "0123456789")))



renamefiles()