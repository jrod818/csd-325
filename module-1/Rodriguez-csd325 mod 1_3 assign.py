# Jose Rodriguez
# 06/07/2026
# CSD325 Module 1.3 Assignment
# On the Wall + Flowchart(s)



# This program asks the user for a number and sings and counts down the bottles of beer song.


def countdown(bottles):
    # This function controls the countdown lyrics.
    while bottles > 1:
        print(str(bottles) + " bottles of beer on the wall, " + str(bottles) + " bottles of beer.")
        bottles = bottles - 1

        if bottles == 1:
            print("Take one down, pass it around, 1 bottle of beer on the wall.\n")
        else:
            print("Take one down, pass it around, " + str(bottles) + " bottles of beer on the wall.\n")

    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down, pass it around, 0 bottles of beer on the wall.\n")


def main():
    print("On the Wall Program")
    print("-------------------")

    bottles = int(input("How many bottles of beer are on the wall? "))

    countdown(bottles)

    print("Time to buy more beer!")


main()
