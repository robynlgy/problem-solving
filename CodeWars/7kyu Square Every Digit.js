// Welcome. In this kata, you are asked to square every digit
// of a number and concatenate them.

// For example, if we run 9119 through the function, 811181 will 
// come out, because 9^2 is 81 and 1^2 is 1.

// Note: The function accepts an integer and returns an integer

function squareDigits(num) {
    let newString = '';
    for (let char of num.toString()) {
        newString += parseInt(char) ** 2;
    }
    return parseInt(newString);
}


//Best solution:
function squareDigits(num) {
    return Number(('' + num).split('').map(function (val) { return val * val; }).join(''));

}