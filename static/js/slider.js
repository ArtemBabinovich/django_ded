const mainSwiperWrapper = document.querySelector('.main__swiper-slider');
const miniSlidersWrapper = document.querySelector('.main__content-block-mini-sliders-wrapper');

// класс для создания экземпляров таймера баннеров
class CountdownTimer {
    constructor(deadline, cbChange, param, cbComplete) {
        this._deadline = deadline;
        this._cbChange = cbChange;
        this._cbComplete = cbComplete;
        this._timerId = null;
        this._out = {
            days: '',
            hours: '',
            minutes: '',
            seconds: '',
            daysTitle: '',
            hoursTitle: '',
            minutesTitle: '',
            secondsTitle: '',
            param: param,
        };
        this._start();
    }

    static declensionNum(num, words) {
        return words[(num % 100 > 4 && num % 100 < 20) ? 2 : [2, 0, 1, 1, 1, 2][(num % 10 < 5) ? num % 10 : 5]];
    }

    _start() {
        this._calc();
        this._timerId = setInterval(this._calc.bind(this), 1000);
    }

    _calc() {
        const diff = this._deadline - new Date();
        const days = diff > 0 ? Math.floor(diff / 1000 / 60 / 60 / 24) : 0;
        const hours = diff > 0 ? Math.floor(diff / 1000 / 60 / 60) % 24 : 0;
        const minutes = diff > 0 ? Math.floor(diff / 1000 / 60) % 60 : 0;
        const seconds = diff > 0 ? Math.floor(diff / 1000) % 60 : 0;
        this._out.days = days < 10 ? '0' + days : '' + days;
        this._out.hours = hours < 10 ? '0' + hours : '' + hours;
        this._out.minutes = minutes < 10 ? '0' + minutes : '' + minutes;
        this._out.seconds = seconds < 10 ? '0' + seconds : '' + seconds;
        this._out.daysTitle = CountdownTimer.declensionNum(days, ['день', 'дня', 'дней']);
        this._out.hoursTitle = CountdownTimer.declensionNum(hours, ['час', 'часа', 'часов']);
        this._out.minutesTitle = CountdownTimer.declensionNum(minutes, ['минута', 'минуты', 'минут']);
        this._out.secondsTitle = CountdownTimer.declensionNum(seconds, ['секунда', 'секунды', 'секунд']);
        this._cbChange ? this._cbChange(this._out) : null;
        if (diff <= 0) {
            clearInterval(this._timerId);
            this._cbComplete ? this._cbComplete() : null;
        }
    }
}


function getSwiperItem(url) {
    fetch(url)
        .then(resp => resp.json())
        .then(item => {
            for (let i of item.results) {
                mainSwiperWrapper.innerHTML += `<div class="main__slider-slide swiper-slide">
                                                    <div class="main__slider-slide-image">
                                                        <img class="main__slider-image" src='${i.image_for_big_slider}' alt="">
                                                    </div>
                                                    <div class="container">
                                                        <a href="#${i.url}" class="main__slider-slide-link">
                                                            <p style="color: ${i.color_title}">
                                                                ${i.title}
                                                            </p>
                                                            <p style="color: ${i.color_title};">
                                                                ${i.additional_title ? i.additional_title : ''}
                                                            </p>
                                                        </a>
                                                    </div>
                                            </div>`
            }

            const swiper = new Swiper('.main__slider-wrapper', {
                pagination: {
                    el: '.swiper-pagination', type: 'bullets', clickable: true,
                }, loop: true, simulateTouch: false, navigation: {
                    nextEl: '.slider__action-prev', prevEl: '.slider__action-next',
                }, slidesPerView: 1, autoplay: {
                    delay: item.timer ? item.timer : 2000, disableOnInteraction: false, pauseOnMouseEnter: true,
                }
            });
            // const mainSliderWrapper = document.querySelector('.main__slider-wrapper');
            // const mainSliderImage = document.querySelectorAll('.main__slider-image');
            // const zoomWindow = document.querySelector('.main__slider-zoomWindow');
            // if (window.innerWidth <= 1024) {
            //
            // } else {
            //     mainSliderWrapper.addEventListener('mousemove', (e) => {
            //         let src = '';
            //         zoomWindow.style.display = 'block'
            //         zoomWindow.style.top = `${e.offsetY - 40}px`
            //         zoomWindow.style.left = `${e.offsetX + 100}px`
            //         mainSliderImage.forEach(slidesItem => {
            //             if (e.target === slidesItem) {
            //                 src = slidesItem.getAttribute('src')
            //             }
            //         })
            //         let sliderWidth = document.querySelector('.main__slider').clientWidth;
            //         zoomWindow.style.background = `url(${src})`;
            //         zoomWindow.style.backgroundRepeat = 'no-repeat'
            //         zoomWindow.style.backgroundSize = `${sliderWidth}px`;
            //         zoomWindow.style.backgroundPositionX = `${-e.offsetX + 45}px`
            //         zoomWindow.style.backgroundPositionY = `${-e.offsetY + 40}px`
            //         zoomWindow.style.transform = `scale(2.3)`;
            //     })
            //     mainSliderWrapper.addEventListener('mouseout', () => {
            //         zoomWindow.style.display = 'none'
            //     })
            // }
        })
}

