# randomQuizGenerator_byMe - create quiz files and answer files

# The randomQuizGenerator_byMe is original from randomQuizGenerator.py
# I write this file by me getting rid of the original file

# From the capitals dictionary, we should create 35 files with different 50 random questions
# Every question have 4 answers, 1 correct answer and 3 wrong answer

import random 

capitals = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 
    'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 
    'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 
    'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 
    'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 
    'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 
    'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 
    'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 
    'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 
    'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 
    'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 
    'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
    'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
    }

# Create 35 questionFile.txt files and 35 answerFile.txt files with 35 listed affixes.
for fileNum in range(35):
    questionFile = open('questionFile%s.txt' % (fileNum + 1), 'w')
    answerFile = open('answerFile%s.txt' % (fileNum + 1), 'w')

    # Add head for every questionFile.txt
    questionFile.write('Name:\n\nDate:\n\nPeriod\n\n')
    questionFile.write((' ' * 20) + 'State Capitals (Quiz %s)' % (fileNum + 1))
    questionFile.write('\n\n')

    # Shuffle the the order of key of related question
    states = list(capitals.keys())
    random.shuffle(states)

    # Create 50 questions for every questionFile.txt and answers
    for questionNum in range(50):
        # Choose one key, get its value from capitals as correct answer
        correctAnswer = capitals[states[questionNum]]
        # Give other values to a wrong answer list 
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer, 3)
        # Create 4 options
        answersOption = wrongAnswer + [correctAnswer]
        random.shuffle(answersOption)

        # Create question
        questionFile.write('%s What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            questionFile.write(' %s. %s\n' % ('ABCD'[i], answersOption[i]))
        # Create a new line for each question
        questionFile.write('\n')

        # Create related answers for every quiz file
        # \n Create a new line for each correct answer
        answerFile.write('%s. %s\n' % (questionNum + 1, 
        'ABCD'[answersOption.index(correctAnswer)]))
    
    # Close files
    questionFile.close()
    answerFile.close()