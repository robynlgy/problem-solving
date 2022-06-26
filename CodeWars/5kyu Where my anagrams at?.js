// What is an anagram ? Well, two words are anagrams of each other if they both contain the 
// same letters.For example:

// 'abba' & 'baab' == true

// 'abba' & 'bbaa' == true

// 'abba' & 'abbba' == false

// 'abba' & 'abca' == false

// Write a function that will find all the anagrams of a word from a list.You will be
// given two inputs a word and an array with words.You should return an array of all
// the anagrams or an empty array if there are none.For example:

// anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

// anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

// anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

// ======= BROKEN KATA ==========


function anagrams(word, words) {
    let anagramsArr = [];
    let sortedWord = word.split('').sort(compare).join('')
    for (let elem of words) {
        if (word.length !== elem.length) { continue };
        let sortedElem = elem.split('').sort(compare).join('');
        if (sortedElem === sortedWord) {
            anagramsArr.push(elem)
        }
    }
    return anagramsArr;
}

// to compare strings
function compare(a, b) {
    if (a < b) { return -1 };
    if (b > a) { return 1 };
    return 0;
}

