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
} else {
    presentBtn.addEventListener('click', () => {
        dropPresentModal.style.display = 'flex';
        dropPresentModal.style.overflowY = 'auto';
        document.body.style.overflow = 'hidden';
    })
    if (window.innerWidth < 1024) {
        dropPresentModal.style.display = 'none'
    } else {
        presentBtn.addEventListener('mouseover', () => {
            presentWrapperHover.style.position = 'absolute';
            presentWrapperHover.style.display = 'block';
            if (window.innerWidth < 1920) {
                presentWrapperHover.style.top = '82px';
            } else {
                presentWrapperHover.style.top = '100px';
            }
            presentWrapperHover.style.right = '270px';
            presentWrapperHover.style.zIndex = '50'
        })
        presentBtn.addEventListener('mouseout', () => {
            presentWrapperHover.style.display = 'none';
        })
        presentWrapperHover.addEventListener('click', () => {
            presentWrapperHover.style.display = 'none';
        })
    }
}
if (window.innerWidth < 480) {
    discountsBtn.forEach(item => {
        item.addEventListener('click', () => {
            salesBtn.classList.toggle('active')
        })
    })
} else {
    discountsBtn.forEach(item => {
        item.addEventListener('click', () => {
            dropDownModal.style.display = 'flex';
            dropDownModal.style.overflowY = 'auto'
            document.body.style.overflowY = 'hidden'
        })
        if (window.innerWidth < 1024) {
            dropDownModal.style.display = 'none'

        } else {
            item.addEventListener('mouseover', () => {
                dropDownModalHover.style.position = 'absolute';
                dropDownModalHover.style.display = 'block';
                if (window.innerWidth < 1920) {
                    dropDownModalHover.style.top = '82px'
                } else {
                    dropDownModalHover.style.top = '100px'
                }
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
    if (e.target === e.currentTarget) {
        dropPresentModal.style.display = 'none';
        document.body.style.overflowY = 'auto'
    }
})
dropDownModal.addEventListener('click', (e) => {
    if (e.target === e.currentTarget) {
        dropDownModal.style.display = 'none';
        document.body.style.overflowY = 'auto'
    }
})

const selectedChoice = document.querySelector('.who__selected-choice'),
    selectedChoiceActive = document.querySelector('.who__selected'),
    occasionChoice = document.querySelector('.occasion__selected-choice'),
    occasionChoiceActive = document.querySelector('.occasion__selected'),
    orderChoice = document.querySelector('.order__selected-choice'),
    orderChoiceActive = document.querySelector('.order__selected'),
    remindChoice = document.querySelector('.remind__selected-choice'),
    remindChoiceActive = document.querySelector('.remind__selected');

function get_presents(url) {
    fetch(url)
        .then(resp => resp.json())
        .then(res => {
            for (let i of res) {
                selectedChoiceActive.innerHTML = `
                                                        ${i.reason_set[0].name}
                                                    `
                occasionChoiceActive.innerHTML = `
                                                        ${i.recipient_set[0].name}
                                                    `
                orderChoiceActive.innerHTML = `
                                                    ${i.present_set[0].name}
                                                `
                remindChoiceActive.innerHTML = `
                                                        ${i.remindfordays_set[0].days}
                                                    `
                for (let j of i.reason_set) {
                    selectedChoice.innerHTML += `
                                                    <li class="selected__choice-item"">
                                                        ${j.name}
                                                    </li>
                                                `
                }
                for (let k of i.recipient_set) {
                    occasionChoice.innerHTML += `
                                                    <li class="selected__choice-item">
                                                        ${k.name}
                                                    </li>
                                                `
                }
                for (let b of i.present_set) {
                    orderChoice.innerHTML += `
                                                    <li class="selected__choice-item">
                                                        ${b.name}
                                                    </li>
                                                `
                }
                for (let t of i.remindfordays_set) {
                    remindChoice.innerHTML += `
                                                    <li class="selected__choice-item">
                                                        ${t.days}
                                                    </li>
                                                `
                }
            }
        })
}

get_presents('https://developer.itec.by/api/presents/get/')

function post_presents(url) {
    const presentForm = document.getElementById('#remindPresentForm'),
        presentName = document.getElementById('#presentFormName'),
        presentEmail = document.getElementById('#presentFormEmail'),
        presentPhone = document.getElementById('#presentFormPhone'),
        presentCalendarDate = document.getElementById('#presentCalendarDate'),
        whoSelected = document.querySelector('.who__selected'),
        occasionSelected = document.querySelector('.occasion__selected'),
        orderSelected = document.querySelector('.order__selected'),
        remindSelected = document.querySelector('.remind__selected');

    presentForm.onsubmit = () => {
    }
    let formData = new FormData();
    formData.append('name', presentName.value);
    formData.append('email', presentEmail.value);
    formData.append('phone', presentPhone.value);
    let dateNewFormat = presentCalendarDate.textContent.trim()
    formData.append('about_present', [{
        'date': dateNewFormat.replace(/[^0-9]/g,'/'),
    }]);
    formData.append('recipient', 1);
    formData.append('reason', 1);
    formData.append('present', 1);
    formData.append('remind_for_days', 1);
    console.log(formData.get('about_present'))
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Cookie': 'csrf'
        },

        body: formData,
    })
        .then(resp => resp.json())
        .then(res => console.log(res))
}
const presentFormBtn = document.querySelector('.present__form-btn')
presentFormBtn.addEventListener('click', () => {
    // post_presents('https://developer.itec.by/api/presents/add/')
    let Data = new FormData();
    // Data.append('name', 'Вася');
    // Data.append('email', 'dsgjskdh@yandex.ru' );
    // Data.append('phone', '+37529243534');
    // // let dateNewFormat = presentCalendarDate.textContent.trim()
    // Data.append('about_present', [{
    //     'date': '19/02/2022',
    // }]);
    // Data.append('recipient', 1);
    // Data.append('reason', 1);
    // Data.append('present', 1);
    // Data.append('remind_for_days', 1);
    // Data.append('remind_every_years', true);
    fetch('https://developer.itec.by/api/presents/add/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: {
            "name": "Вася",
            "email": "user@example.com",
            "phone": "+375448502752",
            "about_present": [
                {
                    "date": "12/02/2022"
                }
            ],
            "recipient": 1,
            "reason": 2,
            "present": 2,
            "remind_for_days": 2,
            "remind_every_years": true
        },
    })
        .then(resp => resp.json())
        .then(res => console.log(res))
})

const firstFormName = document.getElementById('#firstFormName');
const firstFormPhone = document.getElementById('#firstFormPhone');
const firstFormEmail = document.getElementById('#firstFormEmail');
const secondFormName = document.getElementById('#secondFormName')
const secondFormPhone = document.getElementById('#secondFormPhone')
const secondFormEmail = document.getElementById('#secondFormEmail');

firstFormName.oninput = () => {
    firstFormName.value = firstFormName.value.replace(/\s/g, '')
}
firstFormPhone.oninput = () => {
    firstFormPhone.value = firstFormPhone.value.replace(/\s/g, '')
}
firstFormEmail.oninput = () => {
    firstFormEmail.value = firstFormEmail.value.replace(/\s/g, '')
}
secondFormName.oninput = () => {
    secondFormName.value = secondFormName.value.replace(/\s/g, '')
}
secondFormPhone.oninput = () => {
    secondFormPhone.value = secondFormPhone.value.replace(/\s/g, '')
}
secondFormEmail.oninput = () => {
    secondFormEmail.value = secondFormEmail.value.replace(/\s/g, '')
}
