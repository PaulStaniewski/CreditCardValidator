import re

#  Credit Card Validator for American Express, Discover, MasterCard, Visa, Diners Club or Carte Blanche cards.
#  By Paul S.


def main():

    card_number = input("Enter a credit card number: ")  # get the card number from the user

    pattern_visa_master_discover = re.compile(r"\d{4}\D\d{4}\D\d{4}\D\d{4}")  # pattern with any separator
    pattern2_visa_master_discover = re.compile(r"\d{4}\d{4}\d{4}\d{4}")  # pattern with only digits
    pattern_american_express = re.compile(r"\d{4}\D\d{6}\D\d{5}")  # pattern with any separator
    pattern2_american_express = re.compile(r"\d{4}\d{6}\d{5}")  # pattern with only digits
    pattern_diners_club = re.compile(r"\d{4}\D\d{6}\D\d{4}")  # pattern with any separator
    pattern2_diners_club = re.compile(r"\d{4}\d{6}\d{4}")  # pattern with only digits

    # check if the input matches the pattern
    if re.match(pattern_visa_master_discover, card_number) or re.match(pattern2_visa_master_discover, card_number)\
            or re.match(pattern_american_express, card_number) or re.match(pattern2_american_express, card_number)\
            or re.match(pattern_diners_club, card_number) or re.match(pattern2_diners_club, card_number):
        card_number = card_number.replace('-', '')  # remove the separator
        if is_valid(card_number):  # check if the card number is valid, and what brand it is
            if card_number[0:2] == '37':
                print("Card is valid, it is American Express card.")
                continue_program()
            elif card_number[0] == '4':
                print("Card is valid, it is a Visa card.")
                continue_program()
            elif card_number[0] == '5':
                print("Card is valid, it is Mastercard.")
                continue_program()
            elif card_number[0] == '6':
                print("Card is valid, it is Discover card.")
                continue_program()
            if card_number[0] == '3':
                if card_number[0:2] == '37':
                    pass
                else:
                    print("Card is valid, it is Diners Club or Carte Blanche card.")
                    continue_program()
        else:  # if the card number is not valid
            print("The card number is invalid.")
            main()  # ask the user to enter a new card number
    else:  # if the input does not match the pattern
        print("Please enter a valid card number.")
        main()  # call the main function again


def is_valid(number):
    # Check if the card number is valid
    if not is_valid_length(number):  # check if the card number has between 14 and 19 digits
        return False
    elif not is_valid_prefix(number):  # check if the card number starts with 4, 5, 37, or 6
        return False
    elif not is_valid_checksum(number):  # check if the card number passes the Luhn test
        return False
    else:
        return True


def is_valid_length(number):
    # Check if the card number has between 14 and 19 digits
    return 14 <= len(number) <= 19


def is_valid_prefix(number):
    # Check if the card number starts with 3, 4, 5, 37, or 6
    return number[0] == "3" or number[0] == "4" or number[0] == "5" or number[0:2] == "37" or number[0] == "6"


def is_valid_checksum(number):
    # Check if the card number passes the Luhn test

    sum = 0

    for i in range(len(number) - 1, -1, -2):
        sum += int(number[i])
    for i in range(len(number) - 2, -1, -2):
        sum += get_digit(int(number[i]) * 2)
    return sum % 10 == 0


def get_digit(number):
    # Return this number if it is a single digit, otherwise, return the sum of the two digits

    if number < 9:
        return number
    else:
        return number // 10 + number % 10


def continue_program():
    # Ask the user if they want to continue the program
    answer = input("Do you want validate another number? (y/n): ")
    if answer == "y":
        main()
    elif answer == "n":
        print("Thanks for using Credit Card Validator by Paul S.")
    else:
        print("Please enter y or n.")
        continue_program()


if __name__ == "__main__":
    main()
