// var primeNumbers = []
// var nonPrimeNumbers = []

// for (let count = 1; count <= 1000; count++) {
//   if (count == 2 || count == 3 || count == 5 || count == 7 || count == 11) {
//     primeNumbers.push(count)
//   } else if (
//     count % 2 == 0 ||
//     count % 3 == 0 ||
//     count % 5 == 0 ||
//     count % 7 == 0 ||
//     count % 11 == 0
//   ) {
//     nonPrimeNumbers.push(count)
//   } else {
//     primeNumbers.push(count)
//   }
// }

// console.log(primeNumbers)

// var sum = 0
// const sumPrimeNumbers = () => {
//   sum = primeNumbers.reduce((sum, current) => sum + current)
//   console.log('The sum of the prime numbers up to 1000 is', sum)
// }

// sumPrimeNumbers()
var primeNumbers = []
var nonPrimeNumbers = []

for (let count = 1; count <= 1000; count++) {
  if (count == 2 || count == 3 || count == 5 || count == 7 || count == 11) {
    primeNumbers.push(count)
  } else if (
    count % 2 == 0 ||
    count % 3 == 0 ||
    count % 5 == 0 ||
    count % 7 == 0 ||
    count % 11 == 0
  ) {
    nonPrimeNumbers.push(count)
  } else {
    primeNumbers.push(count)
  }
}

console.log(primeNumbers)

const main = () => {
  var sum = 0

  sum = primeNumbers.reduce((sum, current) => sum + current)
  console.log('The sum of the prime numbers up to 1000 is', sum)
}

main()
