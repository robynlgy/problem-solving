// ROT13 is a simple letter substitution cipher that replaces a letter with the
// letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

// Create a function that takes a string and returns the string ciphered with Rot13.
//  If there are numbers or special characters included in the string, they should be 
// returned as they are. Only letters from the latin/english alphabet should be shifted, 
// like in the original Rot13 "implementation".


let test = 'aAaAzZ! !^&*~'

function rot13(message) {
    return message.split('').map(function (char) {
        let charCode = char.charCodeAt(0);
        let rot13Code = charCode + 13;
        // if orig and ciphered is a valid letter       -- instead of having numbers, could define var that represents what they are instead eg, codeA = 'A'.charCodeAt(0)
        if ((charCode > 64 && charCode < 91 && rot13Code > 64 && rot13Code < 91)
            || (charCode > 96 && charCode < 123 && rot13Code > 96 && rot13Code < 123)) {
            return String.fromCharCode(rot13Code);
        }
        // if orig is a valid letter but ciphered isnt;
        // this section could've been included above as ((code - codeA) + 13) % 26 + codeA ---- see below
        else if ((charCode > 64 && charCode < 91) || (charCode > 96 && charCode < 123)) {
            return String.fromCharCode(rot13Code - 26);
        }
        // orig is not a valid letter
        else {
            return char;
        }
    }).join('')
}



// ???????????
//https://www.codewars.com/kata/530e15517bc88ac656000716/solutions/javascript
//
// Explanation for ((code - codeA) + 13) % 26 + codeA from user kgroat
// 
//The idea with this section:

// ((code - codeA) + 13) % 26 + codeA

// is that we take the character code (say for a V, the code would be 86) and subract the character code for A, which is 65. This simplifies the first bit down to:

// ((21) + 13) % 26 + codeA

// We do this to determine the letter's position in the alphabet. V is the 22nd letter (indexed from zero, that's 21). We then add 13, as the challenge asks, to get:

// (34) % 26 + codeA

// The problem here is that there is no 34th letter -- we have to make sure it wraps around to the start of the alphabet if we go too far, so we take the number, and use modulo 26 (taking the remainder if we were to divide by 26) since there are only 26 letters in the alphabet. This gives us:

// 8 + codeA

// Here, we are left with the 9th letter (8, indexed from zero), which is I. However, the character code for I is 73, so in order to get back to the correct code, we have to add back the char code for A, or 65. This now simplifies as so:

// 8 + 65 -> 73