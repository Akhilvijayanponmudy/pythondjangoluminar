console.log(localStorage.getItem("accno"));


class Bank{

static accountDetails(){

    let userData={
1000:{acno:1000,password:"userone",balance:5000},
1001:{acno:1001,password:"usertwo",balance:5000},
1002:{acno:1003,password:"useethree",balance:5000}
    }
    return userData
}

static authanticate(acno,password){
var dataset=Bank.accountDetails()
if(acno in dataset){
    if (password==dataset[acno]["password"]){
        //successfull authentication
        return 1
    } 
    else{
        //invalid password
        return 0
    }
    
    
    {
        
    }

}
else{
    //invalid account number
    return -1
}

}

static setStorage(accno,password){
let obj={
    accno:accno,
    password:password
}
localStorage.setItem("data",JSON.stringify(obj))
}



static login(){
   var accno=document.querySelector("#acno").value
   var password=document.querySelector("#pwd").value
   let user=Bank.authanticate(accno,password) // 0,1 or -1
   if(user==0){
       alert ("invalid password")


   }
   else if(user==1){
       Bank.setStorage(accno,password)
       window.location.href="home.html"
   }
   else if(user==-1){
       alert("invalid account")

   }
}
static withdrawal(){

}

static deposit(){
    var data=Bank.accountDetails()
var accno=document.querySelector("#acno").value
var password=document.querySelector("#pwd").value
var amount=document.querySelector("#amt").value
let user=Bank.authanticate(accno,password)
if(user==0){
    alert ("invalid password")


}
else if(user==1){
    alert("successfully deposited")
}
else if(user==-1){
    alert("invalid account")

}
}




}



