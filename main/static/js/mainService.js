const serviceBlockWrapper = document.querySelectorAll('.main__content-service-block-wrapper')


function get__services(url) {
    fetch(url)
        .then(resp => resp.json())
        .then(res => {
            let serviceItem = ``;
            for (let i of res.data){
                for (let j of i.services){
                    serviceItem += `<li class="service__block-list-item">
                                        <div class="service__block-list-item-hit" style="display: ${j.marker === null ? 'none' : 'flex'}">
                                            ${j.marker}
                                        </div>
                                        <a href="${i.url}">
                                            ${j.service_title}
                                        </a>
                                    </li>`
                }
                serviceBlockWrapper.forEach(item => {
                item.innerHTML += `<div class="service__block-item">
                                                        <div class="service__block-item-title">
                                                            ${i.title}
                                                            ${i.additional_title === null ? '' : i.additional_title }
                                                        </div>
                                                        <ul class="service__block-item-list">
                                                            ${i.services.length === 0 ? '' : serviceItem}
                                                        </ul>
                                                    </div>`
                })
                serviceItem = '';
            }

        })
}
get__services('https://developer.itec.by/api/block_services/')

