// function

// 함수 선언식
// function [함수명](){
//   'code'
// };

// 함수 표현식
// const [변수명] = function [함수명](){
//   'code'
// };

function gugudan(){
  console.log("3 * 1 = 3")
};

gugudan();

const gugudan22 = function gugudan(){
  console.log("3 * 1 = 3")
};
// 보통 const를 사용. 중복성 제거때문에.

gugudan22();
// 함수 표현식은 변수의 이름이 중요하다.

//익명 함수
const gugudan33 = function(){
  console.log("3 * 1 = 3")
};
gugudan33();