getSwiperItem('https://developer.itec.by/api/big_slider/')

let page = 1;
let offset = 850;
let prevPage = true;
window.addEventListener('scroll', () => {
    if (window.pageYOffset > offset) {
        offset += 850
        if (prevPage) {
            page++
            miniSliders(`https://developer.itec.by/api/small_slider_with_pagination/?page=${page}`)
        }
    }
})
let stateTips = true;

function miniSliders(url) {
    fetch(url)
        .then(resp => resp.json())
        .then(res => {
            if (!res.next) {
                prevPage = false
            }
            let services = ``;
            let count = 1;
            console.log(res)
            for (let i of res.slides) {
                for (let j of i.services) {
                    services += `
                                <a href="https://www.google.com/" class="mini__swiper-item swiper-slide">
                                    <div class="mini__swiper-item-image">
                                        <img data-lazy="${j.image_for_mini_slider}" alt="${j.image_for_mini_slider}">
                                    </div>
                                    <div class="mini__swiper-item-text">
                                        <p style="color: ${j.color_service_title}">${j.service_title}</p>
                                        <p style="color: ${j.color_bottom_description};">${j.bottom_description}</p>
                                        <p style="color: ${j.color_bottom_description_2}; display: ${j.bottom_description_2 === null ? 'none' : 'block'}">${j.bottom_description_2}</p>
                                    </div>
                                </a>
                                `
                }
                let div = document.createElement('div')
                div.innerHTML = `
                                <div class="main__content-block-mini-slider-item" id="${i.url}">
                                    <div class="mini__slider-title-wrapper">
                                        <div class="mini__slider-item-title"">
                                            ${i.title} ${i.additional_title === null ? '' : i.additional_title}
                                    </div>
                                    <div class="main__slider-item-sub-title">
                                        ${i.additional_title_2 === null ? '' : i.additional_title_2}
                                    </div>
                                </div>
                                <div class="mini__swiper-container${page}">
                                    ${services}
                                </div>
                            </div>
                        `
                miniSlidersWrapper.append(div)
                services = ``
                count++
            }
            let countTips = 0;
            let adviceContent = ``
            let anchorsLi = ``
            let contentDescription = ``;
            let openAllBlock = ``;

            function get_tips(url) {
                fetch(url)
                    .then(resp => resp.json())
                    .then(result => {
                        console.log(result)
                        const blockMiniSlider = document.querySelectorAll('.main__content-block-mini-slider-item')
                        if (blockMiniSlider[0].children[3]) {
                            countTips++
                        }
                        // циклы для заголовка и контента советов adviceContent
                        adviceContent += `
                                    <div class="swiper__tips-drop-title">
                                        ${result.results[0] ? result.results[0].advices[0].title : ''}
                                    </div>
                                    <div class="swiper__tips-drop-sub-title">
                                        ${result.results[0] ? result.results[0].advices[0].title2 : ''}
                                    </div>
                                `
                        if (result.results[0]) {
                            for (let l of result.results[0].advices[0].content) {
                                contentDescription += `
                                            <div class="swiper__tips-drop-about-head" id="${l.url}">
                                                ${l.title}
                                            </div>
                                            ${l.description}
                                            <a href="${l.service === null ? '' : l.service.url}" style="display: ${l.service === null ? 'none' : 'block'}">
                                                ${l.service === null ? '' : l.service.service_title}
                                            </a>
                                            <div class="swiper__tips-drop-image" style="display: ${l.photo === null ? 'none' : 'block'}">
                                                <img src="${l.photo === null ? '' : l.photo}" alt="${l.photo === null ? '' : l.photo}">
                                            </div>
                                            <a href="${l.services_catalog === null ? '' : l.services_catalog.url}" class="swiper__tips-drop-image-title" style="display: ${l.services_catalog === null ? 'none' : 'block'}">
                                                ${l.services_catalog === null ? '' : l.services_catalog.title}
                                            </a>
                                        `
                            }
                        }
                        adviceContent += `
                                        <div class="swiper__tips-drop-about">
                                            ${contentDescription}
                                        </div>
                                    `
                        contentDescription = ``
                        // циклы для заголовков и контента советов openAllBlock
                        if (result.results[0]) {
                            result.results[0].advices.shift()
                            for (let i of result.results[0].advices) {
                                openAllBlock += `
                                    <div class="swiper__tips-drop-title">
                                        ${i.title}
                                    </div>
                                    <div class="swiper__tips-drop-sub-title">
                                        ${i.title2}
                                    </div>
                                `
                                for (let l of i.content) {
                                    contentDescription += `
                                            <div class="swiper__tips-drop-about-head" id="${l.url}">
                                                ${l.title}
                                            </div>
                                            ${l.description}
                                            <div class="swiper__tips-drop-image" style="display: ${l.photo === null ? 'none' : 'block'}">
                                                <img src="${l.photo === null ? '' : l.photo}" alt="${l.photo === null ? '' : l.photo}">
                                            </div>
                                            <a href="#${l.services_catalog === null ? '' : l.services_catalog.url}" class="swiper__tips-drop-image-title" style="display: ${l.services_catalog === null ? 'none' : 'block'}">
                                                ${l.services_catalog === null ? '' : l.services_catalog.title}
                                            </a>
                                            <a href="${l.service === null ? '' : l.service.url}" style="display: ${l.service === null ? 'none' : 'block'}">
                                                ${l.service === null ? '' : l.service.service_title}
                                            </a>
                                        `

                                }
                                openAllBlock += `
                                        <div class="swiper__tips-drop-about">
                                            ${contentDescription}
                                        </div>
                                    `
                                contentDescription = ``
                            }
                            // акции в советах
                            for (let k in result.results[0].discount) {
                                adviceContent += `
                                        <div class="swiper__tips-drop-stock-block" style="display: ${result.results[0].discount[k] === undefined ? 'none' : 'flex'}">
                                            ${result.results[0].discount[k]}
                                        </div>
                                    `
                            }
                            // якоря
                            for (let y of result.results[0].advices_url) {
                                anchorsLi += `
                                    <li class="swiper__tips-anchors-item">
                                        <p class="${y.url}">
                                            ${y.title}
                                        </p>
                                    </li>  
                                `
                            }
                        }
                        adviceContent += `
                                <div class="swiper__tips-content">
                                    <div class="swiper__tips-content-action-wrapper">
                                        <div class="swiper__tips-content-title">
                                        Содержание
                                        </div>
                                        <div class="swiper__tips-action-collapse">
                                            [свернуть]
                                        </div>
                                        <div class="swiper__tips-action-show">
                                            [показать]
                                        </div>
                                    </div>
                                    <div class="swiper__tips-anchors">
                                        <ul class="swiper__tips-anchors-list">
                                            ${anchorsLi}
                                        </ul>
                                    </div>
                                    <div class="swiper__tips-backAll">
                                        <span id="swiperBackAll">
                                            Читать ВСЕ ...
                                        </span>
                                    </div>
                                    <div class="swiper__tips-openAllBlock">
                                        ${openAllBlock}
                                    </div>
                                </div>
                            `
                        let div = document.createElement('div')
                        div.classList.add('mini__swiper-tips')
                        div.innerHTML = `
                                        <span class="mini__swiper-tips-text" id="tipsText">Читать СОВЕТЫ...</span>
                                        <div class="mini__swiper-tips-drop">
                                            <div class="swiper__tips-drop">
                                                ${adviceContent}
                                            </div>
                                        </div>
                        `
                        blockMiniSlider[countTips].append(div)
                        // читать советы
                        const miniSwiperTips = document.querySelector('.mini__swiper-tips');
                        const tipsText = document.getElementById('tipsText')
                        const slickArrow = document.querySelectorAll('.slick-arrow')
                        const allBlock = document.querySelector('.swiper__tips-openAllBlock')
                        miniSwiperTips.addEventListener('click', (e) => {
                            if (e.target.id === 'tipsText') {
                                e.target.parentElement.children[1].classList.toggle('tips__active')
                                e.currentTarget.parentElement.children[1].children[0].style.top = '12%'
                                e.currentTarget.parentElement.children[1].children[2].style.top = '12%'
                                e.target.parentElement.children[1].style.top = `13%`
                                e.target.parentElement.children[0].style.marginBottom = '20px'
                            }
                            if (allBlock.classList.contains('tips__active')) {

                            }
                            if (e.target.classList.contains('swiper__tips-action-show')) {
                                e.target.parentElement.parentElement.children[1].style.display = 'block'
                            }
                            if (e.target.classList.contains('swiper__tips-action-collapse')) {
                                e.target.parentElement.parentElement.children[1].style.display = 'none'
                            }
                            if (e.target.parentElement.children[1] === undefined ? false : e.target.parentElement.children[1].classList.contains('tips__active')) {
                                e.target.parentElement.children[0].textContent = 'Свернуть СОВЕТЫ'
                                tipsText.style.marginBottom = `20px`
                                e.target.parentElement.parentElement.children[1].style.top = `13%`
                                if (e.target.parentElement.parentElement.children[2].clientHeight >= 350) {
                                    e.target.parentElement.parentElement.children[1].style.top = `18%`
                                }
                            } else {
                                if (e.target.id === 'tipsText') {
                                    e.target.parentElement.children[0].textContent = 'Читать СОВЕТЫ...'
                                    e.target.parentElement.children[0].style.marginBottom = '0px'
                                    slickArrow.forEach(item => item.style.top = '40%')
                                }
                                if (e.target.id === 'swiperBackAll') {
                                    e.target.parentElement.parentElement.children[3].classList.toggle('tips__active')
                                    if (e.target.parentElement.parentElement.children[3].classList.contains('tips__active')) {
                                        e.target.parentElement.parentElement.children[2].children[0].textContent = 'Свернуть ВСЕ'
                                        e.currentTarget.parentElement.children[1].children[0].style.top = '1.4%'
                                        e.currentTarget.parentElement.children[1].children[2].style.top = '1.4%'
                                    } else {
                                        e.currentTarget.parentElement.children[1].children[0].style.top = '12%'
                                        e.currentTarget.parentElement.children[1].children[2].style.top = '12%'
                                        e.target.parentElement.parentElement.children[2].children[0].textContent = 'Читать ВСЕ'
                                    }
                                }
                            }
                        })
                        // -----------------------
                    })
            }

            if (stateTips) {
                get_tips('https://developer.itec.by/api/content_tips')
            }
            //----------------------------
            // Anchors tips logic
            const tipsAllBlock = document.querySelector('.swiper__tips-openAllBlock')
            const navTips = document.querySelectorAll('.swiper__tips-anchors-item > p');
            navTips.forEach(item => {
                item.addEventListener('click', () => {
                    tipsAllBlock.classList.add('tips__active');
                    const idElem = item.getAttribute('class')
                    const element = document.getElementById(idElem);
                    if (tipsAllBlock.classList.contains('tips__active')) {
                        scrollBy(0, element.getBoundingClientRect().top - 30)
                    }
                })
            })
            // ---------------------------
            stateTips = false
        })
        .then(timer => {
            $(document).ready(function () {
                $(`.mini__swiper-container${page}`).slick({
                    infinite: true,
                    slidesToShow: 3.5,
                    slidesToScroll: 3,
                    speed: 1000,
                    autoplay: true,
                    rtl: false,
                    autoplaySpeed: timer ? timer : 5000,
                    responsive: [{
                        breakpoint: 1920, settings: {
                            slidesToShow: 3, slidesToScroll: 3,
                        }
                    }, {
                        breakpoint: 1024, settings: {
                            slidesToShow: 2, slidesToScroll: 2,
                        }
                    }, {
                        breakpoint: 768, settings: {
                            slidesToShow: 1, slidesToScroll: 1,
                        }
                    }]
                })
            })
        })
}

