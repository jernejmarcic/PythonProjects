sentence = str(input("Enter the sentence: "))
print(sentence.count(" ") + 1)
# The solution is suboptimal, it requires the user to be corret, since it counts whitescpace and assumes there will be no extra whitespace.