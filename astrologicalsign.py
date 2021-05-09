# Compare the day and month of the input,
# to the chart from the problem and print out the astrological sign
for i in range (int(input())):
    number, month = input().split()
    number = int(number);  month = str(month)
    if month == "Mar":
        if number >=21:
            print("Aries")
        else:
            print("Pisces")

    elif month == "Apr":
        if number >=21:
            print("Taurus")
        else:
            print("Aries")

    elif month == "May":
        if number >=21:
            print("Gemini")
        else:
            print("Taurus")

    elif month == "Jun":
        if number >=22:
            print("Cancer")
        else:
            print("Gemini")

    elif month == "Jul":
        if number >=23:
            print("Leo")
        else:
            print("Cancer")

    elif month == "Aug":
        if number >=23:
            print("Virgo")
        else:
            print("Leo")

    elif month == "Sep":
        if number >=22:
            print("Libra")
        else:
            print("Virgo") 
    
    elif month == "Oct":
        if number >=23:
            print("Scorpio")
        else:
            print("Libra")  

    elif month == "Nov":
        if number >=23:
            print("Sagittarius")
        else:
            print("Scorpio")

    elif month == "Dec":
        if number >=22:
            print("Capricorn")
        else:
            print("Sagittarius")  

    elif month == "Jan":
        if number >=21:
            print("Aquarius")
        else:
            print("Capricorn")

    elif month == "Feb":
        if number >=20:
            print("Pisces")
        else:
            print("Aquarius") 
