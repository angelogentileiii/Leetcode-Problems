# As far as I'm aware there is not a leetcode problem that requires this solution but it was something I saw online and wanted to work on a solution as well


def textToNumber(string: str) -> int:
    numberVals: dict[str, int] = {
        "a": 1,  # Handle 'a' as a shortcut for 'one'
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
    }

    multipliers: dict[str, int] = {
        "hundred": 100,
        "thousand": 1000,
        "million": 1000000,
        "billion": 1000000000,
        "trillion": 1000000000000,
    }

    string = string.replace("-", " ").replace(" and", "").lower().strip()

    words = string.split(" ")
    print(f"Words: {words} \n")

    current = 0
    result = 0

    for word in words:
        if word in numberVals:
            current += numberVals[word]

            print(f"Current Val: {current}")
        elif word in multipliers:
            if current == 0:
                current = 1

            current *= multipliers[word]

            print(f"Current Val in Multiplier: {current}")

            if multipliers[word] >= 1000:
                result += current
                current = 0

                print(f"Update Result: {result}")
        else:
            pass

    result += current
    print(f"\nResult: {result}")
    print("-" * 35, "\n")

    return result


textToNumber("one hundred million six thousand and three")
textToNumber("two-thousand six hundred and five")
textToNumber("a hundred thousand and seventeen")
textToNumber(
    "seven trillion thirty-five million six hundred and seventeen thousand forty-eight"
)
