# Take the input of what Jon Marius can say and what the Doctor wants to hear
jonMarius = input()
doctorHear = input()

# If Jon Marius can hold the "Aaah.." longer or equal to the doctor,
# he will go to the doctor
if len(jonMarius) >= len(doctorHear):
    print ("go")
# Otherwise, he will not
else:
    print("no")
