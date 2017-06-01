


number = 23
running = True

while running:
    guess = int(raw_input('You can input a number:'))

    if guess == number:
        print 'Congratulations,you guessed it!'  # New block starts here.
        print "(but you do not win any prizes!)"  # New block ends here.
        running = False #end the loop
    elif guess < number:
        print 'Sorry,the number is a little higher than that'  # Another block
        # You can do anything you want in a block...
    else:
        print '不好意思，目标数字比你输入的小一点点'  # test Chinese
else:
    print 'The while loop is over'

print 'Done!'
# Always executed.
