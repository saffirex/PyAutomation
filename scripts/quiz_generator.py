import random, quizzie

for quiznum in range(10):
    file= open(f'capitals{quiznum+1}.txt','w')
    ans_key= open(f'capitals_ans{quiznum+1}.txt', 'w')
    
    file.write('Name:\n\n Date: \n\n Roll num:\n\n')
    file.write(f'State Capitals Quiz {quiznum+1}'.center(10, '*'))
    file.write('\n\n')

    states = list(quizzie.capitals.keys())
    random.shuffle(states)

    for qn in range(20):
        rightans=quizzie.capitals[states[qn]] #states[qn]= random name of state from the shuffled list states which later acts as the key for accessing from the capitals dictionary
        wrongans= list(quizzie.capitals.values()) #list of all the values in the dictionaryt
        del wrongans[wrongans.index(rightans)] #deletes the right answer from the lsit of values, after getting its index
        wrongans=random.sample(wrongans, 3) #gets 3 random values of ans in a list
        options= wrongans + [rightans] #adds correct ans to the list of wrongans
        random.shuffle(options) #randomizes the list of options so that the correct ans isn't always the last

        file.write(f'{qn+1}. What is the capital of {states[qn]}?\n')
        for abcd in range(4):
            file.write(f"{'ABCD'[abcd]}. {options[abcd]}\n")
            file.write("\n")
        
        ans_key.write(f"{qn+1}.{'ABCD'[options.index(rightans)]}")

    file.close()
    ans_key.close()