miniSliders('https://developer.itec.by/api/small_slider_with_pagination/')

function banners(url) {
    fetch(url)
        .then(resp => resp.json())
        .then(res => {
            const saleBlockWrapper = document.querySelectorAll('.main__content-sale-block-item-wrapper');
            let countdownTimerItem = 0;
            for (let i in res) {
                for (let m of res[i]) {
                    let sliderItems = ``;
                    let sliderItems1 = ``;
                    let sliderItems2 = ``;
                    let timerItems = ``;
                    if (m.slider_1 || m.slider_2) {
                        for (let j of m.slider_1) {
                            sliderItems1 += `
                                        <div class="main__content-sale-block-swiper-item">
                                            <img src="https://developer.itec.by${j.foto}" alt="">
                                            <div class="main__content-sale-block-swiper-item-title">
                                                <p>${j.name}</p>
                                            </div>
                                        </div>
                                        `
                        }
                        for (let k of m.slider_2) {
                            sliderItems2 += `
                                        <div class="main__content-sale-block-swiper-item">
                                            <img src="https://developer.itec.by${k.foto}" alt="">
                                            <div class="main__content-sale-block-swiper-item-title">
                                                <p>${k.name}</p>
                                            </div>
                                        </div>
                                        `
                        }
                    } else {
                        for (let j of m.slider) {
                            sliderItems += `
                                            <div class="main__content-sale-block-swiper-item">
                                                <img src="https://developer.itec.by${j.foto}" alt="">
                                                <div class="main__content-sale-block-swiper-item-title">
                                                    <p>${j.name}</p>
                                                </div>
                                            </div>
                                            `
                        }
                    }
                    if (m.timer !== undefined) {
                        countdownTimerItem++
                        timerItems = `
                                    <div class="main__content-sale-block-item-main-end-time-item">
                                        <div class="main__content-sale-block-item-main-end-time-item-date-wrap">
                                            <div class="main__content-sale-block-item-main-end-time-item-date item_date-count-days${countdownTimerItem}">
                                                
                                            </div>
                                            <div class="main__content-sale-block-item-main-end-time-item-date item_date-count-days${countdownTimerItem}">
                                                
                                            </div>
                                        </div>
                                        <div class="main__content-sale-block-item-main-end-time item_date-count-days-text${countdownTimerItem}">
                                            
                                        </div>
                                    </div>
                                    <div class="main__content-sale-block-item-main-end-time-item">
                                        <div class="main__content-sale-block-item-main-end-time-item-date-wrap">
                                            <div class="main__content-sale-block-item-main-end-time-item-date item_date-count-hours${countdownTimerItem}">
                                                
                                            </div>
                                            <div class="main__content-sale-block-item-main-end-time-item-date item_date-count-hours${countdownTimerItem}">
                                                
                                            </div>
                                        </div>
                                        <div class="main__content-sale-block-item-main-end-time item_date-count-hours-text${countdownTimerItem}">
                                            
                                        </div>
                                    </div>
                                    <div class="main__content-sale-block-item-main-end-time-item">
                                        <div class="main__content-sale-block-item-main-end-time-item-date-wrap">
                                            <div class="main__content-sale-block-item-main-end-time-item-date item_date-count-minutes${countdownTimerItem}">
                                                
                                            </div>
                                            <div class="main__content-sale-block-item-main-end-time-item-date item_date-count-minutes${countdownTimerItem}">
                                                
                                            </div>
                                        </div>
                                        <div class="main__content-sale-block-item-main-end-time item_date-count-minutes-text${countdownTimerItem}">
                                            
                                        </div>
                                    </div>
                                    <div class="main__content-sale-block-item-main-end-time-item">
                                        <div class="main__content-sale-block-item-main-end-time-item-date-wrap">
                                            <div class="main__content-sale-block-item-main-end-time-item-date item_date-count-seconds${countdownTimerItem}">
                                                
                                            </div>
                                            <div class="main__content-sale-block-item-main-end-time-item-date item_date-count-seconds${countdownTimerItem}">
                                                
                                            </div>
                                        </div>
                                        <div class="main__content-sale-block-item-main-end-time item_date-count-seconds-text${countdownTimerItem}">
                                            
                                        </div>
                                    </div>
                                `
                    }
                    let calendarDate = new Date(m.calendar_date)
                    console.log(m.slider)
                    saleBlockWrapper.forEach(item => {
                        item.innerHTML += `
                                        <div class="main__content-sale-block-item ${m.baner_type_2 ? "bannerT2" : 'banner'}">
                                        <div class="main__content-sale-block-item-time-wrapper">
                                            <div class="main__content-sale-block-item-time" style="display: ${m.calendar_title ? 'block' : 'none'};">
                                                ${m.calendar_title}
                                            </div>
                                            <div class="main__content-sale-block-item-sub-time" style="display: ${m.calendar_date ? 'block' : 'none'}">
                                                ${calendarDate.toLocaleString('default', {
                            year: 'numeric',
                            month: 'long',
                            day: 'numeric'
                        })}
                                            </div>
                                            <div class="main__content-sale-block-item-banner-title" style="display: ${m.banner_title ? 'block' : 'none'}">
                                                ${m.banner_title}
                                            </div>
                                            </div>
                                            <div class="main__content-sale-block-item-wrap ${m.baner_type_2 ? 'translate' : ''}">
                                                <div class="main__content-sale-block-item-main-text">
                                                    ${m.text_1}
                                                </div>
                                                ${m.slider ? `
                                                <div class="main__content-sale-block-item-swiper">
                                                    ${sliderItems}
                                                </div>`
                            : ''}
                                                ${m.slider_1 ? `
                                            <div class="main__content-sale-block-item-swiper">
                                                ${sliderItems1}
                                            </div>
                                            ` : ''}
                                                <div class="main__content-sale-block-item-main-text">
                                                    ${m.text_2}
                                                </div>
                                                ${m.slider_2 ? `
                                            <div class="main__content-sale-block-item-swiper">
                                                ${sliderItems2}
                                            </div>
                                            ` : ''}
                                                ${m.text_3 ? `
                                            <div class="main__content-sale-block-item-main-text">
                                                ${m.text_3}
                                            </div>
                                            ` : ''}
                                            </div>
                                            ${m.timer === undefined ? '' : `
                                            <div class="main__content-sale-block-item-main-end">
                                                <p class="main__content-sale-block-item-main-end-title">
                                                    До конца акции осталось
                                                </p>
                                                <div class="main__content-sale-block-item-main-end-time">
                                                    ${timerItems}
                                                </div>
                                            </div>
                                            `}
                                                <div class="main__content-sale-block-item-main-more">
                                                    <a href="#">
                                                        Подробнее
                                                    </a>
                                                </div>
                                        </div>
                                    `
                    })
                    sliderItems = ``;
                    sliderItems1 = ``;
                    sliderItems2 = ``;
                    timerItems = ``;
                    if (m.timer) {
                        bannerTimer()
                    }

                    function bannerTimer() {
                        let deadLine = new Date(m.timer)
                        // экземпляры классов таймера для баннеров
                        new CountdownTimer(deadLine, (timer) => {
                            let bannerTimerText = document.querySelectorAll('.item_date-count-days-text' + timer.param);
                            let bannerTimerDate = document.querySelectorAll('.item_date-count-days' + timer.param);
                            let bannerTimerTextHours = document.querySelectorAll('.item_date-count-hours-text' + timer.param);
                            let bannerTimerDateHours = document.querySelectorAll('.item_date-count-hours' + timer.param);
                            let bannerTimerDateMinutes = document.querySelectorAll('.item_date-count-minutes' + timer.param);
                            let bannerTimerTextMinutes = document.querySelectorAll('.item_date-count-minutes-text' + timer.param);
                            let bannerTimerDateSeconds = document.querySelectorAll('.item_date-count-seconds' + timer.param)
                            let bannerTimerTextSeconds = document.querySelectorAll('.item_date-count-seconds-text' + timer.param)
                            bannerTimerText.forEach(bannerTimerTextItem => {
                                bannerTimerTextItem.innerHTML = timer.daysTitle
                            })
                            bannerTimerDate[0].innerHTML = timer.days[0]
                            bannerTimerDate[2].innerHTML = timer.days[0]
                            bannerTimerDate[1].innerHTML = timer.days[1]
                            bannerTimerDate[3].innerHTML = timer.days[1]
                            bannerTimerTextHours.forEach(bannerTimerTextHoursItem => {
                                bannerTimerTextHoursItem.innerHTML = timer.hoursTitle
                            })
                            bannerTimerDateHours[0].innerHTML = timer.hours[0]
                            bannerTimerDateHours[2].innerHTML = timer.hours[0]
                            bannerTimerDateHours[1].innerHTML = timer.hours[1]
                            bannerTimerDateHours[3].innerHTML = timer.hours[1]
                            bannerTimerTextMinutes.forEach(bannerTimerTextMinutesItem => {
                                bannerTimerTextMinutesItem.innerHTML = timer.minutesTitle
                            })
                            bannerTimerDateMinutes[0].innerHTML = timer.minutes[0]
                            bannerTimerDateMinutes[2].innerHTML = timer.minutes[0]
                            bannerTimerDateMinutes[1].innerHTML = timer.minutes[1]
                            bannerTimerDateMinutes[3].innerHTML = timer.minutes[1]
                            bannerTimerTextSeconds.forEach(bannerTimerTextSeconds => {
                                bannerTimerTextSeconds.innerHTML = timer.secondsTitle
                            })
                            bannerTimerDateSeconds[0].innerHTML = timer.seconds[0]
                            bannerTimerDateSeconds[2].innerHTML = timer.seconds[0]
                            bannerTimerDateSeconds[1].innerHTML = timer.seconds[1]
                            bannerTimerDateSeconds[3].innerHTML = timer.seconds[1]
                        }, countdownTimerItem, () => {
                        })
                    }
                }
            }
            $(document).ready(function () {
                $(`.main__content-sale-block-item-swiper`).slick({
                    infinite: true,
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    speed: 1000,
                    autoplay: true,
                    autoplaySpeed: 2000,
                })
            })
            const translateBlock = document.querySelectorAll('.translate');
            console.log(translateBlock)
            translateBlock.forEach(item => {
                item.addEventListener('mouseover', (e) => {
                    if (e.currentTarget === item) {
                        clearInterval(interval)
                    }
                })
                item.onmouseleave = () => {
                    interval = setInterval(() => {
                        item.scrollBy({
                            behavior: 'smooth',
                            top: 100,
                            left: 0,
                        })
                    }, 1000)
                }
            })
            let interval = setInterval(() => {
                translateBlock.forEach(item => {
                    item.scrollBy({
                        behavior: 'smooth',
                        top: 100,
                        left: 0,
                    })
                })
            }, 1000)
        })
}

