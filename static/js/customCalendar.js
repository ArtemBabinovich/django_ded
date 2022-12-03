const currentDate = document.querySelectorAll('.current__date'),
    daysWrap = document.querySelectorAll('.calendar__days-wrap'),
    monthPrev = document.querySelectorAll('.month__prev'),
    monthNext = document.querySelectorAll('.month__next'),
    calendarSelected = document.querySelectorAll('.calendar__selected'),
    calendar = document.querySelectorAll('.calendar'),
    calendarDropDownWrap = document.querySelectorAll('.calendar__drop-down-wrap'),
    calendarIcon = document.getElementById('#calendarIcon').id,
    dateNow = document.querySelectorAll('.date__now'),
    dateNowBtn = document.querySelectorAll('.date__now-btn-now'),
    dateNowClearBtn = document.querySelectorAll('.date__clear-btn'),
    calendarIconMobile = document.getElementById('#calendarIconMobile').id;


// give isActive class
let selectedText;

calendarSelected.forEach(selectedItem => {
    selectedItem.addEventListener('click', (e) => {
        if (e.target.id === calendarIcon || e.target.id === calendarIconMobile){
            calendarDropDownWrap.forEach(item => {
                item.classList.toggle('dropDownCalendar');
            })
        }
        else {
            calendar.forEach(calendarItem => {
                calendarItem.classList.toggle('calendarActive')
            })
            selectedText = selectedItem.querySelector('.calendar__selected-date');
        }
    })
})

daysWrap.forEach(daysWrapItem => {
    daysWrapItem.addEventListener('click', (event) => {
        if (event.target.getAttribute('class') === 'days__item'){
            selectedText.innerHTML = `${event.target.innerText.length < 2 ? '0' + event.target.innerText : event.target.innerText }.${currMonth + 1}.${currYear}`;
            calendar.forEach(calendarItem => {
                calendarItem.classList.remove('calendarActive')
            })
        }
        // else if (event.target.getAttribute('class') === 'days__item-prevMonth'){
        //     selectedText.innerHTML = `${event.target.innerText.length < 2 ? '0' + event.target.innerText : event.target.innerText }.${currMonth < 10 ? '0' : ''}${currMonth < 2 ? currMonth + 1 : currMonth}.${currYear}`
        //     calendar.forEach(calendarItem => {
        //         calendarItem.classList.remove('calendarActive')
        //     })
        // } else if (event.target.getAttribute('class') === 'days__item-nextMonth'){
        //     selectedText.innerHTML = `${event.target.innerText.length < 2 ? '0' + event.target.innerText : event.target.innerText }.${currMonth < 10 ? '0' : ''}${currMonth + 2 > 12 ? currMonth + 1 : currMonth + 2}.${currYear}`
        //     calendar.forEach(calendarItem => {
        //         calendarItem.classList.remove('calendarActive')
        //     })
        // }
    })
})

// getting new date, current year and month
let date = new Date(),
    currYear = date.getFullYear(),
    currMonth = date.getMonth();


const months = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль',
                'Август','Сентябрь','Октябрь','Ноябрь','Декабрь'];

const renderCalendar = () => {
    let firstDateOfMonth = new Date(currYear, currMonth, 0).getDay() // getting first day of month
    let lastDateOfMonth = new Date(currYear, currMonth + 1, 0).getDate() // getting last date of month
    let lastDayOfMonth = new Date(currYear, currMonth, lastDateOfMonth).getDay() // getting last day of month
    let lastDateOfLastMonth = new Date(currYear, currMonth, 0).getDate() // getting last date of previous month
    let liTag = ''

    for (let i = firstDateOfMonth; i > 0 ; i--) {
        liTag += `<li class="days__item-prevMonth"></li>`
        // ${lastDateOfLastMonth - i + 1}
    }

    for (let i = 1; i <= lastDateOfMonth ; i++) {
        liTag += `<li class="days__item">${i}</li>`
    }

    for (let i = lastDayOfMonth; i < 7; i++) {
        liTag += `<li class="days__item-nextMonth"></li>`
        // ${i - lastDayOfMonth + 1}
    }
    currentDate.forEach(item => {
        item.innerText = `${months[currMonth]} ${currYear}`
    })
    daysWrap.forEach(item => {
        item.innerHTML = liTag;
    })
}
renderCalendar()

monthNext.forEach(item => {
    item.addEventListener('click', () => {
        currMonth += 1;
        if (currMonth < 0 || currMonth > 11 ){
            date = new Date(currYear, currMonth)
            currYear = date.getFullYear();
            currMonth = date.getMonth();
        }else {
            date = new Date()
        }
        renderCalendar()
    })
})
monthPrev.forEach(item => {
    item.addEventListener('click', () => {
        currMonth -= 1;
        if (currMonth < 0 || currMonth > 11 ){
            date = new Date(currYear, currMonth)
            currYear = date.getFullYear();
            currMonth = date.getMonth();
        }else {
            date = new Date()
        }
        renderCalendar()
    })
})

let calendarDateNow = new Date();

dateNow.forEach(dateNowItem => {
    dateNowItem.innerHTML = `${calendarDateNow.getDate()}.${calendarDateNow.getMonth() + 1}.${calendarDateNow.getFullYear()}`
})
dateNowBtn.forEach(dateNowBtnItem => {
    dateNowBtnItem.addEventListener('click',() => {
        dateNow.forEach(item => {
            item.innerHTML = `${calendarDateNow.getDate()}.${calendarDateNow.getMonth() + 1}.${calendarDateNow.getFullYear()}`
        })
    })
})
dateNowClearBtn.forEach(dateNowClearBtnItem => {
    dateNowClearBtnItem.addEventListener('click', () => {
        dateNow.forEach(item => {
            item.innerHTML = `00.00.0000`;
        });
    })
})

