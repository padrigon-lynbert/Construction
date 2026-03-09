// fetch page and inject the content
function loadContent(url) {
    fetch(url)
        .then(response => response.text())
        .then(data => {
            const contentDiv = document.querySelector(".content");
            contentDiv.innerHTML = data;

            // check page type and initialize JS
            if (url.includes("leads")) {
                initLeadsTable(contentDiv);
            }
            // you can add more pages in future
            // else if (url.includes("quotation")) { initQuotation(contentDiv); }
        });
}

// initialize leads table
function initLeadsTable(container) {
    const cells = container.querySelectorAll(".cell");

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let cookie of cookies) {
                cookie = cookie.trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    cells.forEach(cell => {
        cell.setAttribute("tabindex", "0");
        cell.addEventListener("blur", function() {
            const rowId = this.closest("tr").dataset.id;
            const field = this.dataset.field;
            // const value = this.textContent;
                const value = this.tagName === "INPUT" || this.tagName === "TEXTAREA" ? this.value : this.textContent;
            const csrftoken = getCookie('csrftoken');

            console.log("Row ID:", rowId);
            console.log("Field:", field);
            console.log("Value:", value);

            fetch("/lead_management/update_lead/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrftoken
                },
                body: JSON.stringify({ id: rowId, field: field, value: value })
            }).catch(error => console.error("Error:", error));
        });
    });
}


document.addEventListener("DOMContentLoaded", function() {
    loadContent(defaultPage); // default content when page loads
});