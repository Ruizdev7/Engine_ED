window.addEventListener('scroll', function () {
    let header = document.querySelector('header')
    header.classList.toggle('sticky', window.scrollY > 0)
})

const iconoMenu = document.querySelector('#icono-menu')
menu = document.querySelector('#menu');

iconoMenu.addEventListener('click', (e) => {
    menu
        .classList
        .toggle('activate')
    document
        .body
        .classList
        .toggle('opacity')

    const rutaActual = e
        .target
        .getAttribute('src')
    if (rutaActual == '../static/imgs/open-menu.png') {
        e
            .target
            .setAttribute('src', '../static/imgs/open-menu2.png')
    } else {
        e
            .target
            .setAttribute('src', '../static/imgs/open-menu.png')
    }
})