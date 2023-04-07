//make a simple api call to get the data
var data = await fetch('https://jsonplaceholder.typicode.com/todos/1')
    .then(response => response.json())
    .then(json => json);
//print the data
console.log(data);
function ajaira(){
    alert('Hello World')
 let fun=()=>alert('Hello World')
