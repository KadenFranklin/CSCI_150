from typing import *
import math

# Kaden Franklin
# Last letter first letter(Countries edition).py

def choose_difficulty():
    print("Welcome to the Last letter First letter word game "\
          "(Country edition).\n"
        "In this game two players continually name countries with"\
        " matching ending and starting letters until"\
          " one player quits.  \n"
        "There are two difficulty modes: easy, and hard.\n"
        "Easy mode allows players to use "\
          "countries with names of any length. \n"
        "Hard mode only allows players to use countries with names"\
          " longer than 8 characters ")
    y : bool = False
    choose = str(input("To select your difficulty please"\
                       " input 'easy', or 'hard'."))
    while y == False:

        if choose.lower() == "easy" :
            y = True
            easy_mode()
        elif choose.lower == "hard" :
            y = True
            hard_mode()
        else:
            choose = str (input("I'm sorry that is not a valid input."\
                                " Please input 'easy', or 'hard'"))

def rerun():
    x = str(input("Would you like to play again, please respond"\
                  " with 'Yes' or 'No'."))
    if x.lower() == "yes" :
        main()
    elif x.lower() == "no":
        quit()
    else:
        x = str(input("Would you like to play again, "\
                      " please respond with 'Yes' or 'No'."))

def is_country_check(x : str) -> bool:
    all_countries_list : List (str) = ["afghanistan", "akrotiri", "albania", \
                                   "algeria", "american samoa", \
                                   "andorra", "angola", "anguilla", \
                                   "antarctica", "antigua", "barbuda", \
                                   "argentina", "armenia", "aruba", \
                                   "ashmore", "cartier islands", \
                                   "australia", \
                                   "austria", "azerbaijan", \
                                   "aahamas", "bahrain", \
                                   "bangladesh", "barbados", \
                                   "bassas da india", \
                                   "belarus", "belgium", "belize", \
                                   "benin", \
                                   "bermuda", "bhutan", "bolivia", \
                                   "bosnia", \
                                   "herzegovina", "botswana", \
                                   "bouvet island", \
                                   "brazil", \
                                   "british indian ocean territory", \
                                   "british virgin islands", \
                                   "brunei", "bulgaria", \
                                   "burkina faso", "burma", \
                                   "burundi", "cambodia", \
                                   "cameroon", "canada", "cape verde", \
                                   "cayman islands", \
                                   "central african republic", \
                                   "chad", "chile", \
                                   "china", "christmas island", \
                                   "clipperton island", \
                                   "cocos islands", \
                                   "keeling islands", \
                                   "colombia", "comoros", \
                                   "democratic republic of the congo", \
                                   "republic of the congo", "cook islands", \
                                   "coral sea islands", "costa rica", \
                                   "cote d'ivoire", "croatia", "cuba", \
                                   "cyprus", \
                                   "czech republic", "denmark", "dhekelia", \
                                   "djibouti", "dominica", \
                                   "dominican republic", \
                                   "ecuador", "egypt", "el salvador", \
                                   "equatorial guinea", "eritrea", \
                                   "estonia", \
                                   "ethiopia", "europa island", \
                                   "falkland islands", \
                                   "islas malvinas", "faroe islands", \
                                   "fiji", \
                                   "finland", "france" "french guiana", \
                                   "french polynesia", "french southern", \
                                   "antarctic lands", "gabon", "gambia", \
                                   "the gambia", "gaza strip", \
                                   "georgia", "germany", \
                                   "ghana", "gibraltar", "glorioso islands", \
                                   "greece", "greenland", "grenada", \
                                   "guadeloupe", \
                                   "guam", "guatemala", "guernsey", \
                                   "guinea", \
                                   "guinea-bissau", "guyana", "haiti", \
                                   "heard island",  "mcdonald islands", \
                                   "holy see", \
                                   "vatican city", "honduras", "hong kong", \
                                   "hungary", \
                                   "iceland", "india", "indonesia", \
                                   "iran", "iraq", \
                                   "ireland", "isle of man", "israel", \
                                   "italy", \
                                   "jamaica", "jan mayen", "japan", \
                                   "jersey", \
                                   "jordan", "juan de nova island", \
                                   "kazakhstan", \
                                   "kenya", "kiribati", "north korea", \
                                   "south korea", \
                                   "kuwait", "kyrgyzstan", "laos", \
                                   "latvia", "lebanon", \
                                   "lesotho", "liberia", "libya", \
                                   "liechtenstein", \
                                   "lithuania", "luxembourg", "macau", \
                                   "macedonia", \
                                   "madagascar", "malawi", "malaysia", \
                                   "maldives", \
                                   "mali", "malta", "marshall islands", \
                                   "martinique", \
                                   "mauritania", "mauritius", \
                                   "mayotte", "mexico", \
                                   "federated states of micronesia", \
                                   "moldova", \
                                   "monaco", "mongolia", "montserrat", \
                                   "morocco", \
                                   "mozambique", "namibia", "nauru", \
                                   "navassa island", \
                                   "nepal", "netherlands", \
                                   "netherlands antilles", \
                                   "new caledonia", "new zealand", \
                                   "nicaragua", \
                                   "niger", "nigeria", "niue", \
                                   "norfolk island", \
                                   "northern mariana islands", "norway", \
                                   "oman", \
                                   "pakistan", "palau", "panama", \
                                   "papua new guinea", "paracel islands", \
                                   "paraguay", "peru", "philippines", \
                                   "pitcairn islands", "poland", "portugal", \
                                   "puerto rico", "qatar", "reunion", \
                                   "romania", \
                                   "russia", "rwanda", "saint helena", \
                                   "saint kitts", "nevis", "saint lucia", \
                                   "saint pierre", "miquelon", \
                                   "saint vincent", \
                                   "grenadines", "samoa", "san marino", \
                                   "sao tome", "principe", "saudi arabia", \
                                   "senegal", "serbia", "montenegro", \
                                   "seychelles", "sierra leone", \
                                   "singapore", \
                                   "slovakia", "slovenia", \
                                   "solomon islands", \
                                   "somalia", "south africa", \
                                   "south georgia", \
                                   "south sandwich islands", "spain", \
                                   "spratly islands", "sri lanka", \
                                   "sudan", "suriname", "svalbard", \
                                   "swaziland", "sweden", "switzerland", \
                                   "syria", "taiwan", "tajikistan", \
                                   "tanzania", \
                                   "thailand", "timor-leste", "togo", \
                                   "tokelau", "tonga", "trinidad", \
                                   "tobago", "tromelin island", \
                                   "tunisia", "turkey", "turkmenistan", \
                                   "turks islands", "caicos islands", \
                                   "tuvalu", "uganda", "ukraine", \
                                   "united arab emirates", "united kingdom", \
                                   "united states", "uruguay", "uzbekistan", \
                                   "vanuatu", "venezuela", "vietnam", \
                                   "virgin islands", "wake island", \
                                   "wallis", "futuna", "west bank", \
                                   "western sahara", "yemen", \
                                   "zambia", "zimbabwe"]
    if all_countries_list.count(x.lower()) > 0 :
        return True
    else :
        return False

