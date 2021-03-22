class Parent{
    m1(){
        console.log("inside parent class");
    }
}


class Child extends Parent{
    m2(){
        console.log("inside child class");
    }
}

class Subchild extends Child{
    m3(){
        console.log("inside subchild");
    }
}



var subchild=new Subchild()
subchild.m2()
subchild.m1()
subchild.m3()

