
let total = 0;
let size = prompt("What size would you like? (S/M/L)");
if (size === "S"){
    total += 15;
    let pep = prompt("Add Pepperoni? (Y/N)");
    if (pep === "Y"){
        total += 2;
    }
    let cheese = prompt("Add Cheese? (Y/N)");
    if (cheese === "Y"){
        total += 1;
    }
} else if (size === "M"){
    total += 20;
    let pep = prompt("Add Pepperoni? (Y/N)");
    if (pep === "Y"){
        total += 3;
    }
    let cheese = prompt("Add Cheese? (Y/N)");
    if (cheese = "Y"){
        total += 1;
    }
} else if (size === "L"){
    total += 25;
    let pep = prompt("Add Pepperoni? (Y/N)");
    if (pep === "Y"){
        total += 3;
    }
    let cheese = prompt("Add Cheese? (Y/N)");
    if (cheese === "Y"){
        total += 1;
    }
}
console.log(`Thank you for choosing Js Pizza! You final bill is ${total}`);