# answer =int(input()) #provide answer
#  guess =int(input()) #provide guess
answer = 35
guess = 34
result = ''
if answer > guess:  # provide conditional
    result = "Oops!  Your guess was too low."
elif answer < guess:  # provide conditional
    result = "Oops!  Your guess was too high."
elif answer == guess:  # provide conditional
    result = "Nice!  Your guess matched the answer!"

print(result)
