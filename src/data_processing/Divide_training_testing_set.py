
import random

gold_standard = open('/home/zelalem/Desktop/Named_Entity_Recognantion/CRF_data_set/gold_standard.txt', 'w')
training_data_set = open('/home/zelalem/Desktop/Named_Entity_Recognantion/CRF_data_set/training_set.txt', 'w')

with open("/home/zelalem/Desktop/Named_Entity_Recognantion/CRF_data_set/Raw_Training_set.txt", "rb") as f:
    data = f.read().split('\n')

random.shuffle(data)

gold_data = data[:28464]
training_data = data[28464:]

print ('Training data classification in Progress.....')

for i in gold_data:
    gold_standard.write(i)
    gold_standard.write('\n')

print ('Testing data classification in Progress.....')
for y in training_data:
    training_data_set.write(y)
    training_data_set.write('\n')

gold_standard.close()
training_data_set.close()

