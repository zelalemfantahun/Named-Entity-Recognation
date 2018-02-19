from nltk.tag import CRFTagger
import ast
ct = CRFTagger()
import re

test_set = open('/home/zelalem/Desktop/Named_Entity_Recognantion/CRF_data_set/sample_testing.txt','r') # reading the testing set here
test_set = test_set.read().split('\n')
test_set = filter(lambda x: not re.match(r'^\s*$', x), test_set)

with open('/home/zelalem/Desktop/Named_Entity_Recognantion/CRF_data_set/sample_training.txt') as f: # reading the tarining set here
    read_line = f.read().splitlines()
    read_lines = filter(lambda x: not re.match(r'^\s*$', x), read_line)

with open('/home/zelalem/Desktop/Named_Entity_Recognantion/CRF_data_set/sample_gold.txt') as f: # reading the gold standard here
    gold_line = f.read().splitlines()
    gold_line = filter(lambda x: not re.match(r'^\s*$', x), read_line)

tagged_text = open('/home/zelalem/Desktop/Named_Entity_Recognantion/CRF_data_set/test_tagged_data.txt', 'w') # writing the tagged data


train_data = []
test_data = []
gold_data = []
number_lines = 0

for i in read_lines:
    i = "[" + i + "]"
    lists_e = ast.literal_eval(i)
    train_data.append(lists_e)

print ('Training the CRF++ model started')
ct.train(train_data,'model.crf.tagger') # training the crf model using the training set
print ('Training the CRF++ model completed')

test_number_lines = 0
print ('Reading Unseen Data')
for lines in test_set:
    test_number_lines = test_number_lines + 1
    print('Processing file', test_number_lines)
    xx = (lines.split())
    test_data.append(xx)


tagged_sent = ct.tag_sents(test_data) # tagging the the unseen data

for tag_set in tagged_sent:
    tagged_text.write(str(tag_set))
    tagged_text.write('\n')

tagged_text.close()
print ('Tagging the Unseen data Completed')

for vz in gold_line:
    vz = "[" + vz + "]"
    gold_list = ast.literal_eval(vz)
    gold_data.append(gold_list)

print ('The Total Accuracy of the System is:'+str(ct.evaluate(gold_data)))