// // //object literals

// //     const fitBitData = {
// //         totalSteps: 308123,
// //         totalMiles: 234234,
// //         "key": "value",
// //         "key": "value"

// //     }



// //     const studentData = {
// //         name: "Toby Green",
// //         age: 25,
// //         nationality: "America",
// //         subjects: ["Maths", "Science", "English"],

// //     }

// //     console.log(studentData.name);
// //     //or
// //     console.log(studentData["name"]);



// //     //printing type of object
// //     console.log(typeof studentData);

    


// //testing

// const house = {
//     doors: "wood",
//     windows: "glass",
//     refrigerator: {
//         outerShell: "metal",
//         insulatingLayer: "plastic",
//         refrigerant: {
//             chemicals: ["carbon", "oxygen", "nitrogen"],
//             method: "compression"
//         }
//     }
// }

// //printing the window material
// console.log()

// //printing the outershell material

// //printing the last chemical in the refrigerant

// // adding a new key and value
// house.big = true;
// house["doors"] = "metal";
// console.log(house);


// const customer = {
//     age: 23,
//     budget: 20000,
//     language: "english",
//     location: "florida",
// }

// customer.age = 24;
// customer.preferance = "boat";
// customer.address = "10-bigstreet";



//for loop

// for (let i = 1; i <=10; i++){
//     sum+= i;
//     console.log(sum);
// }

const number = [];

for (let i = 1; i <=50; i++){
    if(i % 3 === 0 && i % 5 === 0){
        number.push("fizzbuzz");
    } else if (i % 3 === 0){
        number.push("fizz");
    } else if (i % 5 === 0){
        number.push("buzz");
    } else{
        number.push(i);
    }
        

}
console.log(number);