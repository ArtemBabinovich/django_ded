const select = document.querySelectorAll('.form__who-select');
const selectList = document.querySelectorAll('.who__selected-choice');
const selected = document.querySelectorAll('.who__selected');
select.forEach(selectItem => {
    selectItem.addEventListener('click', (e) => {
        selectList.forEach(selectListItem => {
            selectListItem.classList.toggle('selectActive');
            if (selectListItem.classList.contains('selectActive')){
                occasionSelectedChoice.forEach(occasionSelectedChoiceItem => {
                    occasionSelectedChoiceItem.classList.remove('selectActive');
                })
                orderSelectedChoice.forEach(orderSelectedChoiceItem => {
                    orderSelectedChoiceItem.classList.remove('selectActive');
                })
                remindSelectedChoice.forEach(remindSelectedChoiceItem => {
                    remindSelectedChoiceItem.classList.remove('selectActive');
                })
            }
        })
        let text;
        if (e.target.tagName === 'LI'){
            text = e.target.innerText.trim()
            selected.forEach(selectedItem => {
                selectedItem.innerText = text;
            })
        }
    })
})

const occasionSelect = document.querySelectorAll('.form__occasion-select');
const occasionSelected = document.querySelectorAll('.occasion__selected');
const occasionSelectedChoice = document.querySelectorAll('.occasion__selected-choice');
occasionSelect.forEach(occasionItem => {
    occasionItem.addEventListener('click', (e) => {
        occasionSelectedChoice.forEach(occasionSelectedChoiceItem => {
            occasionSelectedChoiceItem.classList.toggle('selectActive');
            if (occasionSelectedChoiceItem.classList.contains('selectActive')){
                selectList.forEach(selectListItem => {
                    selectListItem.classList.remove('selectActive');
                })
                orderSelectedChoice.forEach(orderSelectedChoiceItem => {
                    orderSelectedChoiceItem.classList.remove('selectActive');
                })
                remindSelectedChoice.forEach(remindSelectedChoiceItem => {
                    remindSelectedChoiceItem.classList.remove('selectActive');
                })
            }
        })
        let text;
        if (e.target.tagName === 'LI'){
            text = e.target.innerText.trim()
            occasionSelected.forEach(occasionSelectedItem => {
                occasionSelectedItem.innerText = text;
            })
        }
    })
})

const orderSelect = document.querySelectorAll('.form__order-select');
const orderSelected = document.querySelectorAll('.order__selected');
const orderSelectedChoice = document.querySelectorAll('.order__selected-choice');

orderSelect.forEach(orderSelectItem => {
    orderSelectItem.addEventListener('click', (e) => {
        orderSelectedChoice.forEach(orderSelectedChoiceItem => {
            orderSelectedChoiceItem.classList.toggle('selectActive');
            if (orderSelectedChoiceItem.classList.contains('selectActive')){
                selectList.forEach(selectListItem => {
                    selectListItem.classList.remove('selectActive');
                })
                occasionSelectedChoice.forEach(occasionSelectedChoiceItem => {
                    occasionSelectedChoiceItem.classList.remove('selectActive');
                })
                remindSelectedChoice.forEach(remindSelectedChoiceItem => {
                    remindSelectedChoiceItem.classList.remove('selectActive');
                })
            }
        })
        let text;
        if (e.target.tagName === 'LI'){
            text = e.target.innerText.trim()
            orderSelected.forEach(orderSelectedItem => {
                orderSelectedItem.innerText = text;
            })
        }
    })

})

const remindSelect = document.querySelectorAll('.form__remind-select');
const remindSelected = document.querySelectorAll('.remind__selected');
const remindSelectedChoice = document.querySelectorAll('.remind__selected-choice');

remindSelect.forEach(remindSelectItem => {
    remindSelectItem.addEventListener('click', (e) => {
        remindSelectedChoice.forEach(remindSelectedChoiceItem => {
            remindSelectedChoiceItem.classList.toggle('selectActive');
            if (remindSelectedChoiceItem.classList.contains('selectActive')){
                selectList.forEach(selectListItem => {
                    selectListItem.classList.remove('selectActive');
                })
                orderSelectedChoice.forEach(orderSelectedChoiceItem => {
                    orderSelectedChoiceItem.classList.remove('selectActive');
                })
                occasionSelectedChoice.forEach(occasionSelectedChoiceItem => {
                    occasionSelectedChoiceItem.classList.remove('selectActive');
                })
            }
        })
        let text;
        if (e.target.tagName === 'LI'){
            text = e.target.innerText.trim()
            remindSelected.forEach(remindSelectedItem => {
                remindSelectedItem.innerText = text;
            })
        }
    })
})