# Ashit Neema
# email : ashit.neema@usu.edu
# DataBased take home assessment

# PROBLEM 1 - Least Factorial
# Given an integer n, find the minimal k such that
# k = m! (where m! = 1 * 2 * ... * m) for some integer m; k ≥n. In other
# words, find the smallest factorial which is not less than n.

def leastFactorial(n):
    if n < 1 or n > 120:
        return None

    i = 2
    current_factorial = 1
    while i < n + 1:
        current_factorial *= i
        if current_factorial >= n:
            return current_factorial
        i += 1


def testLeastFactorial():
    print('-' * 20)
    print('Part 1: Least Factorial')

    assert leastFactorial(17) == 24
    assert leastFactorial(5) == 6
    assert leastFactorial(106) == 120
    assert leastFactorial(125) is None
    assert leastFactorial(-10) is None
    # TODO: add your own test cases here

    print('PASSED PROBLEM 1!')


# PROBLEM 2 - Reclying Lipstick
# You own a lipstick business. When a lipstick container is empty, there is actu-
# ally some leftover lipstick at the bottom that cannot be used because it is not
# accessible. Being an environmentally friendly business owner, you would like to
# recycle the leftover lipstick to make more. As a business, you know you need
# ‘numberOfLeftoversNeeded‘ to make a new lipstick. You have ‘numberOfLip-
# sticks‘ in your possession. What’s the total number of lipsticks you can sell
# assuming that each of your customers return their leftovers

def getTotalNumberOfLipsticks(numberOfLipsticks, numberOfLeftoversNeeded):
    if numberOfLipsticks <= 0:
        return 0

    if numberOfLeftoversNeeded <= 0:
        return None

    if numberOfLeftoversNeeded > numberOfLipsticks:
        return numberOfLipsticks

    lipsticks_created = 0
    current_lipsticks = numberOfLipsticks

    while numberOfLipsticks >= numberOfLeftoversNeeded:
        remaining_leftover = (numberOfLipsticks % numberOfLeftoversNeeded)
        recycled_lipsticks = int(numberOfLipsticks / numberOfLeftoversNeeded)
        numberOfLipsticks = recycled_lipsticks + remaining_leftover
        lipsticks_created += recycled_lipsticks

    lipsticks_sold = current_lipsticks + lipsticks_created

    return lipsticks_sold


def testLipsticks():
    print('\n' + '-' * 20)
    print('Part 2: Lipsticks')
    assert getTotalNumberOfLipsticks(5, 2) == 9
    assert getTotalNumberOfLipsticks(15, 5) == 18
    assert getTotalNumberOfLipsticks(2, 3) == 2
    assert getTotalNumberOfLipsticks(0, 3) == 0
    assert getTotalNumberOfLipsticks(2, 0) is None
    # TODO: add your own test cases here

    print('PASSED PROBLEM 2!')


# PROBLEM 3 - Students and Treats
# A school teacher wants to hand out treats to his students. The teacher de-
# cides the best way to divide the treats is to have the students sit in a circle of
# sequentially numbered chairs. A chair number will be drawn from a hat. Begin-
# ning with the student in drawn chair, one treat will be handed to each student
# sequentially going around the circle until all treats have been distributed.
# The teacher wants to have the students involved in sharing treats. He decides
# that whoever gets the very last treat, will be the student who makes the treats
# for the next game. Determine the chair number occupied by the student who
# will receive the last treat.

# For example, there are 4 students and 6 treats. The students arrange them-
# selves in seats numbered 1 to 4. Let’s suppose 2 is drawn from the hat. Students
# receive treats at positions 2,3,4,1,2,3. The student who gets the last treat is in
# chair number 3

def getLastStudent(numberOfStudents, treats, startingChair):
    if numberOfStudents <= 0 or startingChair <= 0 or startingChair > numberOfStudents or treats <= 0:
        return None

    last_index = startingChair + treats - 1
    if last_index <= numberOfStudents:
        return last_index
    actual_last_student = last_index % numberOfStudents
    if actual_last_student == 0:
        return startingChair

    return actual_last_student

def testLastStudent():
    print('\n' + '-' * 20)
    print('Part 3: Students and Treats')
    assert getLastStudent(5, 2, 1) == 2
    assert getLastStudent(5, 2, 2) == 3
    assert getLastStudent(5, 4, 2) == 5
    assert getLastStudent(7, 19, 2) == 6
    assert getLastStudent(3, 7, 3) == 3
    assert getLastStudent(0, 7, 3) is None
    assert getLastStudent(7, 0, 3) is None
    assert getLastStudent(7, 7, 0) is None
    assert getLastStudent(7, 10, 0) is None
    assert getLastStudent(876756888, 2, 876756887) == 876756888
    assert getLastStudent(876756888, 2, 876756888) == 1

    # TODO add your own test cases here

    print('PASSED PROBLEM 3!')


def getPairsOfShoes(listOfShoes):
    if len(listOfShoes) <= 1:
        return 0

    total_pairs = 0
    check_set = set()

    for shoes in listOfShoes:
        if type(shoes) != str:
            return None
        if shoes in check_set:
            total_pairs += 1
            check_set.remove(shoes)
        else:
            check_set.add(shoes)

    return total_pairs

# PROBLEM 4 - Pairs of Shoes
# Given an array of strings that represent a type of shoe, return how many matching
# pairs of shoes can be made?

def testPairsOfShoes():
    print('\n' + '-' * 20)
    print('Part 4: Pairs of Shoes')

    assert getPairsOfShoes(["red", "blue", "red", "green", "green", "red"]) == 2
    assert getPairsOfShoes(["green", "blue", "blue", "blue", "blue", "blue", "green"]) == 3
    assert getPairsOfShoes([]) == 0
    assert getPairsOfShoes(["green", "blue", 45, "blue", "blue", "blue", "green"]) is None
    # TODO: Add your own test cases here

    print('PASSED PROBLEM 4!')
    print('\n\nCongratulations!!')


# Call test functions
testLeastFactorial()
testLipsticks()
testLastStudent()
testPairsOfShoes()
