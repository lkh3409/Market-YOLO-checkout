import pandas as pd
import cv2
from ultralytics import YOLO


def make_name_price_dict(file_path):
    df = pd.read_excel(file_path)
    name_price_dict = {}
    for index, row in df.iterrows():
        name = row['Name']
        price = row['Price']
        name_price_dict[name] = int(price)

    return name_price_dict

def item_index_dict(file_path):
    df = pd.read_excel(file_path)
    names = df['Name'].tolist()
    name_index_dict = {index: name for index, name in enumerate(names)}
    return name_index_dict

excel_file= 'Price.xlsx'

#상품, 인덱스 딕셔너리 
name_index_dict = item_index_dict(excel_file)

# 상품, 가격 딕셔너리
item_dict = make_name_price_dict(excel_file)


model = YOLO("Hyperparameter_tuning/default(img_640, b16)/weights/best.pt")
img = 'test_image/test'

results = model.predict(img + '.jpg', save_txt=True)
dir = str(results[0]).split('\n')[-2].split("'")[1]
with open(dir + '/labels/{}.txt'.format(img)) as f:
    lines = f.readlines()
f.close()
count_result = {}
for line in lines:
    obj = int(line.split(' ')[0])
    if obj in count_result:
        count_result[obj] += 1
    else:
        count_result[obj] = 1

#결과를 이미지로 그리기
plots = results[0].plot()
# 이미지 크기를 조절하여 전체 이미지를 표시
cv2.namedWindow("plot", cv2.WINDOW_NORMAL)
cv2.imshow("plot", plots)
cv2.waitKey(0)
cv2.destroyAllWindows()       


total = 0
for product_code, count in count_result.items():
    name = name_index_dict[product_code]
    print('{}: {}개. (1개당 {}원)'.format(name, count, item_dict[name]))
    total += item_dict[name] * count
print('총 금액: {}원'.format(total))


