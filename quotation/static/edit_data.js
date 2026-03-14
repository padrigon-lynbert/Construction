function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== ''){
        const cookies = document.cookie.split(';');
        for (let cookie of cookies){
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')){
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// autosave for contenteditable cells with class= "selected_cell" -only for single fields (table not included)
document.addEventListener('DOMContentLoaded', function() {

    const selected_cell = document.querySelectorAll(".selected_cell");

    selected_cell.forEach(cell => {

        cell.addEventListener("blur", function() {

            const field = this.dataset.field;
            const value = this.value === "" ? 0 : (this.value ?? this.textContent);
            const id = this.dataset.id; 
            const csrftoken = getCookie('csrftoken');

            console.log("field:", field);
            console.log("value:", value);

            fetch(urls.update_individual_quotation, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrftoken
                },
                body: JSON.stringify({
                    id: id,
                    field: field,
                    value: value
                })
            })
            .then(response => response.json())
            .then(data => {
                console.log("Server response:", data);
            })
            .catch(error => console.error("Error:", error));
        });
    });
});


// autosave for table cells with class="table_edit_item" - for items in the table
document.addEventListener('DOMContentLoaded', function() {
    const tableCells = document.querySelectorAll(".table_edit_item");

    tableCells.forEach(cell => {
        cell.addEventListener("blur", function() {
            const field = this.dataset.field;
            const value = this.value !== undefined ? this.value : this.textContent;
            const id = this.closest("tr").dataset.id;
            const csrftoken = getCookie('csrftoken');

            console.log("table update:", field, value, id);

            fetch(urls.update_item, {
                method: "POST",
                headers:{
                    "Content-Type":"application/json",
                    "X-CSRFToken": csrftoken
                },
                body: JSON.stringify({
                    id: id,
                    field: field,
                    value: value
                })
            })
            .then(r => r.json())
            .then(data => console.log(data))
            .catch(err => console.error(err));
        });
    });
});
