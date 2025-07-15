document.addEventListener("DOMContentLoaded", () => {
    const button = document.querySelector("#changeStyle");
    const paragraph = document.querySelector("#text");
    button.addEventListener("click", () => {
        paragraph.classList.add("red");
    });
});