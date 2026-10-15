import os
import shutil

def split_images_labels(folder_name):
    # 입력받은 폴더 내의 모든 파일 가져오기
    folder_path = os.path.join(os.getcwd(), folder_name)
    
    if not os.path.exists(folder_path):
        print(f"{folder_name} 폴더가 존재하지 않습니다.")
        return

    files = os.listdir(folder_path)

    # "images"와 "labels" 폴더 생성
    images_folder = os.path.join(folder_path, "images")
    labels_folder = os.path.join(folder_path, "labels")

    if not os.path.exists(images_folder):
        os.makedirs(images_folder)

    if not os.path.exists(labels_folder):
        os.makedirs(labels_folder)

    # jpg 파일을 "images" 폴더로, txt 파일을 "labels" 폴더로 이동
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            if file.lower().endswith(".jpg"):
                shutil.move(file_path, os.path.join(images_folder, file))
            elif file.lower().endswith(".txt"):
                shutil.move(file_path, os.path.join(labels_folder, file))


split_images_labels('train')
split_images_labels('valid')
split_images_labels('test')

