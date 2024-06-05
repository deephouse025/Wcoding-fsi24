// let weather = prompt("What is the weather like today?");
// if(weather == "sunny"){
//     console.log("It is nice out");
// } else if (weather == "cloudy"){
//     console.log("Grab your umbrella");
// } else if (weather == "windy"){
//     console.log("Hold onto your hat!");
// } else{
//     console.log("Please input a valid weather condition")
// }


// let input = parseInt(prompt("Give a number!"));
// if (input % 2 === 0) {
//     console.log("even");
// } else {
//     console.log("odd");
// }

// let input = parseInt(prompt("What is the number?"))
// if(input % 3 === 0 && input % 5 === 0){
//     console.log("FizzBuzz");
// } else if(input % 3 === 0){
//     console.log("Fizz");
// } else if(input % 5 === 0){
//     console.log("Buzz");
// } else{
//     console.log(input);
// }

// let rain = prompt("Is it raining? (Yes/No)")

// if (rain === "yes"){
//     let umbrella = prompt("Do you have umbrella? (Yes/No)");
//     if (umbrella == "yes"){
//         console.log("You can go outside");
//     }else{
//         console.log("Wait a while");
//     }

// }else{
//     console.log("You can go outside!");
// }



let weight = parseInt(prompt("What is your weight? (kg)"))

let height = parseInt(prompt("What is your height? (m)"))

let BMI = weight / (height * height);

// let BMI = parseInt(prompt("Enter bmi"));

if (BMI < 18.5){
    console.log(`Your BMI: ${BMI} is classified as Underweight`);
} else if(BMI > 18.5 && BMI < 25){
    console.log(`Your BMI: ${BMI} is classified as Normal`);
} else if(BMI >= 25 && BMI < 30){
    console.log(`Your BMI: ${BMI} is classified as Slightly Overweight`);
} else if(BMI >= 30 && BMI < 35){
    console.log(`Your BMI: ${BMI} is classified as Obese`);
} else if(BMI >= 35){
    console.log(`Your BMI: ${BMI} is classified as Clinically Obese`);
}else{
    console.log("Enter a valid number");
}