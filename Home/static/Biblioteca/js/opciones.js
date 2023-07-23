//Condiciones para los divs de administrarlibros

function MostrarIngresar(){
    
    document.getElementById("Ingresar").style.display = "block"
    document.getElementById("BotonIngresar").style.backgroundColor = "#40A6FF" 
    document.getElementById("Visualizar").style.display = "none"
    document.getElementById("BotonVisualizar").style.backgroundColor = "white"
    document.getElementById("Eliminar").style.display = "none"
    document.getElementById("BotonEliminar").style.backgroundColor = "white"
    document.getElementById("Editar").style.display = "none"
    document.getElementById("BotonEditar").style.backgroundColor = "white"    
}

function MostrarVisualizar(){
    document.getElementById("Ingresar").style.display = "none"
    document.getElementById("BotonIngresar").style.backgroundColor = "white"
    document.getElementById("Visualizar").style.display = "block"
    document.getElementById("BotonVisualizar").style.backgroundColor = "#40A6FF"
    document.getElementById("Eliminar").style.display = "none"
    document.getElementById("BotonEliminar").style.backgroundColor = "white"
    document.getElementById("Editar").style.display = "none"
    document.getElementById("BotonEditar").style.backgroundColor = "white"
}
function MostrarVisualizarA(){
    document.getElementById("Visualizar").style.display = "block"
    document.getElementById("BotonVisualizar").style.backgroundColor = "#40A6FF"
}
function MostrarEliminar(){
    document.getElementById("Ingresar").style.display = "none"
    document.getElementById("BotonIngresar").style.backgroundColor = "white"
    document.getElementById("Visualizar").style.display = "none"
    document.getElementById("BotonVisualizar").style.backgroundColor = "white"
    document.getElementById("Eliminar").style.display = "block"
    document.getElementById("BotonEliminar").style.backgroundColor = "#40A6FF"
    document.getElementById("Editar").style.display = "none"
    document.getElementById("BotonEditar").style.backgroundColor = "white"
}

function MostrarEditar(){
    document.getElementById("Ingresar").style.display = "none"
    document.getElementById("BotonIngresar").style.backgroundColor = "white"
    document.getElementById("Visualizar").style.display = "none"
    document.getElementById("BotonVisualizar").style.backgroundColor = "white"
    document.getElementById("Eliminar").style.display = "none"
    document.getElementById("BotonEliminar").style.backgroundColor = "white"
    document.getElementById("Editar").style.display = "block"
    document.getElementById("BotonEditar").style.backgroundColor = "#40A6FF"
}