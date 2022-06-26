function solution(number) {
    let largestThree = 0
    let largestFive = 0
    if (number % 3 !== 0) {
        largestThree = parseInt(number / 3)
    } else {
        largestThree = number / 3 - 1
    };
    if (number % 5 !== 0) {
        largestFive = parseInt(number / 5)
    } else {
        largestFive = number / 5 - 1
    }
    let totalSum = 0;
    for (i = 1; i <= largestThree; i++) {
        totalSum += 3 * i;
    };
    for (i = 1; i <= largestFive; i++) {
        if (5 * i % 3 !== 0) {
            totalSum += 5 * i;
        }
    };
    if (totalSum >= 0) {
        return totalSum;
    }
    return 0;

}


// what the fuck
function solution(number) {
    let sum = 0;
    for (let i = 3; i < number; i++) {
        if (i % 3 === 0 || i % 5 === 0) {
            sum += i
        }
    }
    if (sum < 0) {
        return -1
    }
    return sum
}