
read_dialogue = open('/home/zelalem/Desktop/Named_Entity_Recognantion/Test_Dialogues.txt','r')
write_dialogue = open('/home/zelalem/Desktop/Named_Entity_Recognantion/Dialogues_Atomese.scm','w')
dialogue = read_dialogue.read().splitlines()
line_count = 0
list_of_answer = []
list_of_question = []

for i in range(len(dialogue)):
    dialogue_list = dialogue[i]
    line_count +=1

    if (line_count % 2 == 0): #even
        answers = (dialogue_list.split())
        for answer in answers:
            list_of_answer.append(answer)

        final_answers = (
        '\t''(ListLink''\n'
        )
        write_dialogue.write(final_answers)
        for x in list_of_answer:
            final_answers = (

            '\t''\t''(''word' ' ' '"'+x+ '"'')'
            '\n'
            )
            write_dialogue.write(final_answers)
        final_answers = (
        '\t'')''\n'
        '\t''(Concept'' ''"AIML chat subsystem goal"'')''\n'
        '\t''(''stv 1 0.25' ')''\n'
        '\t' '(' 'psi-demand'' ''"AIML chat demand"'' ''0.97' ')''\n'

        ')''\n'
        )
        write_dialogue.write(final_answers)
        write_dialogue.write('\n')
    else: #odd
        questions = (dialogue_list.split())
        for question in questions:
            list_of_question.append(question)

        final_questions = (
        "(psi-rule-nocheck" '\n'
        '\t' "(list(AndLink" '\n'
        '\t''\t'"(Evaluation"'\n'
        '\t''\t''\t'"(Predicate"' ''"''says''"'')''\n'
        '\t''\t''\t'"(ListLink"'\n'

        )
        write_dialogue.write(final_questions)


        for y in list_of_question:
            final_questions = ('\t''\t''\t''\t' "(Word" ' ' '"'  +y+ '"' ')')
            write_dialogue.write(final_questions)
            write_dialogue.write('\n')

        final_questions = (
            '\t''\t''\t'')'')''\n'
            '\t'')'')'
            '\n'
        )
        write_dialogue.write(final_questions)
write_dialogue.close()
print ("done")

