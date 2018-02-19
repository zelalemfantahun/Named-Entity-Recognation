import nltk
from nltk.tag.stanford import StanfordPOSTagger
#
# path_to_tagger = '/home/zelalem/Downloads/stanford-postagger-2014-08-27/models/english-bidirectional-distsim.tagger'# import st
# stanford_postagger_jar = '/home/zelalem/Downloads/stanford-postagger-2014-08-27/stanford-postagger.jar'
# st = StanfordPOSTagger(path_to_tagger, stanford_postagger_jar)

crfsuite_data = open('/home/zelalem/Desktop/Named_Entity_Recognantion/CRF_data_set/zelalem_test_data.txt', 'w') # open the file to write features

with open('/home/zelalem/Desktop/Named_Entity_Recognantion/CRF_DATA/raw_training/crf_data1.txt', 'r') as f: # read a raw training data
    train_token = f.read().rstrip('\n')

train_token = nltk.sent_tokenize(train_token) # sentence tokinization using nltk
# print(train_token)
with open('/home/zelalem/Desktop/Named_Entity_Recognantion/CRF_data_set/BuildDirect_data/final_product_list.txt',  newline='\n') as t: # read a product list
    data_t = t.read().rstrip('\n')

product_list=[]
for words in data_t.split('\n'):
    product_list.append(words)



for x in train_token:
    train_token = nltk.word_tokenize(x)
    print (train_token)
    for i in (range(len(train_token))):

        current_word = train_token[i]

        current_word = current_word.split()
        print (current_word)
        current_word = (str(current_word))
        current_word = current_word.strip("'[")
        current_word = current_word.strip("']")
        current_pos = nltk.pos_tag(current_word)

        current_pos = (current_pos[0][1])
        print (current_pos)
        previous_word = train_token[i - 1]
        previous_pos = nltk.pos_tag(previous_word)
        previous_pos = (previous_pos[0][1])

        try:
            next_word = train_token[i+1].splitlines()
            next_word = str(next_word)
            next_word = next_word.strip("'[")
            next_word = next_word.strip("']")
            next_pos = nltk.pos_tag(next_word)
            next_pos = (next_pos[0][1])


            try:
                next_two = train_token[i+2]

            except IndexError:
                next_two = "."

        except IndexError:
            next_word = "."
            next_two = "."



        if i - 1 < 0:
            previous_word = "."
        else:

            previous_word = train_token[i-1].splitlines()
            previous_word = str(previous_word)
            previous_word = previous_word.strip("'[")
            previous_word = previous_word.strip("']")
            previous_pos = nltk.pos_tag(previous_word)
            previous_pos = (previous_pos[0][1])

        if i - 2 < 0:
            previous_two = '.'
        else:
            previous_two = train_token[i - 2]

        if current_word in product_list:

            word_found = (current_word+' '+'PRODUCT')
            word_found = word_found.split()
            pro = str(word_found[1])
            cur_word = str(word_found[0])

            final_word_found = (pro+'\t'+'word=' + cur_word + '\t' + 'cur_pos=' + current_pos + '\t' + 'next_word=' + str(
                next_word) + '\t' + 'next_pos=' + next_pos + '\t' + 'prev_word=' + previous_word + '\t' + 'prev_pos=' + previous_pos + '\t' + 'next_two=' + str(
                next_two) + '\t' + 'prev_two=' + str(previous_two))

            crfsuite_data.write(final_word_found)
            crfsuite_data.write('\n')

        else:
            word_not_found = (str(current_word)+' '+'OTHER')
            word_not_found = (word_not_found.split())
            pro_no = str(word_not_found[1])
            curword = str(word_not_found[0])

            final_word_notfound = (pro_no+ '\t' +'word=' + curword + '\t' + 'cur_pos=' + current_pos + '\t' + 'next_word=' + str(
                next_word) + '\t' + 'next_pos=' + next_pos + '\t' + 'prev_word=' + previous_word + '\t' + 'prev_pos=' + previous_pos + '\t' + 'next_two=' + str(
                next_two) + '\t' + 'prev_two=' + str(previous_two))

            crfsuite_data.write(final_word_notfound)
            crfsuite_data.write('\n')

        bigrams_words = (str(current_word) + ' ' + next_word) # constract bigrams

        if product_list.__contains__ (bigrams_words):
            bigram_found = (bigrams_words + ' ' + 'PRODUCT')
            bigram_found = bigram_found.split()
            bi1 = str(bigram_found[0])
            bi2 = str(bigram_found[1])
            bi3 = str(bigram_found[2]) #bigram product category
            bigram =(bi1 +' '+ bi2)

            bigram_final = (bi3+ '\t' +'word=' + bigram + '\t' +'cur_pos='+'NP'+'\t' +'next_word=' + str(next_word) + '\t' + 'next_pos=' + next_pos + '\t' + 'prev_word=' + previous_word + '\t' + 'prev_pos=' + previous_pos + '\t' + 'next_two=' + str(
                next_two) + '\t' + 'prev_two=' + str(previous_two))

            crfsuite_data.write(bigram_final)
            crfsuite_data.write('\n')
        try:

            next_next_word = train_token[i + 2]
            next_next_word = str(next_next_word)
            trigram_words = (current_word + ' ' + next_word + ' ' + next_next_word)  # constract trigram
            if product_list.__contains__(trigram_words):

                trigram_found = (trigram_words + ' ' + 'PRODUCT')
                trigram_found = trigram_found.split()
                tri1 = str(trigram_found[0])
                tri2 = str(trigram_found[1])
                tri3 = str(trigram_found[2])
                tri4 = str(trigram_found[3]) # trigram product category
                trigram = (tri1+' '+tri2+' '+tri3)
                # print (trigram)

                trigram_final = (tri4 + '\t' + 'word=' + trigram + '\t' + 'cur_pos=' + 'NP' + '\t' + 'next_word=' + str(
                    next_word) + '\t' + 'next_pos=' + next_pos + '\t' + 'prev_word=' + previous_word + '\t' + 'prev_pos=' + previous_pos + '\t' + 'next_two=' + str(
                    next_two) + '\t' + 'prev_two=' + str(previous_two))

                crfsuite_data.write(trigram_final)
                crfsuite_data.write('\n')

        except:
            break

        try:
            next_two_words = train_token[i+3]
            next_two_words = str(next_two_words)
            quadragrams_words = (current_word + ' ' + next_word + ' ' + next_next_word+' '+next_two_words)
            # print (quadragrams_words)
            if product_list.__contains__(quadragrams_words):
                quadragram_found = (quadragrams_words +' '+'PRODUCT')
                quadra1 = str(quadragram_found[0])
                quadra2 = str(quadragram_found[1])
                quadra3 = str(quadragram_found[2])
                quadra4 = str(quadragram_found[3])
                quadra5 = str(quadragram_found[4]) #quadragrams_product category
                quadragrams =(quadra1+' '+quadra2+' '+quadra3+' '+quadra4)

                quadragrams_final = (quadra5 + '\t' + 'word=' + quadragrams + '\t' + 'cur_pos=' + 'NP' + '\t' + 'next_word=' + str(
                    next_word) + '\t' + 'next_pos=' + next_pos + '\t' + 'prev_word=' + previous_word + '\t' + 'prev_pos=' + previous_pos + '\t' + 'next_two=' + str(
                    next_two) + '\t' + 'prev_two=' + str(previous_two))

                crfsuite_data.write(quadragrams_final)
                crfsuite_data.write('\n')

        except:
            break

crfsuite_data.close()
f.close()
t.close()