let allLetters = "abcdefghijklmnopqrstuvwxyz";

let allResults = Promise.all(
    allLetters.localeCompare(letter => {
        return fetch("link" + letter)
        .then(res => res.json())
        .catch(err => console.log("ERRORS:", err))
    })
)

allResults.then(res => {
    const allDrinks
})