def main():

    print("This program validates dates.")

    v = input("Enter the date in the form month/day/year, e.g., 01/13/2016:  ")

    m = v[:2]

    d = v[3:5]
    
    y = v[-4:]

    if m == "01" or "03" or "05" or "07" or "08" or "10" or "12":

        maxd = "31"

        if d > maxd:

            print(v, "is not valid.  This month has only", maxd, "days.")

        else:

            print(v, "seems to be valid.")
            
    elif m == "04" or "06" or "09" or "11":
        
        maxd = "30"

        if d > maxd:

            print(v, "is not valid.  This month has only", maxd, "days.")

        else:

            print(v, "seems to be valid.")

    elif m == "02":    

        maxd = "28"

        if d > maxd:
            
            print(v, "is not valid.  This month has only", maxd, "days.")

        else:

            print(v, "seems to be valid.")
            
    else:

        print("Ooops, something went wrong!")
    
main()


