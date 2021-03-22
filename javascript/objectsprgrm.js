var employee={
    id:1000,name:"ajay",desig:"developer",salary:25000
}

console.log(employee["name"]);
console.log(employee.name);



//checking for gender
console.log("gender" in employee);

//add gender male

employee["gender"]="male"

console.log(employee);


for( let key in employee){
    console.log(key);
}




