MétodosDescripción

.then(resolve)              //Ejecuta la función callback resolve cuando la promesa se cumple.
.catch(reject)              //Ejecuta la función callback reject cuando la promesa se rechaza.
.then(resolve,reject)       //Método equivalente a las dos anteriores en el mismo .then().
.finally(end)               //Ejecuta la función callback end tanto si se cumple como si se rechaza.

//-------------------------------------------------------------

fetch("/url").then(function(response) {   // es una promesa, pedis que te traiga una URL, te muestre una estructura mientras busca la respuesta a tu promesa
    /* Código a realizar cuando se cumpla la promesa */
  });

  fetch("127.0.0.1:5000").then(function(response) {
    /* Código a realizar cuando se cumpla la promesa */
  });

//-------------------------------------------------------------

  fetch("/url")   // Estructura basica. fetch a la API, si responde se resuelve then, sino catch. Responder es devolver un json.
  .then(function(response) {
    /* Código a realizar cuando se cumpla la promesa */
  })
  .catch(function(error) {    // "Error al obtener los productos." Esto es el catch.
    /* Código a realizar cuando se rechaza la promesa */
  });

  //-------------------------------------------------------------

  fetch("/url")   // LOGICA: Hacemos un fetch a la URL, verificamos si hay respuesta, si la hay traemos los datos, y sino que me haga un error.
  .then(response => {
    return response.text(); // Devuelve una promesa
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => { /* Código a realizar cuando se rechaza la promesa */ });



  //-------------------------------------------------------------

  //https://lenguajejs.com/javascript/asincronia/promesas/