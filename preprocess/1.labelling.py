import os

#path에 있는 모든 txt 파일의 모든 줄의 첫 숫자에 value만큼 값을 추가
def modify_txt_files_in_directory(path, value):
    for filename in os.listdir(path):

        # processed1의 train.txt 파일에 대한 예외
        if filename == 'train.txt':
            pass
        # 나머지 모든 txt파일 가공
        elif filename.endswith(".txt"):

            file_path = os.path.join(path, filename)

            with open(file_path, 'r') as file:
                lines = file.readlines()

            modified_lines = []
            for line in lines:
                parts = line.split()
                if parts:
                    first_integer = int(parts[0])
                    modified_line = ' '.join([str(first_integer + value)] + parts[1:])
                    modified_lines.append(modified_line + '\n')

            with open(file_path, 'w') as file:
                file.writelines(modified_lines)


if __name__ == "__main__":
    # 누적 라벨 개수 설정
    former_labels = 0 
    # 수정하고자 하는 디렉토리 경로 설정


    modify_txt_files_in_directory('dataset/dataset1_snack/label',former_labels)
    former_labels +=20

    modify_txt_files_in_directory('dataset/dataset2_snack2/label',former_labels)
    former_labels += 8

    modify_txt_files_in_directory('dataset/dataset3_sauce/label',former_labels)
    former_labels += 218

    modify_txt_files_in_directory('dataset/dataset4_processed1/label',former_labels)
    former_labels += 117

    modify_txt_files_in_directory('dataset/dataset5_processed2/label',former_labels)

    modify_txt_files_in_directory('dataset/dataset6_myeon/label',former_labels)
    former_labels += 10
    modify_txt_files_in_directory('dataset/dataset7_can/label',former_labels)
    

    