let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { orderable: false, targets: [8, 9] },
        { searchable: false, targets: [4, 5, 6] }
    ],
    pageLength: 4,
    destroy: true
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await listaLibros();

    dataTable = $("#tablas_Libros").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const listaLibros = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/administrarlibros/verlibros/");
        const data = await response.json();
        let content = ``;
        data.libros.forEach((libros) => {
            content += `
                <tr>
                    <td style="text-align: center !important;">${libros.id}</td>
                    <td style="text-align: center !important;">${libros.nombre}</td>
                    <td style="text-align: center !important;">${libros.autor}</td>
                    <td style="text-align: center !important;">${libros.tipo}</td>
                    <td style="text-align: center !important;">${libros.cantidadint}</td>
                    <td style="text-align: center !important;">${libros.cantidadext}</td>
                    <td style="text-align: center !important;">${libros.cantidadext+libros.cantidadint}</td>
                    <td style="text-align: center !important;">${libros.categoria}</td>
                    <td style="text-align: center !important;">${libros.descripcion}</td>
                    <td style="text-align: center !important;">${libros.fecha}</td>
                </tr>`;
        });
        tableBody.innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});