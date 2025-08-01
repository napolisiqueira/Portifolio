// Carrossel de certificados - rolagem suave com setas
// Este script permite rolar horizontalmente o carrossel de certificados com as setas

document.addEventListener('DOMContentLoaded', function () {
    const carousel = document.getElementById('certificates-carousel');
    const leftBtn = document.querySelector('.carousel-arrow.left');
    const rightBtn = document.querySelector('.carousel-arrow.right');
    if (!carousel || !leftBtn || !rightBtn) return;

    const scrollAmount = 280; // px

    leftBtn.addEventListener('click', () => {
        carousel.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
    });
    rightBtn.addEventListener('click', () => {
        carousel.scrollBy({ left: scrollAmount, behavior: 'smooth' });
    });
});
