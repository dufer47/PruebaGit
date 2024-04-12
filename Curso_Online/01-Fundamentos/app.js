console.log("Otra manera de mostrar Hola Mundo!")

var listaInvitados = [];
var flag = true;
var index = 0;

while(flag == true)
{
    invitado = prompt("Ingrese Nombre del invitado");
    if (invitado != "")
        break;
    else (invitado == "")
        alert("Error. Ingrese datos validos");
}