banners('https://developer.itec.by/api/banners/main_page/1/')

function videoSlider(url) {
    fetch(url)
        .then(resp => resp.json())
        .then(res => {
            const videoSliderWrapper = document.querySelector('.video__slider-block-slider-wrapper')
            for (let i of res.results) {
                videoSliderWrapper.innerHTML += `
                                                    <div class="video__slider-block-slider-slide swiper-slide">
                                                        <div class="video__slider-block-slider-slide-wrapper">
                                                        ${i.url}
                                                        </div>
                                                        <div class="video__slider-block-slider-slide-text">
                                                            <p>
                                                                ${i.description}
                                                            </p>
                                                            <p style="display: ${i.description2 ? 'block' : 'none'}">
                                                                ${i.description2}
                                                            </p>
                                                        </div>
                                                    </div>
                                                `
            }
            $(document).ready(function () {
                $('.video__slider-block-slider-wrapper').slick({
                    infinite: true,
                    slidesToShow: 3.5,
                    slidesToScroll: 3,
                    speed: 1000,
                    autoplay: true,
                    autoplaySpeed: 5000,
                    responsive: [{
                        breakpoint: 1920, settings: {
                            slidesToShow: 3, slidesToScroll: 3,
                        }
                    }, {
                        breakpoint: 1024, settings: {
                            slidesToShow: 2, slidesToScroll: 2,
                        }
                    }, {
                        breakpoint: 768, settings: {
                            slidesToShow: 1, slidesToScroll: 1,
                        }
                    }]
                })
            })
        })
}

