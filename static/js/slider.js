const mainSwiperWrapper = document.querySelector('.swiper-wrapper');


function getSwiperItem(url) {
    fetch(url)
        .then(resp => resp.json())
        .then(item => {
            for (let i of item) {
                mainSwiperWrapper.innerHTML += `<div class="main__slider-slide swiper-slide">
                                                    <div class="main__slider-slide-image">
                                                        <img class="main__slider-image" src='${i.image}' alt="">
                                                    </div>
                                                    <div class="container">
                                                        <a href="#" class="main__slider-slide-link">
                                                            <p style="color: ${i.color}">
                                                                ${i.text}
                                                            </p>
                                                            <p style="color: ${i.color_2 ? i.color_2 : i.color};">
                                                                ${i.text_2 ? i.text_2 : ''}
                                                            </p>
                                                        </a>
                                                    </div>
                                            </div>`
            }
            const swiper = new Swiper ('.swiper', {
                pagination: {
                    el:'.swiper-pagination',
                    type: 'bullets',
                    clickable:true,
                },
                loop: true,
                simulateTouch: false,
                navigation: {
                    nextEl: '.slider__action-next',
                    prevEl: '.slider__action-prev',
                },
                slidesPevView: 1,
                autoplay: {
                    delay: 2000,
                    disableOnInteraction: false,
                    pauseOnMouseEnter:true,
                }
            });
            const mainSliderWrapper = document.querySelector('.main__slider-wrapper');
            const mainSliderImage = document.querySelectorAll('.main__slider-image');
            const zoomWindow = document.querySelector('.main__slider-zoomWindow');
            mainSliderWrapper.addEventListener('mousemove', (e) => {
                let src = '';
                zoomWindow.style.display = 'block'
                zoomWindow.style.top = `${e.offsetY - 40}px`
                zoomWindow.style.left = `${e.offsetX + 30}px`
                // console.log(e.offsetY, e.offsetX)
                mainSliderImage.forEach(slidesItem => {
                    if (e.target === slidesItem) {
                        src = slidesItem.getAttribute('src')
                        // console.log(src)
                    }
                })
                zoomWindow.style.background = `url(${src})`;
                zoomWindow.style.backgroundRepeat = 'no-repeat'
                zoomWindow.style.backgroundSize = `${window.innerWidth}px`;
                zoomWindow.style.backgroundPositionX = `${-e.offsetX}px`
                zoomWindow.style.backgroundPositionY = `${-e.offsetY}px`
            })
            mainSliderWrapper.addEventListener('mouseout', () => {
                zoomWindow.style.display = 'none'
            })
        })
}


getSwiperItem('https://developer.itec.by/api/foto_slider_base/')
