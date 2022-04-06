import os

def fileFolderDf (file_path):
    sum_size = 0
#   如果是文件就直接获取文件的大小
    if os.path.isfile(file_path):
        sum_size += os.path.getsize(file_path)
#   判断 如果是文件夹列举出文件夹中的所有文件 获取大小
    if os.path.isdir(file_path):
        list_file = os.listdir(file_path)
        for i in list_file:
            join_path = os.path.join(file_path,i)
            print(join_path)
#   再次判断：文件夹里面的文件 是文件还是文件夹 将其计算之和
            if os.path.isfile(join_path):
                sum_size += os.path.getsize(join_path)
            if os.path.isdir(join_path):
                sum_size += fileFolderDf(join_path)
    return sum_size
firle_dir = fileFolderDf("/Users/theblue/Downloads/LaGouCode")
print("文件夹的大小为：",firle_dir,"字节")

