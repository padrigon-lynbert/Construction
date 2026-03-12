function addProject() {
    fetch("{% url 'add_empty_project' %}", {
        method: "POST",
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    })
    .then(() => loadContent("{% url 'quotation' %}"));
}

function deleteProject(id) {
    fetch(`quotation/delete_project/${id}/`)
        .then(() => loadContent("{% url 'quotation' %}"));
}

// Search functionality
document.addEventListener("input", function(e){

    if(e.target.id === "search"){

        const query = e.target.value.toLowerCase();
        const cards = document.querySelectorAll(".project-card");

        cards.forEach(card=>{
            const name = card.dataset.name;
            card.style.display = name.includes(query) ? "block" : "none";
        });

    }

});


// CSRF helper
function getCookie(name) {
    let cookieValue = null;
    document.cookie.split(';').forEach(cookie => {
        const [k, v] = cookie.trim().split('=');
        if (k === name) cookieValue = decodeURIComponent(v);
    });
    return cookieValue;
}