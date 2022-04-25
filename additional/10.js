// object {}

let obj = {};

// let obj2 = {key: value};

let student1 = {
  koreanScore: 90,
  englishScore: 70,
  mathScore: 80,
  scienceScore: 60
};
// object 뒤에는 ;생략하는 경향 있지만, 찍어주는게 좋음

console.log(student1["koreanScore"]);
console.log(student1.englishScore);

//주의 점 연산자를 이용할 때는 key를 문자열로 하지 않는다.
//key 자체는 문자열로 정의해도 됨. 이 경우 띄어쓰기 가능.