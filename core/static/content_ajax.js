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
            // add more pages in future
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

    // make cells editable and send updates on blur
    cells.forEach(cell => {
        cell.setAttribute("tabindex", "0");
        cell.addEventListener("blur", function() {
            const rowId = this.closest("tr").dataset.id;
            const field = this.dataset.field;
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

// load default content on page load (you can change this to any page you want as default) the defaul is set to leads page in templates/core_spa.html
document.addEventListener("DOMContentLoaded", function() {
    loadContent(defaultPage);
});