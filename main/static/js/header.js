const header = document.querySelector('header');
const mainHeaderNav = document.querySelector('.main__nav-list');
window.addEventListener('scroll', () => {
    if (Math.ceil(pageYOffset) >= header.offsetHeight){
        if (window.innerWidth <= 1024){
            mainHeaderNav.style.display = 'none';
        }else {
            mainHeaderNav.style.display = 'flex';
        }
    }else {
        mainHeaderNav.style.display = 'none';
    }
})

// audio
const headerLogo = document.querySelectorAll('.header__logo');
let logoAudio = new Audio('./audio/logoMusic.mp3')


headerLogo.forEach(item => {
    item.addEventListener('mouseover', () => {
        logoAudio.play()
    })
})
// menu drop down
const headerNavList = document.querySelector('.header__nav-list-mobile');
const headerNavMobileBtn = document.querySelector('.header__nav-mobile-btn');
headerNavMobileBtn.addEventListener('click', () => {
    headerNavList.classList.toggle('header__nav-active');
})

