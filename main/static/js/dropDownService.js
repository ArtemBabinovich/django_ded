const mainServiceBlock = document.querySelector('.main__content-block-service-btn'),
    mainServiceBlockDrop = document.querySelector('.main__content-service-block-btn'),
    mainSaleBlock = document.querySelector('.main__content-block-sale-btn');

mainServiceBlock.addEventListener('click', (e) => {
    if (e.target.tagName === 'P' || e.target === e.currentTarget){
        mainServiceBlockDrop.classList.toggle('mainBtnActive');
    }
})