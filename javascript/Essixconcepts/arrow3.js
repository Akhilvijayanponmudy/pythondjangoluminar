var arr=[10,20,30,40,11,12,13,41,42,43]




arr.filter(num=>num%2==0).forEach(num=>console.log(num))

arr.sort((no1,no2)=>no1-no2).forEach(num=>console.log("sorted" +num))



arr.sort((num1,num2)=>num1>num2?-1:1).forEach(num=>console.log(num))


let num=arr.reduce((num1,num2)=>num1+num2)
console.log(num);





let min=arr.reduce((num1,num2)=>num1>num2?num2:num1)
console.log(min);
