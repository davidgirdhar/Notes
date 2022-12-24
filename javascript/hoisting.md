## Hoisting

Now what does hoisting mean it means to to pull or lift something up.Now that similar scenario in javascript,
here variables and functions are hoisted, which pulled up to the top of the file or function, so rather than being available after their declaration, they might actually be available beforehand.
Now let have a look of it by example.

### Variable Hoisting

```javascript
console.log(variable);
```
`ReferenceError: variable is not defined`

Now this one everyone knows for sure. An error is thrown when you try to access the value of a variable that doesn't exist.

```javascript
// output: undefined
console.log(variable);


var variable = "Now it's defined!";

// Outputs: "Now it's defined!"
console.log(variable);
```

Now here while printing out `variable` before declaring we are not getting reference error that it is not defined.
so what's actually happening here.Now as I told you before variables and functions are hoisted in javascript.Basically, the JavaScript interpreter "looks ahead" to find all the variable declarations and "hoists" them to the top of the function. Which means that the example above is equivalent to this:

```javascript

var variable;

// Outputs: undefined
console.log(variable);

variable = "Now it's defined!";

// Outputs: "Now it's defined!"
console.log(variable);

```

This hoisting happens only on variables which are of type `var` only.Have a at look below example.

```javascript
console.log(variable);

let variable = "Now it's defined!";

console.log(variable);
```
`output: ReferenceError: Cannot access 'variable' before initialization`

Now what about function hoisting, well function hoisting is handled differently in javascript.Unlike variables, a function declaration doesn't just hoist the function's name. It also hoists the actual function definition.Have take a look

``` javascript

// output: hello World
print();

function print(){
    console.log("hello World");
}
```
Here we can see javascript enable us to use before it's been declared.
However, function definition hoisting only occurs for function declarations, not function expressions. For example:

``` javascript
// Outputs: "Definition hoisted!"
print();

notPrint();

function print() {
    console.log("Definition hoisted!");
}

var notPrint = function () {
    console.log("Definition not hoisted!");
};
```

`TypeError: notPrint is not a function`


In function expression actual function is a value assigned to a named variable.So this named variable is hoisted.Even if you have a named function assigned, it still will not be hoisted as it is not a declaration and will be created later.



















