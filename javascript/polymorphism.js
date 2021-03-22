class Calc{
    add(){
        console.log("inside no argument method");
    }
    add(num){
        console.log("inside one argument");
    }
    add(mum1,num2){
        console.log("inside two argumenent");
    }
}

var cal= new Calc()
cal.add(10)
cal.add(10,20)

//only recently added method will works