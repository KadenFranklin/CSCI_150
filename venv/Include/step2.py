from typing import *
from waterjug import Waterjug

def get_waterjugs() -> Dict:
    waterjug_dict: Dict[str, int] = {}

    question1 = input("What do you want the capacity of the"\
                      " first waterjug to be? (This will also"\
                      " be the goal waterjug.)")
    waterjug_dict['waterjug_1'] = int(question1)

    question2 = int(input("What do you want the capacity "\
                          "of the second waterjug to be?"))
    waterjug_dict['waterjug_2'] = int(question2)

    goal_amount = int(input("What do you want the goal "\
                            "quantity of water to be?"))
    waterjug_dict['goal_amount'] = int(goal_amount)

    get_solution(waterjug_dict)


def get_solution(waterjug_dict: Dict[str, int]) -> list:
    waterjug_1 = Waterjug(waterjug_dict['waterjug_1'], 0)
    waterjug_2 = Waterjug(waterjug_dict['waterjug_2'], 0)
    solution_list : list = []

    while waterjug_1.contents != waterjug_dict['goal_amount'] :
        print("You may 'Fill' a waterjug, 'Empty' a waterjug, 'Check' the "\
              "contents of a waterjug or 'Pour' from one"\
              " waterjug into another.")
        action = str(input("Please respond with what you would like to do."))

        if action == "Fill":
            action_fill = int(input("Which waterjug would you"\
                                    " like to fill 1 or 2?"))
            if action_fill == 1:
                waterjug_1.fill()
                solution_list.append("fill waterjug 1")
            if action_fill == 2:
                waterjug_2.fill()
                solution_list.append("fill waterjug 2")

        if action == "Empty":
            action_empty = int(input("Which waterjug would you"\
                                     " like to empty '1' or '2'?"))
            if action_empty == 1:
                waterjug_1.empty()
                solution_list.append("empty waterjug 1")
            if action_empty == 2:
                waterjug_2.empty()
                solution_list.append("empty waterjug 2")

        if action == "Check":
            action_check = int(input("Which waterjug would"\
                                     " you like to "\
                                     "check '1' or '2'?"))
            if action_check == 1:
                print(waterjug_1.contents)
                solution_list.append("check waterjug 1")
            if action_check == 2:
                print(waterjug_2.contents)
                solution_list.append("check waterjug 2")

        if action == "Pour":
            action_pour = int(input("Which waterjug would you like"\
                                    " to pour from '1' or '2'?"))
            if action_pour == 1:
                waterjug_1.pour(waterjug_2)
                solution_list.append("pour from waterjug 1")
            if action_pour == 2:
                waterjug_2.pour(waterjug_1)
                solution_list.append("pour from waterjug 2")

    if (waterjug_1.contents == waterjug_dict['goal_amount']) :
        print(solution_list)

def main():
    get_waterjugs()
main()