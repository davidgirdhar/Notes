## <ins>TypeError: Reduce of empty array with no initial value</ins>

Error because your are applying reduce function on an empty array

This can be handled by checking if length of an array is zero or not.


##  <ins>Error message "error:0308010C:digital envelope routines::unsupported"</ins>

```Error: error:0308010C:digital envelope routines::unsupported
    at new Hash (node:internal/crypto/hash:67:19)
    at Object.createHash (node:crypto:130:10)
    at module.exports (/Users/user/Programming Documents/WebServer/untitled/node_modules/webpack/lib/util/createHash.js:135:53)
    at NormalModule._initBuildHash (/Users/user/Programming Documents/WebServer/untitled/node_modules/webpack/lib/NormalModule.js:417:16)
    at handleParseError (/Users/user/Programming Documents/WebServer/untitled/node_modules/webpack/lib/NormalModule.js:471:10)
    at /Users/user/Programming Documents/WebServer/untitled/node_modules/webpack/lib/NormalModule.js:503:5
    at /Users/user/Programming Documents/WebServer/untitled/node_modules/webpack/lib/NormalModule.js:358:12
    at /Users/user/Programming Documents/WebServer/untitled/node_modules/loader-runner/lib/LoaderRunner.js:373:3
    at iterateNormalLoaders (/Users/user/Programming Documents/WebServer/untitled/node_modules/loader-runner/lib/LoaderRunner.js:214:10)
    at iterateNormalLoaders (/Users/user/Programming Documents/WebServer/untitled/node_modules/loader-runner/lib/LoaderRunner.js:221:10)
/Users/user/Programming Documents/WebServer/untitled/node_modules/react-scripts/scripts/start.js:19
  throw err;
  ^
```

In your package.json: change this line

```"start": "react-scripts start"```

to
<br>
```"start": "react-scripts --openssl-legacy-provider start"```



## <ins>npm "failed to parse json"</ins>

There should be problem with your json check if there might ne extra commas just like mention below.

```
},
  "devDependencies": {
    "axios": "^0.15.3",
    "bootstrap-sass": "^3.3.7",
    "cross-env": "^3.2.4",
    "jquery": "^3.1.1",
    "laravel-mix": "0.*",
    "lodash": "^4.17.4",
    "vue": "^2.1.10",
  }
```