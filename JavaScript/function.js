/* 
* 
* Q1: Write JavaScript to store and retrieve a JSON file on your local 
* storage with the following information:
* 
* Name: John Doe
* Age: 35
* City: Collingwood
* 
*/

// person object
var person = { 'Name': 'John Doe', 'Age': 35, 'City': 'Collingwood' };

// assuming we're storing on browser local storage
localStorage.setItem('person', JSON.stringify(person));

// retreiving person object from local storage
var LocalPerson = localStorage.getItem('person');

// printing to console that I have done the task
console.log('Stored Data: ', JSON.parse(LocalPerson));