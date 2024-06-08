while True:
    user_input = input("Your text: ").strip()
    count_even = 0
    total_characters = len(user_input)

#this is for counting even digits in total and exception to space
    for i in user_input:
        if i.isdigit():
            a = int(i)
            if a % 2 == 0:
                count_even += 1
        if i == " ":
            total_characters -= 1


#this is for auto-printing
    for i in range(0, 10):
        if i % 2 == 0:
            print(f"The number of character '{i}' found:", user_input.count(str(i)))

    print("\nThe number of non-even-digit character in the text:", total_characters - count_even)

    select_continue = input("\nDo you want to continue? yes/no ").lower().strip()
    match select_continue:
        case "yes":
            continue
        case "no":
            quit()
        case _:
            continue
