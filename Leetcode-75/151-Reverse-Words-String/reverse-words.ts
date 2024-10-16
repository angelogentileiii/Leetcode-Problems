// PROBLEM #151 - REVERSE WORDS IN A STRING

// Given an input string s, reverse the order of the words.

// A word is defined as a sequence of non-space characters.
// The words in s will be separated by at least one space.

// Return a string of the words in reverse order concatenated by a single space.
// Note that s may contain leading or trailing spaces or multiple spaces between two words.
// The returned string should only have a single space separating the words.
// Do not include any extra spaces. --> Strip additional whitespace from beginning and end of input

//---------------------------------------------------------------------------------------------------------------------------

function reverseWords(s: string): string {
    const words = s.trim().split(" "); // In JS and TS, we must first trim the leading and trailing whitepace and then split
    const noSpaces = words.filter((word) => word.length > 0); // Filter out any empty strings from the split --> Individual spaces become strings with length zero

    console.log(words);
    console.log(noSpaces);

    // Two pointers for string reversal --> Could use reverse method as well
    let i = 0;
    let j = noSpaces.length - 1;

    // Reversal of array elements --> Move words into proper positioning
    while (i < j) {
        [noSpaces[i], noSpaces[j]] = [noSpaces[j], noSpaces[i]];
        i++;
        j--;
    }

    console.log(noSpaces.join(" "));

    // Join the elements of the array by singular spaces and return
    return noSpaces.join(" ");
}

reverseWords("      hello    world     ");
reverseWords("Angelo   is  name   My");
