import np as np
from Character import Character
import re
class main:

    storyFileName = "Story.txt"
    myStory = open(storyFileName, "r")
    myStory = myStory.read()
    #reduces all of the characters is the story txt to lowercase
    myStory = myStory.lower()

    nameFileName = "Names.txt"
    myNames = open(nameFileName, "r")
    myNames = myNames.readlines()

    programmingNameFileName = "ProgramLanguages.txt"
    myProgramNames = open(programmingNameFileName, "r")
    myProgramNames = myProgramNames.readlines()

    learningWaysFileName = "WaysToLearn.txt"
    myLearningTypes = open(learningWaysFileName, "r")
    myLearningTypes = myLearningTypes.readlines()

    jobStatusFileName = "JobStatus.txt"
    myJobStatus = open(jobStatusFileName, "r")
    myJobStatus = myJobStatus.readlines()


    arrOne = np.array([myNames])
    arrTwo = np.array([myProgramNames])
    arrThree = np.array([myLearningTypes])
    arrFour = np.array([myJobStatus])
    data = np.vstack([arrOne, arrTwo, arrThree, arrFour])
    x = 0
    y = 0

    #This will loops through all the arrays stored in the data array and assign the value that pertains to the location of the arrys
    while x < len(data):
        while y <= len(myNames):
            #Gets the lowercase value on each line of the text document stored in the array and changes the word to be lowercase
            value = data[x][y].strip().lower()
            #Checks to see if the value exsists inside the story.txt file
            if -1 != myStory.find(value):
                #each data value is assigned a stop within the data array. This will allign with the parameter needed
                if x == 0:
                    person = value
                    y = 0
                    break
                elif x == 1:
                    languageLearned = value
                    y = 0
                    break
                elif x == 2:
                    selfEducated = value
                    y = 0
                    break
                elif x == 3:
                    gotAJob = value
                    break
            y += 1
        x += 1

    # Find the Age of the person in the story
    age = list(map(int, re.findall('\d+', myStory)))
    personsAge = age[0]

    # Creates a character object and assigns all the values found in the text documents to it
    character = Character(person, personsAge, languageLearned, selfEducated, gotAJob)
    print(str(character.person) + " is the main character and is the age of " + str(character.age) )
    print("He was " + str(character.selfEducated) + " and learned the langues of " + str(character.languageLearned))
    print("With this information his current job status is"+ str(character.gotAJob) )

