let arrow = document.querySelectorAll('.arrow');

for (let i = 0; i < arrow.length; i++) {

    arrow[i].addEventListener('click', (e) => {
        const arrowParent = e.target.parentElement.parentElement

        arrowParent.classList.toggle("showMenu")
    })
}

const sideBar = document.querySelector('.sidebar')
const sideBarBtn = document.querySelector('.fa-bars')

sideBarBtn.addEventListener('click', e => {
    sideBar.classList.toggle('close')
})

const iconos = document.querySelectorAll('.iconos')

for (let i = 0; i < iconos.length; i++) {

    iconos[i].addEventListener('click', e => {

        const nuevo = e.target.parentElement.parentElement.parentElement;

        nuevo.classList.add('showMenu');

        if (e.target.matches(".iconos")) {
            sideBar.classList.remove('close');
        };
    });
};