
### DESTRUCTURING 

Some time when working with array or object, we just need some elements out of them.
So it won't be good practice to fetch that element by their index every time.

So, Destructuring is basically assinging values of array or object to variable.

```javascript
const vehicles = ['mustang', 'f-150', 'expedition'];

const [car, truck, suv] = vehicles;
```
or 

```javascript
const food = ["eggs", "curd","sweetcorn","cake"];

let [egg, curd, ..rest] = food;
console.log(rest);
```
// [ 'sweetcorn', 'cake' ]





