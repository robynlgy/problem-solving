// Write an algorithm that takes an array and moves all of the zeros to the end,
// preserving the order of the other elements.

// moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]

let array = [false, 1, 0, 1, 2, 0, 1, 3, "a"]

var moveZeros = function (arr) {
    // TODO: Program me
    let arr1 = arr.filter(function (elem) { return elem !== 0 })
    let arr2 = arr.filter(function (elem) { return elem === 0 })
    return arr1.concat(arr2)
}

moveZeros(array)



// Try 1 --- failed

var moveZeros = function (arr) {
    // TODO: Program me
    let arr1 = arr.filter(function (elem) { if (elem === false || elem !== 0) { return elem } })
    console.log(arr)
    let arr2 = arr.filter(function (elem) { if (elem === 0) { return elem } })
    console.log('arr1..', arr1)
    console.log('arr2..', arr2)
    return arr1.concat(arr2)
}

// arr1 : [1, 1, 2, 1, 3, 'a'] <==== missing false
// In the function passed in to the filter, you're not returning a value, you're returning a boolean. 
// which was why since the if statement was trying to return the element itself,
// the function was evaluating based on trusey/falsey values, which was why the false
//  from the array returned as false and was not included in arr1

// arr2: []  <===== should include the zeros
// the if function filters out everything that's not 0 and doesn't get to the return stmt
// the 0s don't get included in arr2, bcz like above the elem is evaluated, instead of a boolean
// and 0s are a falsey value so all the zeros failed the filter and nothing got returned

