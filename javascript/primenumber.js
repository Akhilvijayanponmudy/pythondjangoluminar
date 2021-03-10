var number=17

var flag=0
//2,16
for(let i=2;i<number;i++){
if(number%i==0){
    flag+=1;
    break
}
else{
    flag=0}
}
if(flag==0){
    console.log("Prime");
}
else{
    console.log("Not Prime");
}