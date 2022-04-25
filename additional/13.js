// return
// 함수를 호출한 부분으로 데이터를 전달해주기 위해 사용하는 예약어

function sum(num1, num2){
  console.log(num1 + num2);
}

sum(10, 20);
//이 경우 sum 함수로 처리된 결과를 알 수 없다.
//하지만 return이 사용되면 값을 보낼 수 있다. (데이터 반환)

function sum2(num1, num2){
  return num1 + num2;
}

const result = sum(10, 20);
//또한 return문 후의 code는 실행이 되지 않는다.
const result2 = sum(20, 30);

const result_sum = result + result2;
console.log(result_sum);
