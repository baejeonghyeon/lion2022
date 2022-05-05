/* 템플릿 문자열 */
/* 백틱과 기존 문자열의 차이점
1. 큰따옴표나 작은따옴표가 포함된 문장 있으면 도움
*/

let str1 = `'시작이 반이다'`;
console.log(str1);

let str2 = `"시작이 반이다"`;
console.log(str2);

let str3 = `"여러분, '시작이 반이다'라는 말 들어보셨죠?"`
console.log(str3)


/* 이스케이프 문자열을 사용할 수도 있음 */
let str4 = "\"여러분, '시작이 반이다'라는 말 들어보셨죠?\""
console.log(str4)


/* 템플릿 문자열은 변수에 속해져 있는 값을
대입하여 문자열 값을 만들 수 있음 */
let name1 = '철수';
let name2 = '영희';

let string = `${name1}은 ${name2}를 좋아합니다.`;
console.log(string);
