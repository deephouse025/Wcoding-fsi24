

// let word = "I like apples. Because apples are so delicious.";
// console.log(word.indexOf("apples", 8))
// console.log(word[23])

// console.log(word.slice(14))


// console.log(1 == "1") // true -> true
// console.log(1 === "1") // true && false -> false



let credit = parseInt(prompt("Please enter credit score:"));

if (credit >= 300 && credit <580){
    console.log(`Credit score of: ${credit} is classified as Poor!`)
} else if (credit >=580 && credit <670){
    console.log(`Credit score of: ${credit} is classified as Fair!`)
} else if (credit >=670 && credit <740){
    console.log(`Credit score of: ${credit} is classified as Good!`)
} else if (credit >=740 && credit <800){
    console.log(`Credit score of: ${credit} is classified as Very Good!`)
} else if (credit >=800 && credit <=850){
    console.log(`Credit score of: ${credit} is classified as Excellent!`)
} else {
    console.log("Please intput a valid credit score !!")
}
