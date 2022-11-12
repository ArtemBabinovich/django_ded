const currentDate = document.querySelectorAll('.current__date'),
    daysWrap = document.querySelectorAll('.calendar__days-wrap'),
    monthPrev = document.querySelectorAll('.month__prev'),
    monthNext = document.querySelectorAll('.month__next'),
    calendarSelected = document.querySelectorAll('.calendar__selected'),
    calendar = document.querySelector('.calendar'),
    calendarSelectedDate = document.querySelectorAll('.calendar__selected-date'),
    calendarDropDownWrap = document.querySelector('.calendar__drop-down-wrap'),
    calendarItem = document.querySelectorAll('.calendar__item'),
    calendarIcon = document.getElementById('#calendarIcon').id,
    abc = document.getElementById('#abc')


// give isActive class
let selectedText;

calendarSelected.forEach(selectedItem => {
    selectedItem.addEventListener('click', (e) => {
        if (e.target.id === calendarIcon){
            calendarDropDownWrap.classList.toggle('dropDownCalendar');
        }
        else {
            calendar.classList.toggle('calendarActive')
            console.log(selectedText)
            selectedText = selectedItem.querySelector('.calendar__selected-date');
        }
    })
})

daysWrap.forEach(daysWrapItem => {
    daysWrapItem.addEventListener('click', (event) => {
        if (event.target.getAttribute('class') === 'days__item'){
            selectedText.innerHTML = `${event.target.innerText.length < 2 ? '0' + event.target.innerText : event.target.innerText }..${currMonth + 1}..${currYear}`;
            calendar.classList.remove('calendarActive')
        } else if (event.target.getAttribute('class') === 'days__item-prevMonth'){
            selectedText.innerHTML = `${event.target.innerText.length < 2 ? '0' + event.target.innerText : event.target.innerText }..${currMonth < 10 ? '0' : ''}${currMonth < 2 ? currMonth + 1 : currMonth}..${currYear}`
            calendar.classList.remove('calendarActive')
        } else if (event.target.getAttribute('class') === 'days__item-nextMonth'){
            selectedText.innerHTML = `${event.target.innerText.length < 2 ? '0' + event.target.innerText : event.target.innerText }..${currMonth < 10 ? '0' : ''}${currMonth + 2 > 12 ? currMonth + 1 : currMonth + 2}..${currYear}`
            calendar.classList.remove('calendarActive')
        }
    })
})
    // calendarItem.forEach(itemCalendar => {
    //     itemCalendar.addEventListener('click', (e) => {
    //         console.log(itemCalendar.children[0])
    //         daysWrap.forEach(daysWrapItem => {
    //             daysWrapItem.addEventListener('click', (event) => {
    //                 let itemPrevMonth = document.querySelectorAll('.days__item-prevMonth')
    //                 itemPrevMonth.forEach(item => {
    //                     if (event.target === item) {
    //                         // `${event.target.innerText.length < 2 ? '0' + event.target.innerText : event.target.innerText }..${currMonth < 10 ? '0' : ''}${currMonth < 2 ? currMonth + 1 : currMonth}..${currYear}`
    //                         calendar.forEach(calendarItem => {
    //                             calendarItem.classList.remove('isActive')
    //                         })
    //                     }
    //                 })
    //                 let itemNextMonth = document.querySelectorAll('.days__item-nextMonth')
    //                 itemNextMonth.forEach(item => {
    //                     if (event.target === item){
    //                         // `${event.target.innerText.length < 2 ? '0' + event.target.innerText : event.target.innerText }..${currMonth < 10 ? '0' : ''}${currMonth + 2 > 12 ? currMonth + 1 : currMonth + 2}..${currYear}`
    //                         calendar.forEach(calendarItem => {
    //                             calendarItem.classList.remove('isActive')
    //                         })
    //                     }
    //                 })
    //                 let itemDays = document.querySelectorAll('.days__item');
    //                 itemDays.forEach(item => {
    //                     if (event.target === item){
    //                         // `${event.target.innerText.length < 2 ? '0' + event.target.innerText : event.target.innerText }..${currMonth + 1}..${currYear}`
    //                         calendar.forEach(calendarItem => {
    //                             calendarItem.classList.remove('isActive')
    //                         })
    //                     }
    //                 })
    //             })
    //         })
    //         if (e.target.id === calendarIcon){
    //             calendarDropDownWrap.classList.toggle('dropDownCalendar')
    //         }else {
    //             itemCalendar.children[1].classList.toggle('calendarActive');
    //         }
    //     })
    // })

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
        liTag += `<li class="days__item-prevMonth">${lastDateOfLastMonth - i + 1}</li>`
    }

    for (let i = 1; i <= lastDateOfMonth ; i++) {
        liTag += `<li class="days__item">${i}</li>`
    }

    for (let i = lastDayOfMonth; i < 7; i++) {
        liTag += `<li class="days__item-nextMonth">${i - lastDayOfMonth + 1}</li>`
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



const dateInSelected = new Date();