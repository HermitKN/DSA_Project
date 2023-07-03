//Condiciones para los divs de administrarlibros

function MostrarIngresar(){
    
    document.getElementById("Ingresar").style.display = "block"
    document.getElementById("Visualizar").style.display = "none"
    document.getElementById("Eliminar").style.display = "none"
    document.getElementById("Editar").style.display = "none"
    
}

function MostrarVisualizar(){
    document.getElementById("Ingresar").style.display = "none"
    document.getElementById("Visualizar").style.display = "block"
    document.getElementById("Eliminar").style.display = "none"
    document.getElementById("Editar").style.display = "none"
}

function MostrarEliminar(){
    document.getElementById("Ingresar").style.display = "none"
    document.getElementById("Visualizar").style.display = "none"
    document.getElementById("Eliminar").style.display = "block"
    document.getElementById("Editar").style.display = "none"
}

function MostrarEditar(){
    document.getElementById("Ingresar").style.display = "none"
    document.getElementById("Visualizar").style.display = "none"
    document.getElementById("Eliminar").style.display = "none"
    document.getElementById("Editar").style.display = "block"
}
function EliminarLibro(id){
    if(confirm("¿Seguro que desea eliminarlo?")){
       
    }
}