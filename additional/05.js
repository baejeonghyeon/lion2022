// 숫자형

let integer = 10; // 10진수
let hex = 0xa; // 16진수
let binary = 0b1010; // 2진수
let octal = 0o12; // 8진수

console.log(integer, hex, binary, octal);

let negative = -10;
let indices = 1.0e1;
let double = 10.12;

console.log(negative, indices, double);

// infinity, NaN
let inf = 10 / 0;
let isNaN = 10 / "영";

console.log(inf, isNaN);

let sum = 0.1 + 0.2;
console.log(sum); // 0.3000...0004
