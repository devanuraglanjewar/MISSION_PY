# Break and continue in loop
#break: stops the execution of current iteration, but continues with next one.
#continue: skips the rest of code inside the loop for this iteration only.

for i in range(10):
    if i == 5:
        break   #stop the loop when i is equal to 5
    print("Value of i :",i)
    print("\nEnd of Loop")

for i in range(10):
    if i == 5:
        continue   #skip the rest of code inside the loop for this iteration only
    print("Value of i :",i)
    print("\nEnd of Loop")
    
