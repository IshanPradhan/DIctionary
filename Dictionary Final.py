import json
from difflib import get_close_matches
data = json.load(open("data.json"))

try:
    def translate(wrd):
        wrd = wrd.lower()   # converts the word into lower case

        if wrd in data:
            return data[wrd]
        elif wrd.title() in data:  # for condition where user Enter Delhi instead of delhi
            return data[wrd.title()]
        elif wrd.upper() in data:  # in case user enters words like USA
            return data[wrd.upper()]
        elif len(get_close_matches(wrd, data.keys())) >0:
            choice = input("Did you mean %s instead? Enter Y if Yes ,or N if no\n" % get_close_matches(wrd, data.keys())[0])
            if choice == "y" or choice == "Y":
                return data[get_close_matches(wrd, data.keys())[0]]
            elif choice == "n" or choice == "N":
                return "The Desired word Doesn't Exist\nPlease re-check it!\n" \
                       "Thank you for using the App!\n" \
                       "You can try it again though as many times as want!"
            else:
                return "Please Enter valid choice!"
        else:
            return "The Entered word doesn't exist please re-check it!!"

    word = input("Enter word: ")

    output = translate(word)

    if type(output) == list:
        for items in output:
            print(items)

    else:
        print(output)

except KeyError:
    print("The Entered word doesn't exits please re-check it!!")

