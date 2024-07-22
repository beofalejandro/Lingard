var header = document.getElementById('header');
var header_link = document.getElementById('header-link');

window.addEventListener('scroll', () => {
    var scroll = window.scrollY
    if (scroll > 10) {
        header.style.backgroundColor = '#151515'
        header_link.style.color = '#F2BEFC'
    } else {
        header.style.backgroundColor = 'transparent'
        header_link.style.color = '#FFFFFF'
    }
});