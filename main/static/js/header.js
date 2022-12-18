const header = document.querySelector('header');
const mainHeaderNav = document.querySelector('.main__nav-list');
const mainDownNav = document.querySelector('.main__down-navigation-list')
window.addEventListener('scroll', () => {
    if (Math.ceil(pageYOffset) >= header.offsetHeight){
        if (window.innerWidth <= 1024){
            mainHeaderNav.style.display = 'none';
            mainDownNav.style.display = 'none';
        }else {
            mainHeaderNav.style.display = 'flex';
            mainDownNav.style.display = 'flex';
        }
    }else {
        mainHeaderNav.style.display = 'none';
        mainDownNav.style.display = 'none';
    }
})

// menu drop down
const headerNavList = document.querySelector('.header__nav-list-mobile');
const headerNavMobileBtn = document.querySelector('.header__nav-mobile-btn')
const dropDownPresentsMobile = document.querySelectorAll('.drop__down-present-wrapper')
const dropDownSalesMobile = document.querySelectorAll('.drop-down-menu-wrapper')
headerNavMobileBtn.addEventListener('click', () => {
    headerNavList.classList.toggle('header__nav-active');
    dropDownPresentsMobile.forEach(item => {
        if (item.classList.contains('active')){
            item.classList.remove('active')
        }
    })
    dropDownSalesMobile.forEach(item => {
        if (item.classList.contains('active')){
            item.classList.remove('active')
        }
    })
})

// get phone in header
const headerPhone = document.querySelector('.header__phone');
function get__phone(url) {
    fetch(url)
        .then(resp => resp.json())
        .then(res => {
            for (let i of res){
                headerPhone.innerHTML += `
                                            <a href="#">${i.country_code} /${i.number_operator}/ <span style="color: ${i.color_number}">${i.number_phone}</span></a>
                                        `
            }
        })
}
get__phone("https://developer.itec.by/api/phone/")
//get social
const socialNavList = document.querySelectorAll('.secondBlock__nav-list');
function get__social(url) {
    fetch(url)
        .then(resp => resp.json())
        .then(res => {
            for (let i of res){
                socialNavList.forEach(socialNavListItem => {
                    socialNavListItem.innerHTML += `
                                                        <li class="secondBlock__list-item">
                                                            <a href="${i.link}">
                                                                <div class="secondBlock__list-item-imageWrapper">
                                                                    <img src="${i.logo}" alt="${i.name}">
                                                                </div>
                                                                <p>${i.name}</p>
                                                            </a>
                                                        </li>
                                                    `
                })
            }
        })
}
get__social('https://developer.itec.by/api/social_networks/')
// audio
window.onload = function () {
    const headerLogo = document.querySelectorAll('.header__logo');
    let logoAudio = new Audio('https://developer.itec.by/media/audio/logoMusic.mp3')
    headerLogo.forEach(item => {
        item.addEventListener('mouseover', () => {
            logoAudio.play()
        })
    })
}
const Footer = document.querySelector('footer')
const Header = document.querySelector('header')
const windowUp = document.getElementById('#windowUp')
const windowDown = document.getElementById('#windowDown')
windowUp.addEventListener('click', () => {
    scrollBy(0,Header.getBoundingClientRect().top)
})
windowDown.addEventListener('click', () => {
    scrollBy(0,Footer.getBoundingClientRect().bottom)
})