videoSlider('https://developer.itec.by/api/video_links/')

function socialsSlider(url) {
    fetch(url)
        .then(resp => resp.json())
        .then(res => {
            const socialSliderWrapper = document.querySelector('.social__block-slider-wrapper')
            const socialSliderTitle = document.querySelector('.social__slider-title');
            let firstParagraph = document.createElement('p');
            let secondParagraph = document.createElement('p');
            firstParagraph.textContent = res.results[0].title;
            secondParagraph.textContent = res.results[0].title2;
            socialSliderTitle.append(firstParagraph)
            socialSliderTitle.append(secondParagraph)
            for (let i of res.results[0].social_networks) {
                socialSliderWrapper.innerHTML += `
                                                    <div class="social__block-slider-item">
                                                        <a href="#" class="swiper__slide-wrapper">
                                                            <div class="social__block-slider-item-btn">
                                                                <div class="social__block-slider-item-btn-image">
                                                                    <img src="${i.icon_for_url}" alt="">
                                                                </div>
                                                                <div class="social__block-slider-item-btn-text">
                                                                    Подписаться
                                                                </div>
                                                            </div>
                                                            <div class="social__block-slider-item-img">
                                                                <img src="${i.image}" alt="">
                                                            </div>
                                                        </a>
                                                    </div>
                                                `
            }
            $(document).ready(function () {
                $('.social__block-slider-wrapper').slick({
                    infinite: true,
                    slidesToShow: 3.5,
                    slidesToScroll: 3,
                    speed: 1000,
                    autoplay: true,
                    autoplaySpeed: 5000,
                    responsive: [{
                        breakpoint: 1920, settings: {
                            slidesToShow: 3, slidesToScroll: 3,
                        }
                    }, {
                        breakpoint: 1024, settings: {
                            slidesToShow: 2, slidesToScroll: 2,
                        }
                    }, {
                        breakpoint: 768, settings: {
                            slidesToShow: 1, slidesToScroll: 1,
                        }
                    }]
                })
            })
        })
}

socialsSlider('https://developer.itec.by/api/url_for_social_networks/')

function workSlider() {
    $(document).ready(function () {
        $(`.get__work-slider`).slick({
            infinite: true,
            slidesToShow: 1,
            slidesToScroll: 1,
            speed: 2000,
            autoplay: true,
            rtl: false,
            autoplaySpeed: 2000,
        })
    })
}

workSlider()