// let name = "Brian";
// age = 28;
// console.log(name + age)

// console.log(name + age)

// //string method
// let message = "hahahah";

// message.toUpperCase();
// message.toLocaleLowerCase();

// let anothermessage = "      lol    ";
// anothermessage.trim().toUpperCase();

// //Length of the string
// // Attributes
// let firstName = "Thomas";
// console.log(firstName.length);

// //Methods with arguments
// let movie = "Game of Thrones";
// console.log(movie.indexOf("Game"));
// console.log(movie.indexOf("Knight"));


// //Replace Method
// let greetings = "Hello my name is Jennie";
// greetings = greetings.replace("Jennie", "Laney");
// console.log(greetings);


// //slicing our strings
// let song = "I found the love, beautiful and sweet";
// let word = song.slice(12, 16);
// console.log(word);


// let example = "This country is Switzerland, and it is beautiful";
// let exword = example.slice(16, 27);
// console.log(exword);


// let language = "Javascript";

// practicing replace and slice
// let play = "skateboard"
// board = play.slice(5);
// beard=board.replace ("o", "e")
// console.log(beard)


//string template literals
// let age = 21;
// let name = "Johnny";
// let hobby = "playing basketball";
// // console.log(`${name} is ${age} and like ${hobby}`);

// let productName = "apple";
// let productPrice = 2.5;
// let productQuantity = 3;
// console.log(`Hello ${name}, the total price of ${productQuantity} ${productName}s is ${productPrice * productQuantity}`);

let userAge = parseInt(prompt("How old are you?"));
let name = prompt("What is your name?");
let newAge = userAge + 10;
console.log(`Hello ${name}! In 10 years you will be ${newAge}!`);
