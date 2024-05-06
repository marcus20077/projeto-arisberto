const l1 = 6
const l2 = 4
const l3 = 8

if (l1 === l2 & l1 === l3 & l2 === l3){
console.log ("Triangulo equilátero");
} else if (l1 === l2 || l1 === l3 || l2 === l3){
console.log ("triangulo isóscele");
} else {
    console.log ("triangulo escaleno");
}
