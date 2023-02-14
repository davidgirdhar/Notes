## Increase Maximum Size of nodejs deafult memory


```node --max-old-space-size=8192 script.js ```

One of the way to increase default size of nodejs is by running given above command and one of the other option is by changing value of start in packag.json file in script object just like give below:

```Javascript 
{

  "scripts":{
     "start": "node --max-old-space-size=4076 server.js"
  } 

}
```


