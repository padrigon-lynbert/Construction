function loadContent(url) {
    // click sidebar to get url, then fetch content and update the page
    fetch(url)
        .then(response => response.text())
        .then(data => {
            document.querySelector(".content").innerHTML = data;
        });
}