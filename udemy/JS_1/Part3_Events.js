var one = document.querySelector("#one")
var two = document.querySelector("#two")
var three = document.querySelector("#three")

console.log("Connected!")

one.addEventListener("mouseover",function(){
  one.textContent = "Mouse Over me!";
  one.style.color = "red";
})

one.addEventListener("mouseout",function(){
  one.textContent = "Hover Over me!";
  one.style.color = "black";
})

two.addEventListener("click",function(){
  two.textContent = "I was clicked!";
  two.style.color = "blue";
})

three.addEventListener("dblclick",function(){
  three.textContent = "I was double clicked!";
  three.style.color = "red";
})
