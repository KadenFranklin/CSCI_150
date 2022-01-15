from typing import *
from waterjug import Waterjug

def get_waterjugs() -> Dict:
    waterjug_dict: Dict[str, int] = {}
    y = 1
    question0 = input("How many waterjugs would you like?")
    waterjug_dict['total_waterjugs'] = int(question0)


    question1 = input("What do you want the capacity of the first water"\
                      "jug to be? (This will also be the goal waterjug.)")
    waterjug_dict['waterjug_1'] = int(question1)

    goal_amount = int(input("What do you want the goal quantity"\
                            " of water to be?"))
    waterjug_dict['goal_amount'] = int(goal_amount)

    for i in range(int(question0) - 1):
        y += 1
        x = input(f"What do you want the capacity of waterjug # {y} to be?")
        waterjug_dict[f'waterjug_{y}'] = int(x)

    get_solution(waterjug_dict)


def get_solution(waterjug_dict: Dict[str, int]) -> list:
    waterjugs_values_dict: [str, Waterjug] = {}
    y = 1

    for i in range(waterjug_dict['total_waterjugs'] ):
        waterjugs_values_dict[f'waterjug_{y}'] = Waterjug\
            (waterjug_dict[f'waterjug_{y}'], 0)
        y += 1
    solution_list : list = []

    while waterjugs_values_dict['waterjug_1'].contents \
            != waterjug_dict['goal_amount'] :
        print("You may 'Fill' a waterjug, 'Empty' a waterjug, 'Check' "\
              "the contents of a waterjug or 'Pour' from one waterjug "\
              "into another.")
        action = str(input("Please respond with what you would like to do."))

        if action == "Fill":
            action_fill = int(input("Which waterjug would you like to fill?"))
            waterjugs_values_dict[f'waterjug_{action_fill}'].fill()
            solution_list.append(f"fill waterjug # {action_fill}")


        if action == "Empty":
            action_empty = int(input("Which waterjug would you "\
                                     "like to empty?"))
            waterjugs_values_dict[f'waterjug_{action_empty}'].empty()
            solution_list.append(f"empty waterjug # {action_empty}")


        if action == "Check":
            action_check = int(input("Which waterjug would you"\
                                     " like to check?"))
            print(waterjugs_values_dict[f'waterjug_{action_check}'].contents)
            solution_list.append(f"check waterjug # {action_check}")


        if action == "Pour":
            action_pour_from = int(input("Which waterjug would you like"\
                                         " to pour from?"))
            action_pour_to = int(input("Which waterjug would you like "\
                                       "to pour to?"))
            waterjugs_values_dict[f'waterjug_{action_pour_from}'].pour\
                (waterjugs_values_dict[f'waterjug_{action_pour_to}'])
            solution_list.append(f"pour from waterjug # {action_pour_from} "\
                                 "to waterjug # {action_pour_to}")


    if (waterjugs_values_dict['waterjug_1'].contents == waterjug_dict\
            ['goal_amount']) :
        print(f"Solution List:{solution_list}")

def main():
    get_waterjugs()
main()