#! python3
# randomQuizgenerator.py - Creates quizzes with questions and answer 
# in random order, along with the answer key.
# 
# The Quiz library have 50 options
# For every student, create 50 questions from the quiz library with 35 
# different quiz files.
# This is the original version of the book with explanation written by me

import random 

# Existed capitals dictionary
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

# create 35 quiz files from capitals in capitalquiz.txt file
# create related answers in capitalsquiz_answers.txt file
for quizNum in range(35):
    # Create the quiz and answer key files.

    # Create 35 capitalsquiz.txt with different affix numbers, such capitalsquiz1.txt
    # Capitalsquiz2.txt, capitalsquiz2.txt
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w') 
    # Create 35 capitalsquiz_answers.txt with affix numbers
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # Write out the header for the quiz.

    # Write some lines in every quizFile
    # Name:
    # 
    #
    # Date:
    #
    #
    # Period:
    #
    #
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    # Write in the middle with quiz number
    #                       State Capitals Quiz... 
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Shuffle the order of the states:

    # Give the keys of the capitals dictionary to states in 
    # a form of list
    states = list(capitals.keys()) 
    # Shuffle the order of states lists
    random.shuffle(states) 


    # Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        # Get right and wrong answer. 
        # Have shuffled states list
        # Create 50 questions for this quiz file

        # For questionNum, create a correct answer 
        # Use corresponded keys to get the values from capitals
        correctAnswer = capitals[states[questionNum]]
        # Give all values go the wrongAnswers
        wrongAnswers = list(capitals.values())
        # Delete the correct answer from wrong answers list
        # By using index of correct answer
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        # Assign random 3 elements from the wrong answers list
        wrongAnswers = random.sample(wrongAnswers, 3)
        # Assign 4 options to the answerOptions 
        answerOptions = wrongAnswers + [correctAnswer]
        # Shuffle the answerOptions
        random.shuffle(answerOptions)

        # Write the question and answer options to the quiz file

        # Create question model with listed number
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            # Create ABCD four options by using i 
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))

        # Write the answer key to a file
        # Give every number the correct answer. 
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 
        'ABCD'[answerOptions.index(correctAnswer)]))

    # Close opened file for each quiz loop in the end
    # to avoid error
    quizFile.close()
    answerKeyFile.close()
