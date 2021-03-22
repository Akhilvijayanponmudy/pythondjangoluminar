// arrays

var data=[10,"hello",true,10.5];
console.log(data);


var numbers=[10,20,30,40,50]

//for(let i=0; i<numbers.length;i++){
//    console.log(numbers[i])
//}

for(let number of numbers){
    console.log(number);
}


numbers.push(100)
console.log(numbers);


numbers.pop()
console.log(numbers);