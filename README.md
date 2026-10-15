# Market YOLO Checkout

인공지능프로그래밍 수업 프로젝트. YOLOv8로 상품을 인식하고 `Price.xlsx`의 가격표로 합계를 계산하는 무인 계산 시스템입니다.

- `Payment(main).py` : 이미지에서 상품을 검출해 가격을 계산하는 메인 코드
- `yolo_train.py`, `item.yaml`, `class.txt` : YOLOv8 학습 설정
- `Hyperparameter_tuning/` : 이미지 크기·배치·모델 크기별 실험 결과(그래프, 지표)
- `Best_model/` : 최종 선택 모델과 `best.pt` 가중치
- `make_graph (hyperparameter).py` : 실험 결과 비교 그래프

학습 데이터셋과 실험별 가중치는 용량 때문에 제외했습니다.
