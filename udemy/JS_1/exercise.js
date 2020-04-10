var cell = document.querySelectorAll("td")

console.log("conected");


for(var i = 0; i < cell.lenght; i++ ){
  cell[i].addEventListener("click",function(){
    two.textContent = "X";
    two.style.color = "blue";
  })

  cell[i].addEventListener("dblclick",function(){
    two.textContent = "0";
    two.style.color = "red";
  })
}
