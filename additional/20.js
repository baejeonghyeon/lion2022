/* 스위치 조건문 */


switch(key){
  case value1:

    break;
  case value2:

    break;
  default:

    break;
}

let animal = 'Dog';

switch (animal){
  case 'Cat':
    console.log('야옹');
    break;
  case 'Dog':
    console.log('멍멍');
    break;
  default:
    console.log('일치하는 동물 소리 없음');
    break;
};

/* 브레이크 문이 없으면 일치하는 케이스 위에 있는 것은 다 실행 */
/* 쉽게 말해 기본적으로, 일치하는 케이스까지 다 실행한다는 것 */