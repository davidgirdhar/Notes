## ES6 Array functions



`map()` : function creates a new array by doing something with each element of in an array.
for example:
```javascript
function square(a){
    return a*a;
}
let numbers = [1,4,5,7];
let newNumbers = numbers.map(square);
console.log(newNumbers) 
`[ 1, 16, 25, 49 ]`
```
---
Can pass any function you want to perform.
Same as map can be done using forEach()

```javascript
let newNumbers = []
numbers.forEach(function(a){
    newNumbers.push(square(a))
})

console.log(newNumbers);
`[ 1, 16, 25, 49 ]`
```
---

`filters()`: Create a new array by keeping that items only which satisfy given condition.
```javascript
let newNumbers = numbers.filter(function(num){
    return num>=5
})
`[ 5, 7 ]`
```
---

`reduce()`: Accumulate a value by doing something to each item in an array.Function in the reduce takes two parameter one is total value(accumulator) while latter one is item of an array.
```javascript
let numbers = [1,4,5,7];
let newNumber = numbers.reduce(function(accumulator,currnumber){
    return accumulator + currnumber;
})
console.log(newNumber);
`17`
```

`find()` : Find the first item that matches from the array
```javascript
let numbers = [1,4,5,7];
let newNumber = numbers.find(function(x){
    return x%2 == 0;
})
console.log(newNumber);
`4`
```
Now very similar to  `find()` is `findindex()` but there is slight difference which you have understood by the name only that it return index of the first number satifsy condition.

Now You don't have to memorize these functions, just understand it as aftersome time as you would encounter some problems you would remember that there is some function which will help me out. And make your task simpler.
You can also visit [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array).It's one the best site you can take reference related javascript concepts apart from my notes XD.








