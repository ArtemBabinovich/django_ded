const btn = document.querySelector('.header__nav-phone-btn');
const list = document.querySelector('.header__nav-list')
const header = document.querySelector('header');
const mainHeader = document.querySelector('.main__nav-list');
btn.addEventListener('click', () => {
    list.classList.toggle('active');
})
window.addEventListener('scroll', () => {
    if (Math.ceil(pageYOffset) >= header.offsetHeight){
        mainHeader.style.display = 'flex';
    }else {
        mainHeader.style.display = 'none';
    }
})

// console.log(header.offsetHeight)