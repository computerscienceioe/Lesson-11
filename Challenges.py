
# Challenge 1

def challengeOne(n):
  if n == 1:
    print(1)
    return 1
  challengeOneResult = challengeOne(n-1)
  answer = n + challengeOneResult
  print(answer)
  return answer

# print(challengeOne(5))

def challengeTwo(n):
  if n < 5:
    return 1
  return n * challengeTwo(n-1)

# print(challengeTwo(7))


def testChallengeTwo():
  testN = 1
  testAnswer = 1
  if challengeTwo(testN) == testAnswer:
    print("Test passed")
  else:
    print("Test failed")

  testN = 4
  testAnswer = 1
  if challengeTwo(testN) == testAnswer:
    print("Test passed")
  else:
    print("Test failed")

  testN = 5
  testAnswer = 5
  if challengeTwo(testN) == testAnswer:
    print("Test passed")
  else:
    print("Test failed")

  testN = 7
  testAnswer = 210
  if challengeTwo(testN) == testAnswer:
    print("Test passed")
  else:
    print("Test failed")

# testChallengeTwo()

def challengeOne(n):
  if n == 1:
    return 1
  return n + challengeOne(n-1)

def challengeThree(n):
  total = 0
  for i in range(1,n+1):
    total += i
  return total

# print(challengeThree(998))
# print(challengeOne(998))

def challengeFour(n):
  if n <= 1:
    return n
  fibOne = challengeFour(n-1)
  fibTwo = 
  return  + challengeFour(n-2)

def challengeFour(n):
  if n <= 3:
    return n
  return challengeFour(n-1) + challengeFour(n-2) + challengeFour(n-3)

# print(challengeFour(5))
# n(0) = 0
# n(1) = 1
# n(2) = 2
# n(3) = n(2)+n(1)+n(0) = 2+1+0 = 3
# n(4) = n(3)+n(2)+n(1) = 3+2+1 = 6
# n(5) = n(4)+n(3)+n(2) = 6+3+2 = 11

def testChallengeFour():
  testN = 1
  testAnswer = 1
  if challengeFour(testN) == testAnswer:
    print("Test passed")
  else:
    print("Test failed")

  testN = 2
  testAnswer = 2
  if challengeFour(testN) == testAnswer:
    print("Test passed")
  else:
    print("Test failed")

  testN = 3
  testAnswer = 3
  if challengeFour(testN) == testAnswer:
    print("Test passed")
  else:
    print("Test failed")

  testN = 4
  testAnswer = 6
  if challengeFour(testN) == testAnswer:
    print("Test passed")
  else:
    print("Test failed")
  
  testN = 5
  testAnswer = 11
  if challengeFour(testN) == testAnswer:
    print("Test passed")
  else:
    print("Test failed")

# testChallengeFour()

def challengeFive(n):
  total = 1
  for i in range(n):
    total *= 2
  return total

# print(challengeFive(2))

def challengeFiveRecursive(n):
  if n == 0:
    return 1
  return challengeFiveRecursive(n-1) * 2

print(challengeFiveRecursive(10))

# def challengeFiveRecursive(n):
#   if n == 0:
#     return 1
#   return challengeFiveRecursive(n-1) * 2

# print(challengeFiveRecursive(10))



# def challengeFiveRecursive(n):
#   if n == 0:
#     return 1
#   return challengeFiveRecursive(n-1) * 2

# print(challengeFiveRecursive(4))


# def challengeFiveRecursive(n):
#   if n == 0:
#     return 1
#   return challengeFiveRecursive(n-1) * 2

# print(challengeFiveRecursive(4))
