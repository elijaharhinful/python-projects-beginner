# initiate start value
start = 1

while start < 10:
    first_noun = input("Enter a noun: ")
    p_noun = input("Enter a plural noun: ")

    second_noun = input("Enter a second noun: ")
    place = input("Name a place: ")
    adjective = input("Enter an adjective: ")

    third_noun = input("Enter a third noun: ")

    # Print results
    print("*" * 35)
    print("Be kind to your", first_noun, "-footed", p_noun)
    print("For a duck maybe somebody's", second_noun, ",")
    print("Where the weather is always", adjective, ".")
    print()
    print("You may think that is the", third_noun, ".")
    print("Well it is.")
    print("*" * 35)

    # increase start value by one
    start = + 1
