import os

def convert_and_save_yolo_label(original_label_path, image_width, image_height):
    for filename in os.listdir(original_label_path):
        if filename.endswith('.txt'):
            with open(original_label_path+'\\'+filename, 'r') as original_label_file:
                lines = original_label_file.readlines()

            yolo_label = []
            for line in lines:
                class_id, x1, y1, x2, y2 = map(float, line.strip().split())
                x_center = (x1 + x2) / 2.0
                y_center = (y1 + y2) / 2.0
                width = abs(x2 - x1)
                height = abs(y2 - y1)
            
                # 이미지 크기에 따라 좌표 스케일링
                x_center, y_center, width, height = x_center * image_width, y_center * image_height, width * image_width, height * image_height
                yolo_label.append(f'{int(class_id)} {x_center} {y_center} {width} {height}\n')

            with open(original_label_path+'\\'+filename, 'w') as yolo_label_file:
                yolo_label_file.writelines(yolo_label)

convert_and_save_yolo_label('test/labels',1920,1080)
convert_and_save_yolo_label('train/labels',1920,1080)
convert_and_save_yolo_label('valid/labels',1920,1080)