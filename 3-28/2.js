let bill = 0;

console.log("Welcome to JS Pool!");

let userInput = prompt("Would you like to use our swimming pool services? (Yes/No)");
if (userInput == "yes"){
    let age = Number(prompt("Great, How old are you?"))
    if (age <= 12 && age > 6){
        let members = Number(prompt("How many are in your party? (1-9)"));
        bill += 5 * members
        let suit = prompt("Do you want to rent a swimming suit?")
        if (suit === "yes"){
            bill += 3;
        }
        let photos = prompt("Do you want to take a picture?")
        if (photos === "Yes"){
            bill += 3;
        }
    } else if (age >= 13 && age <= 19){
        let members = Number(prompt("How many are in your party? (1-9)"));
        bill += 8 * members
        let suit = prompt("Do you want to rent a swimming suit?")
        if (suit === "yes"){
            bill += 3;
        }
        let photos = prompt("Do you want to take a picture?")
        if (photos === "Yes"){
            bill += 3;
        }
    } else if (age >= 20 && age <= 28){
        let members = Number(prompt("How many are in your party? (1-9)"));
        bill += 12 * members
        let suit = prompt("Do you want to rent a swimming suit?")
        if (suit === "yes"){
            bill += 3;
        }
        let photos = prompt("Do you want to take a picture?")
        if (photos === "Yes"){
            bill += 3;
        }
    } else {
        console.log("Sorry the pool is only for under 29 yrs");
    }
   
} else {
    console.log("Thanks anyway!");
}
console.log(`Your total is ${bill} !`);