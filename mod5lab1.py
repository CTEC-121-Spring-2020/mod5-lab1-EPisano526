"""
CTEC 121
Esther Pisano
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""


def main1():
    print("Happy birthday to you!")
    print("Happy birthday to you!")
    print("Happy birthday, dear Fred...")
    print("Happy birthday to you!")
    print()


""" IPO template
Input(s): none
Process: prints/ outputs chorus happy song
Output: prints to terminal screen
"""


def happy():
    print("Happy birthday to you!")


def main2():
    print()
    happy()
    happy()
    print("Happy birthday, dear Fred...")
    happy()
    print()


# generalize for any person
""" IPO template
Input(s): a name
Process: prints/ outputs chorus happy song
Output: prints to terminal screen
"""


def happyBDay(name):
    print("appy birthday, dear ", name, "...", sep="")


def main3():
    print()
    happy()
    happy()
    happyBDay("Esther")
    happy()
    print()


# combine song into a function
""" IPO singhappyBday()
Input(s): a name
Process: prints/ outputs chorus happy song
Output: prints to terminal screen
"""


def singHappyBDay(name):
    happy()
    happy()
    happyBDay(name)
    happy()
    print()


def main4():
    print()
    singHappyBDay("Fred")
    singHappyBDay("Lucy")
    singHappyBDay("Josh")


main4()
