class Person{
    setPerson(age,name){
        this.age=age;
        this.name=name;
    }
    printPerson(){
        console.log(this.age+ "," +this.name);
    }
}


var obj=new Person();
obj.setPerson(25,"ajay")
obj.printPerson()
///////////////////////////////////////////////////////////


class Student{
    constructor(name,clas,age){
        this.name=name;
        this.clas=clas;
        this.age=age;
    }
    printStudent(){
        console.log(this.name+ "," +this.clas +"," +this.age);
    }
}

var obj=new Student("akhil","django",24);
obj.printStudent()















