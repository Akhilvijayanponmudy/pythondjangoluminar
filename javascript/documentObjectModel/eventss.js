var clk=document.querySelector("#clk")


clk.addEventListener("click",()=>{
    clk.textContent="Clicked";
    clk.style.color="red";
})





var dbl=document.querySelector("#dbl")


dbl.addEventListener("dblclick",()=>{
    dbl.textContent="double clicked"
    dbl.style.color="red"


})



var ove=document.querySelector("#ove")

ove.addEventListener("mousemover",()=>{
    ove.textContent="mouse over me"
    ove.style.color="yellow"
})


ove.addEventListener("mouseout",()=>{
    ove.textContent="mouse not over me"
    ove.style.color="cyan"
})