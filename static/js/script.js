window.addEventListener('scroll', function() {
    const header = document.querySelector('header');
    header.classList.toggle("sticky", window.scrollY > 0)
});

function menuToggle() {
    const navToggle = document.querySelector('.menu-toggle');
    const navbar = document.querySelector('.navbar');
    navToggle.classList.toggle('active');
    navbar.classList.toggle('active');
}

const btnDismiss = document.querySelector('.btn-dismiss');
const popupBox = document.querySelector('.popup-overlay');

btnDismiss.addEventListener('click', () => {
    popupBox.classList.add('dismiss');
})