var countDeafRats = function (town) {
    // Your code here
    let count = 0;
    let crowded = town.split('').filter(function (val) { return val != " " }).join('')
    let piper = crowded.indexOf("P")
    //before piper
    for (let i = 0; i < piper; i += 2) {
        if ((crowded[i] + crowded[i + 1]) === 'O~') {
            count++;
        }
    }
    //after piper
    for (let j = piper + 1; j < crowded.length; j += 2) {
        if ((crowded[j] + crowded[j + 1]) === '~O') {
            count++;
        }
    }
    return count;
}


let town = '~O~O~O~O P'             // 0
countDeafRats(town)
let town2 = 'P O~ O~ ~O O~'         // 1
countDeafRats(town2)
let town3 = '~O~O~O~OP~O~OO~'       // 2
countDeafRats(town3)
let town4 = 'O~~O~OO~   PO~~OO~'    // 3
countDeafRats(town4)