let randomNumber = Math.random();
randomNumber = Math.floor(randomNumber * 6) + 1;
let userAnswer = parseInt(prompt("Take a guess!"));
if (userAnswer === randomNumber){
    console.log("Great Guess!");
} else{
    console.log("Wrong!");
}