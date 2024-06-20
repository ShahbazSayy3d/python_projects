email = input("Enter your Email: ")

k, j, d = 0, 0, 0  

if len(email) >= 6:

    if email[0].isalpha():

        if ('@' in email) and (email.count('@') == 1):

            if (email[-4] == ".") ^ (email[-3] == "."):  #^XOR operator checks either one condition to be true

                for i in email:
                    if i == i.isspace():
                        k = 1  # Set k to 1 if there is any whitespace character

                    elif i.isalpha():
                        if i == i.upper():  # Check if the character is uppercase
                            j = 1  # Set j to 1 if there is any uppercase alphabet

                    elif i.isdigit():
                        continue  # Skip digits

                    elif i == "_" or i == "." or i == "@":
                        continue  # Skip specific characters

                    else:
                        d = 1  # Set d to 1 if there is any other character that doesn't match the conditions


                if k == 1 or j == 1 or d == 1:
                    print("Wrong Email: 5")
                else:
                    print("Correct Email")
            else:
                print("Wrong Email: 4 Incorrect position of '.'")
        else:
            print("Wrong Email: 3 Incorrect number of '@' symbols")
    else:
        print("Wrong Email: 2 First character must be alphabetic")
else:
    print("Wrong Email: 1 Length should be at least 6 characters")
