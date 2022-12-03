const discountsBtn = document.querySelectorAll('.header__discounts-button');
const dropDownModal = document.querySelector('.btn__drop-down-menu');
const presentBtn = document.querySelector('.header__remind-present-button');
const dropPresentModal = document.querySelector('.btn__drop-down-present');
const presentWrapperHover = document.querySelector('.btn__drop-down-present-hover');
const dropDownModalHover = document.querySelector('.btn__drop-down-menu-hover');
const closeModal = document.querySelector('.close__modal')
const presentClose = document.querySelector('.present__close');
const salesBtn = document.getElementById('#salesBtn');
const presentsBtn = document.getElementById('#presentBtn');


salesBtn.style.display = 'none';
// close present modal
presentsBtn.style.display = 'none';
presentClose.addEventListener('click', () => {
    dropPresentModal.style.display = 'none'
    document.body.style.overflowY = 'auto'
})

// close price modal
closeModal.addEventListener('click', () => {
    presentWrapperHover.style.display = 'none';
    dropDownModal.style.display = 'none';
    document.body.style.overflowY = 'auto'
})



if (window.innerWidth < 480) {
    presentBtn.addEventListener('click', () => {
        presentsBtn.classList.toggle('active');
    })
}else {
    presentBtn.addEventListener('click', () => {
        dropPresentModal.style.display = 'flex';
        dropPresentModal.style.overflowY = 'auto';
        document.body.style.overflow = 'hidden';
    })
    if (window.innerWidth < 1024){
        dropPresentModal.style.display = 'none'
    }else {
        presentBtn.addEventListener('mouseover', () => {
            presentWrapperHover.style.position = 'absolute';
            presentWrapperHover.style.display = 'block';
            presentWrapperHover.style.top = '87px';
            presentWrapperHover.style.right = '270px';
            presentWrapperHover.style.zIndex = '50'
        })
        presentBtn.addEventListener('mouseout', () => {
            presentWrapperHover.style.display = 'none'
        })
    }
}
if (window.innerWidth < 480) {
    discountsBtn.forEach(item => {
        item.addEventListener('click', () => {
            salesBtn.classList.toggle('active')
        })
    })
}else {
    discountsBtn.forEach(item => {
        item.addEventListener('click', () => {
            dropDownModal.style.display = 'flex';
            dropDownModal.style.overflowY = 'auto'
            document.body.style.overflowY = 'hidden'
        })
        if (window.innerWidth < 1024){
            dropDownModal.style.display = 'none'

        }else {
            item.addEventListener('mouseover', () => {
                dropDownModalHover.style.position = 'absolute';
                dropDownModalHover.style.display = 'block';
                dropDownModalHover.style.top = '87px';
                dropDownModalHover.style.right = '0px';
                dropDownModalHover.style.zIndex = '50'
            })
            item.addEventListener('mouseout', () => {
                dropDownModalHover.style.display = 'none'
            })
        }
    })
}
dropPresentModal.addEventListener('click', (e) => {
    if (e.target === e.currentTarget){
        dropPresentModal.style.display = 'none';
        document.body.style.overflowY = 'auto'
    }
})
dropDownModal.addEventListener('click', (e) => {
    if (e.target === e.currentTarget){
        dropDownModal.style.display = 'none';
        document.body.style.overflowY = 'auto'
    }
})