const animado = document.querySelectorAll('.animado');


function mostrarScroll() {
    const scrollTop = document.documentElement.scrollTop;
    for (let i = 0; i < animado.length; i++) {
        const alturaAnimado = animado[i].offsetTop;
        if (alturaAnimado - 450 < scrollTop) {
            animado[i].style.opacity = 1;
            animado[i].classList.add('mostrarArriba')
        }
    }
}

window.addEventListener('scroll', mostrarScroll);