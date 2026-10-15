import yaml


name_dict = {}
file_path = 'class.txt'  # 실제 파일 경로로 대체하세요


with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

for index, line in enumerate(lines):
    # 줄의 양 끝에 있는 공백 및 개행 문자 제거 후 딕셔너리에 추가
    name_dict[index] = line.strip()

data = {
    "train" : 'C:/Users/Kanghoon/Desktop/Project/Market/dataset/train',
        "val" : 'C:/Users/Kanghoon/Desktop/Project/Market/dataset/valid',
        "test" : 'C:/Users/Kanghoon/Desktop/Project/Market/dataset/test', 
        "names" : name_dict}

with open('./item.yaml', 'w') as f :
    yaml.dump(data, f)

# check written file
with open('./item.yaml', 'r') as f :
    lines = yaml.safe_load(f)
    print(lines)