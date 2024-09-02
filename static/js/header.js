document.addEventListener("DOMContentLoaded", function () {
    const header = document.querySelector('.fixed-top');
    const content = document.querySelector('.content');

    if (header) {
        const headerHeight = header.offsetHeight;
        content.style.paddingTop = headerHeight + 'px';
    }
});