const mainSwiperWrapper = document.querySelector('.main__swiper-slider');
const miniSlidersWrapper = document.querySelector('.main__content-block-mini-sliders-wrapper');
function getSwiperItem(url,url2,url3) {
    fetch(url2)
        .then(resp => resp.json())
        .then(res => {
            let services = ``;
            for (let i of res.slides){
                for (let j of i.services){
                    services += `
                                <div class="mini__swiper-item swiper-slide">
                                    <div class="mini__swiper-item-image">
                                        <img src="${j.image_for_mini_slider}" alt="${j.image_for_mini_slider}">
                                    </div>
                                    <a href="#" class="mini__swiper-item-text">
                                        <p style="color: ${j.color_service_title}">${j.service_title}</p>
                                        <p style="color: ${j.color_bottom_description};">${j.bottom_description}</p>
                                    </a>
                                </div>
                                `
                }
                miniSlidersWrapper.innerHTML += `
                                                <div class="main__content-block-mini-slider-item" id="${i.url}">
                                                    <div class="mini__slider-title-wrapper">
                                                        <div class="mini__slider-item-title" style="color: ${i.color_title}">
                                                            ${i.title} ${i.additional_title === null ? '' : i.additional_title}
                                                        </div>
                                                        <div class="main__slider-item-sub-title" style="color: ${i.color_title}">
                                                            /${i.additional_title_2 === null ? '' : i.additional_title_2}/
                                                        </div>
                                                    </div>
                                                    <div class="mini__slider-arrow-wrapper">
                                                        <div class="mini__slider-prev">
                                                            <img src="https://developer.itec.by/static/img/icons/miniSliderPrevArrow.svg" alt="">
                                                        </div>
                                                        <div class="mini__slider-next">
                                                            <img src="https://developer.itec.by/static/img/icons/miniSliderNextArrow.svg" alt="">
                                                        </div>
                                                    </div>
                                                    <div class="mini__swiper-container swiper">
                                                        <div class="mini__swiper-wrapper swiper-wrapper">
                                                            ${services}
                                                        </div>
                                                    </div>
                                                    <div class="mini__swiper-tips">
                                                        <p class="mini__swiper-tips-text" id="#tipsText">???????????? ???????????? ...</p>
                                                        <div class="mini__swiper-tips-drop">
                                                            <div class="swiper__tips-drop">
                                                                <div class="swiper__tips-drop-title">
                                                                    ?????????????????? ???????? ???? ?????????? ?????? ????????????????????
                                                                </div>
                                                                <div class="swiper__tips-drop-sub-title">
                                                                    / ???? ?????? ???????? ???????????????? /
                                                                </div>
                                                                <div class="swiper__tips-drop-about">
                                                                    <div class="swiper__tips-drop-about-head">
                                                                        ??????????????????! ????????????!
                                                                    </div>
                                                                    <p>
                                                                        ????????????! 
                                                                    </p>
                                                                    <p>
                                                                        ???? ?????????? ?? ?????????? ?????????????????????? ???? ?????????????????????????????? ??????????????.
                                                                    </p>
                                                                    <p>
                                                                        ?????????? ???????????????? ???? ??????????????????.
                                                                    </p>
                                                                    <p>
                                                                        ????????????, ?????? ??????-???????? ????????????????????, ???????????????? ???????????????????????????? ???????????????? ??????????.
                                                                    </p>
                                                                    <p>
                                                                        ???? ???????????????????? ?????????????????? ?????? ???? ????????????!
                                                                    </p>
                                                                    <p>
                                                                        ?????? ?????????????????? ???????????????
                                                                    </p>
                                                                    <p>
                                                                        ???????????? ???? ?????????? ???? ???????????? ???????????????? ??????????!
                                                                    </p>
                                                                </div>
                                                                <div class="swiper__tips-drop-stock-block">
                                                                    <div class="stock__block-title">
                                                                        ??????????! ????????????..!!!
                                                                    </div>
                                                                    <p style="color: black">
                                                                        ?????????????????? ???????? - <span style="color: red">???? 100 ??.</span>
                                                                    </p>
                                                                    <p style="color: #410000">
                                                                        ?????????????????????? ??????????????!
                                                                    </p>
                                                                </div>
                                                                <div class="swiper__tips-content">
                                                                    <div class="swiper__tips-content-action-wrapper">
                                                                        <div class="swiper__tips-content-title">
                                                                            ????????????????????
                                                                        </div>
                                                                        <div class="swiper__tips-action-collapse">
                                                                            [????????????????]
                                                                        </div>
                                                                        <div class="swiper__tips-action-show">
                                                                            [????????????????]
                                                                        </div>
                                                                    </div>
                                                                    <div class="swiper__tips-anchors">
                                                                        <ul class="swiper__tips-anchors-list">
                                                                            <li class="swiper__tips-anchors-item">
                                                                                <a href="#">
                                                                                    ;dlfagadusflkdjhgksdfjh
                                                                                </a>
                                                                            </li>
                                                                            <li class="swiper__tips-anchors-item">
                                                                                <a href="#">
                                                                                    ;dlfagadu
                                                                                </a>
                                                                            </li>
                                                                            <li class="swiper__tips-anchors-item">
                                                                                <a href="#">
                                                                                    ;dlfagadu
                                                                                </a>
                                                                            </li>
                                                                            <li class="swiper__tips-anchors-item">
                                                                                <a href="#">
                                                                                    ;dlfagadu
                                                                                </a>
                                                                            </li>
                                                                            <li class="swiper__tips-anchors-item">
                                                                                <a href="#">
                                                                                    ;dlfagadu
                                                                                </a>
                                                                            </li>
                                                                            <li class="swiper__tips-anchors-item">
                                                                                <a href="#">
                                                                                    ;dlfagadu
                                                                                </a>
                                                                            </li>
                                                                            <li class="swiper__tips-anchors-item">
                                                                                <a href="#">
                                                                                    ;dlfagadu
                                                                                </a>
                                                                            </li>
                                                                            <li class="swiper__tips-anchors-item">
                                                                                <a href="#">
                                                                                    ;dlfagadu
                                                                                </a>
                                                                            </li>
                                                                            <li class="swiper__tips-anchors-item">
                                                                                <a href="#">
                                                                                    ;dlfagadu
                                                                                </a>
                                                                            </li>
                                                                            <li class="swiper__tips-anchors-item">
                                                                                <a href="#">
                                                                                    ;dlfagadu
                                                                                </a>
                                                                            </li>
                                                                        </ul>
                                                                    </div>
                                                                    <div class="swiper__tips-backAll">
                                                                        <span id="#swiperBackAll">
                                                                            ???????????????? ?????? ...
                                                                        </span>
                                                                    </div>
                                                                    <div class="swiper__tips-openAllBlock">
                                                                        <div class="swiper__tips-drop-title">
                                                                            ?????????????????? ???????????????????? ???? ?? ??????????
                                                                        </div>
                                                                        <div class="swiper__tips-drop-sub-title">
                                                                            /?????????????? ???????????????? - ?????????? ??????????????????/
                                                                        </div>
                                                                        <div class="swiper__tips-anchor-title">
                                                                            ?????????????? ???????????????? ???? 100 ??.
                                                                        </div>
                                                                        <div class="swiper__tips-drop-about">
                                                                            <p>
                                                                                ?????? ?????????????????? ?????????????????? ?????????????? ?? ???????????????????? ???????????? ?? ???????????
                                                                            </p>
                                                                            <p>
                                                                                ???????????????? ?????????????????? ????????????????????: 
                                                                            </p>
                                                                            <ul class="swiper__tips-drop-numericList">
                                                                                <li class="tips-drop-numericListItem">
                                                                                    1. ???????????????? ???????????? ??? ?????? ???????? ???????????? ?????????? ?? ????????????????.
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    2. ???????????????? ?????????????????? ?????????????????? ???????? ?? ?????????????? ???? ?????????? 500 ????????????.
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    3. ???????????????????? ?? ???????????? ?????????????? ????????????????????.
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    4. ???????????????????? ???????? ?????????????????? ?????????? ???????????????? ?????????? ???????????????? ???????? ??????????????????.
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    5. ??????????????????????? ?????????????????? ???? ?????????? ???????????? ???????????????????? ?????????? ??? 100 ????????????.
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    6. ?????????? 15-30 ?????????? ???? ???????????????? ?????????????????????? ???? 100% ?????????????? ????????????:
                                                                                    <p>
                                                                                        - ???????? ?????????? ?????????????????? ???????????????????? ?? ???????????????????????? ?? ???????????? ??????????????????????;
                                                                                    </p>
                                                                                    <p>
                                                                                        - ???? ???????????????????????? ?????????????????????? ?????????? ???????????? ???????????????? ?????????????? ????????.
                                                                                    </p>
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    7. ?????????????????????????????? ?????????????????? ???? ?? ?????????? ????????????????????????????.
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    8. ???????? ?????????????????? ?????????????????? ?????? ????????????????????:
                                                                                    <p>
                                                                                        - ?????????????????? ????????????????????, ?????????? ?????????????????????????? ?????????? ??????????;
                                                                                    </p>
                                                                                    <p>
                                                                                        - ?????????? ?????????? ?????????????????? ?????????????? ???????????? ?? ?????????????????????? ?????????? ??????????;
                                                                                    </p>
                                                                                    <p>
                                                                                        - ???????? ???????? ?????????? ???????????????? ???????????????????? ?????? ?? ?????????????? ?????? ???????????? ??????????????????.
                                                                                    </p>
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    9. ???????????????? ???????????????? ???????????? ?????????????? ??????????????????.
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    10. ???????????????????? ?? ?????????????????? ????????????.
                                                                                </li>
                                                                            </ul>
                                                                        </div>
                                                                        <div class="swiper__tips-drop-image">
                                                                            <img src="../img/dropTipsImage.jpg" alt="">
                                                                        </div>
                                                                        <div class="swiper__tips-drop-image-title">
                                                                            ?????????????????????? ????????
                                                                        </div>
                                                                        <div class="swiper__tips-anchor-title">
                                                                            ?????? ?????? ????????????!
                                                                        </div>
                                                                        <div class="swiper__tips-drop-about">
                                                                            <p>
                                                                                ?????? ???? ???????????????????????
                                                                            </p>
                                                                            <ul class="swiper__tips-drop-numericList">
                                                                                <li class="tips-drop-numericListItem">
                                                                                    1.  ????????.
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    2. ?? ???????? ???????????? 100 ???????????? ???????????????? ?? ??????????????. ?????? ?????????? ?????????????????????? ?????????????????????? ???????????? ???????????????? ??????????????, ???????????????????????? ???? ?????????????????? ?????????? ????????????????????.
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    3. ???????????????? ???????????????? ?????????????????? ?? ?????????????????????? ?????????????????????? ???????????? ?? ???????????? ????????????. 
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    4. ?????????????????? 1000 ??????! ??????????, ??????????????, ?????????????? ??? ?????????? ?????? ???? ??????????????!
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    5. ?????????????????? ?????? ?????? ?? ?????????????????????? ??????????. ?? ???????? ???? ??????????!
                                                                                </li>
                                                                            </ul>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            `
                services = ``
            }
            const miniSwiperTips = document.querySelectorAll('.mini__swiper-tips');
            miniSwiperTips.forEach(item => {
                item.addEventListener('click', (e) => {
                    if (e.target.id === '#tipsText'){
                        // console.log(item.children[1])
                        item.children[1].classList.toggle('tips__active')
                    }
                })
            })
            const miniSwiper = new Swiper ('.mini__swiper-container', {
                simulateTouch: false,
                loop: true,
                autoplay: {
                    delay: res.timer ? res.timer : 4000,
                    disableOnInteraction: false,
                    pauseOnMouseEnter:true,
                },
                navigation: {
                    nextEl: '.mini__slider-next',
                    prevEl: '.mini__slider-prev',
                },
                breakpoints: {
                    1919: {
                        slidesPerView: 3.5
                    },
                    1365: {
                        slidesPerView: 3,
                    },
                    1023: {
                        slidesPerView: 3,
                    },
                    767: {
                        slidesPerView: 2,
                    },
                    480:{
                        slidesPerView: 1.5,
                    },
                    319: {
                        slidesPerView: 1,
                    },
                }
            })
        })
    fetch(url)
        .then(resp => resp.json())
        .then(item => {
            for (let i of item.slides) {
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
            const swiper = new Swiper ('.main__slider-wrapper', {
                pagination: {
                    el:'.swiper-pagination',
                    type: 'bullets',
                    clickable:true,
                },
                loop: true,
                simulateTouch: false,
                navigation: {
                    nextEl: '.slider__action-prev',
                    prevEl: '.slider__action-next',
                },
                slidesPerView: 1,
                autoplay: {
                    delay: item.timer,
                    disableOnInteraction: false,
                    pauseOnMouseEnter:true,
                }
            });
            const mainSliderWrapper = document.querySelector('.main__slider-wrapper');
            const mainSliderImage = document.querySelectorAll('.main__slider-image');
            const zoomWindow = document.querySelector('.main__slider-zoomWindow');
            if (window.innerWidth <= 1024){

            }else {
                mainSliderWrapper.addEventListener('mousemove', (e) => {
                    let src = '';
                    zoomWindow.style.display = 'block'
                    // zoomWindow.style.top = `${e.offsetY - 40}px`
                    // zoomWindow.style.left = `${e.offsetX + 30}px`
                    zoomWindow.style.top = `${e.offsetY - 40}px`
                    zoomWindow.style.left = `${e.offsetX + 100}px`
                    mainSliderImage.forEach(slidesItem => {
                        if (e.target === slidesItem) {
                            src = slidesItem.getAttribute('src')
                        }
                    })
                    let sliderWidth = document.querySelector('.main__slider').clientWidth;
                    zoomWindow.style.background = `url(${src})`;
                    zoomWindow.style.backgroundRepeat = 'no-repeat'
                    zoomWindow.style.backgroundSize = `${sliderWidth}px`;
                    zoomWindow.style.backgroundPositionX = `${-e.offsetX + 45}px`
                    zoomWindow.style.backgroundPositionY = `${-e.offsetY + 40}px`
                    zoomWindow.style.transform = `scale(2.3)`;
                })
                mainSliderWrapper.addEventListener('mouseout', () => {
                    zoomWindow.style.display = 'none'
                })
            }
        })

    fetch(url3)
        .then(resp => resp.json())
        .then(res => {
            const saleBlockWrapper = document.querySelectorAll('.main__content-sale-block-item-wrapper');
            for (let i of res){
                saleBlockWrapper.forEach(item => {
                    item.innerHTML += `
                                                <div class="main__content-sale-block-item">
                                                    <div class="main__content-sale-block-item-time-wrapper">
                                                        <div class="main__content-sale-block-item-time">
                                                            ${i.text}
                                                        </div>
                                                        <div class="main__content-sale-block-item-sub-time" style="${i.calendar ? 'display:block' : 'display:none'}">
                                                            ${i.calendar === null ? '' : i.calendar.banner_calendar}
                                                        </div>
                                                    </div>
                                                    <div class="main__content-sale-block-item-img">
                                                        <div class="main__content-sale-block-item-img-wrapper">
                                                            <img src="${i.url}" alt="">
                                                        </div>
                                                    </div>
                                                </div>
                                            `
                })
            }
            const swiper = new Swiper('.main__content-sale-block-item-swiper', {
                simulateTouch: false,
                autoplay: {
                    delay: 2000,
                    disableOnInteraction: false,
                    pauseOnMouseEnter:true,
                },
                loop:true,
            })

        })
}


getSwiperItem('https://developer.itec.by/api/big_slider/','https://developer.itec.by/api/small_slider/','https://developer.itec.by/api/banners/')

