/* 함수 선언식 */
function sum(num1, num2){
  return num1 + num2;
};

/* 함수 표현식 */
const sum = function sum(num1, num2){
  return num1 + num2;
};

/* 화살표 함수 
특징. 화살표 함수의 내용에서 중괄호 안에 바로 return을 사용한다면
간단하게 줄일 수 있다.
ex 가장 겉에 있는 괄호 지우기.*/
const sum = (num1, num2) => num1 + num2;
/*또한 변수가 하나면 소괄호를 생각할 수도 있다.
전달할 매개 변수가 없으면 ()만 해도 된다.*/
const sum = x => x * x;

const sum = (num1, num2) => {
  return num1 + num2;
};

const result = sum(10, 20);
console.log(result);

/* 내부적으로 객체를 반환하고 있다면? 객체를 소괄호로 한 번 감싸야 함*/
const getObject = () =>
  ({
    name: "철수",
    age: 20
  });