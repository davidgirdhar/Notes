### Hooks
Now in react we render html elements using ReactDOM. Now suppose we want our page to be user-responsive then we have to re-render that particular html elements. For example:

```javascript
import React from "react";
import ReactDOM from "react-dom";

let count = 0;

function increase(){
    count++;
}

ReactDOM.render(
  <div className="container">
    <h1>{count}</h1>
    <button on-click={increase}>+</button>
  </div>,
  document.getElementById("root")
);
```

now here you can that despite clicking on + button value of count won't increase on interface but in our logs only.
But if we call this ReactDOM every time then it then value will increase.But that piece of code would be inefficient because of repitition.

So here comes Hooks to our rescue, `useState` Hook allows us to track state in a function component 


```javascript
import { useState } from "react";

function FavoriteColor() {
  const [color, setColor] = useState("red");
}

```

here in color we set our default value and with of setcolor function we can update it's value. You can use amy name just like of a variable.