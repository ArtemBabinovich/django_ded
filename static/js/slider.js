const sliderWrapper = document.querySelector('.main__slider-wrapper');
const sliderNext = document.querySelector('.slider__action-next');
const sliderPrev = document.querySelector('.slider__action-prev');
const mainSlider = document.querySelector('.main__slider')
const main = document.querySelector('main')

function get__sliderItem(url) {
    fetch(url)
        .then(resp => resp.json())
        .then(sliderItem => {
            for (let i of sliderItem){
                sliderWrapper.innerHTML += `<div class="slider__item">
                                                <div class="item__image">
                                                    <img src='${i.image}' alt="">
                                                </div>
                                                <div class="container">
                                                    <a href="#" class="slider__item-link" style="color: ${i.color}">
                                                        <p>${i.text}</p>
                                                        ${i.text_2 ? `<span style="color: ${i.color_2}">${i.text_2}</span>`:''}
                                                    </a>
                                                </div>
                                            </div>`
            }
            const mainSliderItem = document.querySelectorAll('.slider__item');
            mainSliderItem.forEach(item => {
                item.style.minWidth = `${sliderWrapper.clientWidth}px`
            })
        })
}
get__sliderItem('http://developer.itec.by/api/foto_slider_base/');
let count = 0;
sliderNext.addEventListener('click', () => {
    if (count === (sliderWrapper.clientWidth * 18) - sliderWrapper.clientWidth){

    }else {
        count += sliderWrapper.clientWidth;
        sliderWrapper.style.transform = `translateX(${-(count)}px)`
    }
})
sliderPrev.addEventListener('click', () => {
    if (count === 0){

    }else {
        count -= sliderWrapper.clientWidth;
        sliderWrapper.style.transform = `translateX(${-count}px)`
    }
})
let sliderInterval = setInterval(() => {
    if (count === (sliderWrapper.clientWidth * 18) - sliderWrapper.clientWidth){
        count = -sliderWrapper.clientWidth;
    }else {
        count += sliderWrapper.clientWidth;
        sliderWrapper.style.transform = `translateX(${-(count)}px)`
    }
},4000)


mainSlider.addEventListener('mousemove', (e) => {
    if (e.currentTarget){
        console.log(e.currentTarget)
        clearInterval(sliderInterval)
    }
})
mainSlider.addEventListener('mouseout', () => {
    console.log(11)
    sliderInterval = setInterval(() => {
        if (count === (sliderWrapper.clientWidth * 18) - sliderWrapper.clientWidth){
            count = -sliderWrapper.clientWidth;
        }else {
            count += sliderWrapper.clientWidth;
            sliderWrapper.style.transform = `translateX(${-(count)}px)`
        }
    },4000);
})

let a = new Audio('./audio/logoMusic.mp3')
console.log(a)