def turn_counter(x: int) -> str:
    if x % 2 == 0 :
        return "It is Player 2's turn."
    else :
        return "It is Player 1's turn."

def last_let_first_let_checker(x : List[str], y : str) -> bool:
    if x == [] and is_country_check(y) :
        return True
    elif x != []:
        z = (x[-1])
        if z[-1] == y[0]:
            return True
    else:
        return False

def easy_mode() :
    turn_counter_int = 0
    country_list : List = []
    quit_bool = False
    while quit_bool == False:
        turn_counter_int += 1
        print(f"{turn_counter(turn_counter_int)}\n"
              f"The score is currently: {turn_counter_int}.")
        country_question_bool = False
        while country_question_bool == False:
            country_question = str (input("Please enter the proper "\
                                        "name of a country, or"\
                                        " type 'quit' to end the game."))
            if is_country_check(country_question.lower()) == True :
                country_question = country_question.lower()
                if last_let_first_let_checker\
                            (country_list, country_question):
                    country_list.append(country_question)
                    print(f"That is a valid entry, "\
                          "the list is now:{country_list}")
                    country_question_bool = True
                else:
                    country_question = str(input("I'm sorry that is not a "\
                                                 "valid input. Please input"\
                                                 " a correct country, whose"\
                                                 " first character matches "\
                                                 "that of the last character"\
                                                 " of the prevous country."))
            elif country_question.lower() == "quit":
                quit_bool == True
                rerun()
            else:
                country_question = str(input("I'm sorry that is not"\
                                             " a valid input"\
                                             ". Please input a"\
                                             " correct country."))

def hard_mode() :
    turn_counter_int = 0
    country_list : List = []
    quit_bool = False
    while quit_bool == False:
        turn_counter_int += 1
        print(f"{turn_counter(turn_counter_int)}\n"
              f"The score is currently: {turn_counter_int}.")
        country_question_bool = False
        while country_question_bool == False:
            country_question = str (input("Please enter the proper "\
                                        "name of a country, or"\
                                        " type 'quit' to end the game."))
            if (is_country_check(country_question) == True)\
                    and (len(country_question) > 8):
                country_question = country_question.lower()
                if last_let_first_let_checker\
                            (country_list, country_question):
                    country_list.append(country_question)
                    print(f"That is a valid entry, the"\
                          " list is now:{country_list}")
                    country_question_bool = True
                else:
                    country_question = str(input("I'm sorry that is not a "\
                                                 "valid input. Please input"\
                                                 " a correct country, whose"\
                                                 " first character matches "\
                                                 "that of the last character"\
                                                 " of the prevous country."))
            elif country_question.lower() == "quit":
                quit_bool == True
                rerun()
            else:
                country_question = str(input("I'm sorry that is not a valid"\
                                             " input. Please input a"\
                                             " correct country, that"\
                                             " is longer than eight "\
                                             "characters."))

def main() :
    choose_difficulty()
main()