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
    const headerNavListMobile = document.querySelector('.header__nav-list-mobile');
    presentBtn.addEventListener('click', () => {
        presentsBtn.classList.toggle('active');
        salesBtn.classList.remove('active')
        if (headerNavListMobile.classList.contains('header__nav-active')) {
            headerNavListMobile.classList.remove('header__nav-active')
        }
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
                presentWrapperHover.style.top = '66px';
            } else {
                presentWrapperHover.style.top = '66px';
            }
            presentWrapperHover.style.right = '255px';
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
    const headerNavListMobile = document.querySelector('.header__nav-list-mobile');
    discountsBtn.forEach(item => {
        item.addEventListener('click', () => {
            salesBtn.classList.toggle('active')
            presentsBtn.classList.remove('active')
            if (headerNavListMobile.classList.contains('header__nav-active')) {
                headerNavListMobile.classList.remove('header__nav-active')
            }
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
                    dropDownModalHover.style.top = '66px'
                } else {
                    dropDownModalHover.style.top = '66px'
                }
                dropDownModalHover.style.right = '0px';
                dropDownModalHover.style.zIndex = '50'
                dropDownModalHover.style.minWidth = '580px'
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

const selectedChoice = document.querySelectorAll('.who__selected-choice'),
    selectedChoiceActive = document.querySelectorAll('.who__selected'),
    occasionChoice = document.querySelectorAll('.occasion__selected-choice'),
    occasionChoiceActive = document.querySelectorAll('.occasion__selected'),
    orderChoice = document.querySelectorAll('.order__selected-choice'),
    orderChoiceActive = document.querySelectorAll('.order__selected'),
    remindChoice = document.querySelectorAll('.remind__selected-choice'),
    remindChoiceActive = document.querySelectorAll('.remind__selected');

function get_presents(url) {
    fetch(url)
        .then(resp => resp.json())
        .then(res => {
            for (let i of res) {
                selectedChoiceActive.forEach(item => {
                    item.innerHTML = `
                                        ${i.reason_set[0].name}
                                    `
                })
                occasionChoiceActive.forEach(item => {
                    item.innerHTML = `
                                                        ${i.recipient_set[0].name}
                                                    `
                })
                orderChoiceActive.forEach(item => {
                    item.innerHTML = `
                                                    ${i.present_set[0].name}
                                                `
                })
                remindChoiceActive.forEach(item => {
                    item.innerHTML = `
                                                        ${i.remindfordays_set[0].days}
                                                    `
                })
                remindChoiceActive
                for (let j of i.reason_set) {
                    selectedChoice.forEach(item => {
                        item.innerHTML += `
                                                    <li class="selected__choice-item"">
                                                        ${j.name}
                                                    </li>
                                                `
                    })
                }
                for (let k of i.recipient_set) {
                    occasionChoice.forEach(item => {
                        item.innerHTML += `
                                                    <li class="selected__choice-item">
                                                        ${k.name}
                                                    </li>
                                                `
                    })
                }
                for (let b of i.present_set) {
                    orderChoice.forEach(item => {
                        item.innerHTML += `
                                                    <li class="selected__choice-item">
                                                        ${b.name}
                                                    </li>
                                                `
                    })
                }
                for (let t of i.remindfordays_set) {
                    remindChoice.forEach(item => {
                        item.innerHTML += `
                                                    <li class="selected__choice-item">
                                                        ${t.days}
                                                    </li>
                                                `
                    })
                }
            }
        })
}

get_presents('https://developer.itec.by/api/presents/get/')

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const presentName = document.getElementById('#presentFormName');
const presentEmail = document.getElementById('#presentFormEmail');
const presentPhone = document.getElementById('#presentFormPhone');
presentPhone.oninput = () => {
    if(presentPhone.value.length === 2) {
        presentPhone.value += ' /'
    }
    if(presentPhone.value.length === 7){
        presentPhone.value += '/ '
    }
    if(presentPhone.value.length === 12){
        presentPhone.value += ' '
    }
    if(presentPhone.value.length === 15){
        presentPhone.value += ' '
    }
    console.log(presentPhone.value.length, presentPhone.value)

    // presentPhone.value = presentPhone.value.replace(/\s/g, '')
}
presentEmail.oninput = () => {
    presentEmail.value = presentEmail.value.replace(/\s/g, '')
}

function post_presents(url) {
    const presentForm = document.getElementById('#remindPresentForm'),
        presentCalendarDate = document.getElementById('#presentCalendarDate'),
        whoSelected = document.querySelector('.who__selected'),
        occasionSelected = document.querySelector('.occasion__selected'),
        orderSelected = document.querySelector('.order__selected'),
        remindSelected = document.querySelector('.remind__selected');
    let dateNewFormat = presentCalendarDate.textContent.trim()
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },

        body: JSON.stringify(
            {
                "name": presentName.value.trim(),
                "email": presentEmail.value.trim(),
                "phone": presentPhone.value.trim(),
                "about_present": [
                    {
                        "date": dateNewFormat.replace(/[^0-9]/g, '/')
                    }
                ],
                "recipient": whoSelected.textContent.trim(),
                "reason": occasionSelected.textContent.trim(),
                "present": orderSelected.textContent.trim(),
                "remind_for_days": remindSelected.textContent.trim(),
                "remind_every_years": true
            }
        ),
    })
        .then(resp => resp.json())
        .then(res => console.log(res))
}

const presentFormBtn = document.querySelector('.present__form-btn')
presentFormBtn.addEventListener('click', () => {
    post_presents('https://developer.itec.by/api/presents/add/')

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

function post_sale(url) {
    if (secondFormEmail.value === firstFormEmail) {
        secondFormEmail.style.border = '1px solid red'
        firstFormEmail.style.border = '1px solid red'
    } else if (firstFormPhone.value === secondFormPhone.value) {
        firstFormPhone.style.border = '1px solid red'
        secondFormPhone.style.border = '1px solid red'
    } else {
        secondFormEmail.style.border = '1px solid white'
        firstFormEmail.style.border = '1px solid white'
        firstFormPhone.style.border = '1px solid white'
        secondFormPhone.style.border = '1px solid white'
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },

            body: JSON.stringify(
                {
                    name: firstFormName.value,
                    phone: firstFormPhone.value,
                    email: firstFormEmail.value,
                    friends_name: secondFormName.value,
                    friends_phone: secondFormPhone.value,
                    friends_email: secondFormEmail.value,
                }
            ),
        })
            .then(resp => resp.json())
            .then(res => console.log(res))
    }
}

const saleBtnPost = document.querySelector('.secondBlock__form-btn');
saleBtnPost.addEventListener('click', () => {
    post_sale('https://developer.itec.by/api/discont/add/')
})