const discountsBtn = document.querySelectorAll('.header__discounts-button');
const dropDownModal = document.querySelector('.btn__drop-down-menu');
const remindBtn = document.querySelector('.header__remind-present-button');
const dropRemindModal = document.querySelector('.btn__drop-down-present');

remindBtn.addEventListener('click', () => {
    dropRemindModal.classList.toggle('btn__drop-down-present-active')
})

discountsBtn.forEach(item => {
    item.addEventListener('click', () => {
        dropDownModal.classList.toggle('btn__drop-down-menu-active')
    })
})