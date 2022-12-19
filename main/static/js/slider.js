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
                let timer = i.time_pause_for_mini_slider
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
                                                        <p class="mini__swiper-tips-text" id="#tipsText">Читать СОВЕТЫ ...</p>
                                                        <div class="mini__swiper-tips-drop">
                                                            <div class="swiper__tips-drop">
                                                                <div class="swiper__tips-drop-title">
                                                                    Обработка фото на заказ без предоплаты
                                                                </div>
                                                                <div class="swiper__tips-drop-sub-title">
                                                                    / не дай себя обмануть /
                                                                </div>
                                                                <div class="swiper__tips-drop-about">
                                                                    <div class="swiper__tips-drop-about-head">
                                                                        ОСТОРОЖНО! БИЗНЕС!
                                                                    </div>
                                                                    <p>
                                                                        Друзья! 
                                                                    </p>
                                                                    <p>
                                                                        Мы живем в эпоху обнаглевших от безнаказанности жуликов.
                                                                    </p>
                                                                    <p>
                                                                        Совет честного от художника.
                                                                    </p>
                                                                    <p>
                                                                        Прежде, чем что-либо заказывать, требуйте доказательства качества услуг.
                                                                    </p>
                                                                    <p>
                                                                        Не позволяйте разводить вас на деньги!
                                                                    </p>
                                                                    <p>
                                                                        Как проверить мастера?
                                                                    </p>
                                                                    <p>
                                                                        Советы от профи на каждой странице сайта!
                                                                    </p>
                                                                </div>
                                                                <div class="swiper__tips-drop-stock-block">
                                                                    <div class="stock__block-title">
                                                                        Акция! Скидки..!!!
                                                                    </div>
                                                                    <p style="color: black">
                                                                        Обработка фото - <span style="color: red">от 100 р.</span>
                                                                    </p>
                                                                    <p style="color: #410000">
                                                                        Официальный договор!
                                                                    </p>
                                                                </div>
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
                                                                        Свернуть ВСЕ ...
                                                                    </div>
                                                                    <div class="swiper__tips-openAllBlock">
                                                                        <div class="swiper__tips-drop-title">
                                                                            Обработка фотографий до и после
                                                                        </div>
                                                                        <div class="swiper__tips-drop-sub-title">
                                                                            /проверь качество - затем заказывай/
                                                                        </div>
                                                                        <div class="swiper__tips-anchor-title">
                                                                            Проверь качество за 100 р.
                                                                        </div>
                                                                        <div class="swiper__tips-drop-about">
                                                                            <p>
                                                                                Как проверить честность мастера и надежность студии в целом?
                                                                            </p>
                                                                            <p>
                                                                                Следуйте пошаговой инструкции: 
                                                                            </p>
                                                                            <ul class="swiper__tips-drop-numericList">
                                                                                <li class="tips-drop-numericListItem">
                                                                                    1. Оставьте Заявку – это ваша прямая связь с мастером.
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    2. Закажите недорогую обработку фото с оплатой не более 500 рублей.
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    3. Прикрепите к Заявке пробную фотографию.
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    4. Согласуйте ваши пожелания через закрытый канал рабочего чата художника.
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    5. Согласовали? Отправьте на карту студии «Сбербанк» аванс – 100 рублей.
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    6. Через 15-30 минут вы получите выполненную на 100% готовую работу:
                                                                                    <p>
                                                                                        - фото будет полностью обработано в соответствии с вашими пожеланиями;
                                                                                    </p>
                                                                                    <p>
                                                                                        - на обработанном изображении будет стоять защитный водяной знак.
                                                                                    </p>
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    7. Проанализируйте результат ДО и ПОСЛЕ редактирования.
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    8. Если результат обработки вам понравился:
                                                                                    <p>
                                                                                        - доплатите оставшуюся, ранее согласованную часть денег;
                                                                                    </p>
                                                                                    <p>
                                                                                        - сразу после получения доплаты защита с изображения будет снята;
                                                                                    </p>
                                                                                    <p>
                                                                                        - ваше фото будет повторно отправлено вам в готовом для печати состоянии.
                                                                                    </p>
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    9. Проверка качества работы мастера завершена.
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    10. Переходите к основному заказу.
                                                                                </li>
                                                                            </ul>
                                                                        </div>
                                                                        <div class="swiper__tips-drop-image">
                                                                            <img src="../img/dropTipsImage.jpg" alt="">
                                                                        </div>
                                                                        <div class="swiper__tips-drop-image-title">
                                                                            РЕСТАВРАЦИЯ ФОТО
                                                                        </div>
                                                                        <div class="swiper__tips-anchor-title">
                                                                            Как все ужасно!
                                                                        </div>
                                                                        <div class="swiper__tips-drop-about">
                                                                            <p>
                                                                                Вам не понравилось?
                                                                            </p>
                                                                            <ul class="swiper__tips-drop-numericList">
                                                                                <li class="tips-drop-numericListItem">
                                                                                    1.  Жаль.
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    2. В этом случае, 100 рублей остаются у мастера. Это самая минимальная компенсация оплаты рабочего времени, потраченного на обработку вашей фотографии.
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    3. Сравните качество обработки с результатом аналогичной работы в другой студии. 
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    4. Проверено 1000 раз! Лучше, дешевле, честнее – никто вам не сделает!
                                                                                </li>
                                                                                <li class="tips-drop-numericListItem">
                                                                                    5. Подумайте ещё раз и обращайтесь снова. Я обид не помню!
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


getSwiperItem('https://developer.itec.by/api/big_slider/','https://developer.itec.by/api/small_slider/','https://developer.itec.by/api/small_slider/')

