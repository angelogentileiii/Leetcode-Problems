// As far as I'm aware there is not a leetcode problem that requires this solution but it was something I saw online and wanted to work on a solution as well

function textToNumber(str: string): number {
    const numberVals: { [key: string]: number } = {
        a: 1,
        one: 1,
        two: 2,
        three: 3,
        four: 4,
        five: 5,
        six: 6,
        seven: 7,
        eight: 8,
        nine: 9,
        ten: 10,
        eleven: 11,
        twelve: 12,
        thirteen: 13,
        fourteen: 14,
        fifteen: 15,
        sixteen: 16,
        seventeen: 17,
        eighteen: 18,
        nineteen: 19,
        twenty: 20,
        thirty: 30,
        forty: 40,
        fifty: 50,
        sixty: 60,
        seventy: 70,
        eighty: 80,
        ninety: 90,
    };

    const multipliers: { [key: string]: number } = {
        hundred: 100,
        thousand: 1000,
        million: 1000000,
        billion: 1000000000,
        trillion: 1000000000000,
    };

    const numbers = str
        .replace(/\band/g, "")
        .replace(/-/g, " ")
        .split(" ")
        .filter(Boolean);

    console.log(numbers, "\n");

    let current = 0;
    let result = 0;

    for (const word of numbers) {
        if (numberVals[word] != undefined) {
            current += numberVals[word];

            console.log("Current Val: ", current);
        } else if (multipliers[word] != undefined) {
            if (current === 0) {
                current = 1;
            }
            current *= multipliers[word];

            console.log("Current Val in Multiplier: ", current);

            if (multipliers[word] >= 1000) {
                result += current;
                current = 0;

                console.log("Updated Result: ", result);
            }
        } else {
            throw new Error(`Unknown word: ${word}`);
        }
    }
    result += current;
    console.log("\nResult:", result);
    console.log("-".repeat(35), "\n");

    return result;
}

textToNumber("one hundred million six thousand and three");
textToNumber("two-thousand six hundred and five");
textToNumber("a hundred thousand and seventeen");
textToNumber(
    "seven trillion thirty-five million six hundred and seventeen thousand forty-eight"
);
