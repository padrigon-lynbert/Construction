function loadContent(url) {
    fetch(url)
        .then(response => response.text())
        .then(data => {
            document.querySelector(".content").innerHTML = data;
        });
}