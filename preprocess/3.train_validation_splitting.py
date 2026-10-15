import os
from glob import glob
import shutil
import numpy as np

#현재 경로의 train 폴더 내에 valid 폴더 생성 
os.makedirs('train/valid')

#파일을 옮기는 함수 movedata 정의
def movedata(data_list, source_path, target_path):
    for data in data_list:
        source_file = os.path.join(source_path, data)
        target_file = os.path.join(target_path, data)
        
        print(f"{source_file}에서 {target_file}로 이동 중")
        shutil.move(source_file, target_file)


# folder 내의 파일들을 train test set으로 분리
def TVsplit(folder):

    # jpg, txt 파일 리스트로 만들기
    imgpath = os.path.join(folder) 
    img_list = glob(os.path.join(folder, '*.jpg'))
    target_list = glob(os.path.join(folder, '*.txt'))

    #리스트에 포함된 불필요한 파일 경로 제거 
    img_list = [name.replace(folder+'\\', '') for name in img_list ]
    target_list = [name.replace(folder+'\\','') for name in target_list ]

    # 'train.txt'파일 제거
    if target_list.count('train.txt') :
        target_list.remove('train.txt')

    # train test set 분리
    datalen = len(img_list)
    train_rate = 0.2 # train set 비율 0.2(조정 가능)

    np.random.seed(42) # random seed = 42
    index = np.arange(datalen)
    np.random.shuffle(index)
    test_img = np.array(img_list)[index[0:int(train_rate*datalen)]]
    test_target = np.array(target_list)[index[0:int(train_rate*datalen)]]

    train_img = list(set(img_list)-set(test_img))
    train_target = list(set(target_list)-set(test_target))

    # 파일 이동
    movedata(test_img, folder, 'train\\valid')
    movedata(test_target, folder, 'train\\valid')

# your data에 자신의 파일 경로 지정
your_path ='./'

TVsplit(your_path+'train')

