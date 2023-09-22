from Character import Character
import re
class main:
    storyFileName = "Story.txt"
    myStory = open(storyFileName, "r")
    myStory = myStory.read()

    nameFileName = "Names.txt"
    myNames = open(nameFileName, "r")
    myNames = myNames.readlines()

    #Find the name of the person in the story
    for testname in myNames:
        testname = testname.strip()
        if -1 != myStory.find(testname):
            person = testname

    #Find the Age of the person in the story
    age = list(map(int, re.findall('\d+', myStory)))
    personsAge= age[0]

    #need to do
    languageLearned= 1
    #need to do
    selfEducated= 1
    #need to do
    gotAJob= 1
    
    #Creates a character object
    character = Character(person, personsAge, languageLearned, selfEducated, gotAJob)
    print(character.person)
    print("is the main character and is the age of  " )
    print(character.age)



