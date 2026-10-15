import matplotlib.pyplot as plt

plt.plot([16, 32, 48], [0.96647,0.94935,0.96162],label='Yolov8n')
plt.plot([16,32,48],[0.96336,0.96746,0.96408],label='Yolov8s')
plt.xticks([16, 32, 48], labels=['16','32','64'])
plt.xlabel('Batch_size')
plt.ylabel('recall-precision')
plt.legend()
plt.show()

plt.plot([640, 720, 840], [0.96336,0.95345,0.95789])
plt.xticks([640, 740, 840], labels=['640','720','840'])
plt.xlabel('imgsize')
plt.ylabel('recall-precision')
plt.legend()
plt.show()