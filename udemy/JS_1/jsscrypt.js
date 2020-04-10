// alert("Welcome to Bank");
// var deposit = prompt("Whow much would you deposit today?");
// alert("You've deposited: " + deposit);
// console.log("Some text for console.");

var students = [];
main();


function add(){
  name = prompt("Enter name to add ");
  students.push(name);
}

function display(){
  console.log(students);
}

function remove()
{
  name = prompt("Enter name to remove ");
  students.pop(name);
}

function main()
{
  var input = "quit";
  while(true){
    input = prompt("Select: add, display, remove, quit")
    if(input == "quit"){
      break;
    }
    if(input == "add"){
      add();
    }
    if(input == "display"){
      display();
    }
    if(input == "remove"){
      remove();
    }
  }
}
