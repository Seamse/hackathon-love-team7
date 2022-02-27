const all = document.getElementById('btn-all')
const thrown = document.getElementById('btn-thrown')
const fished = document.getElementById('btn-fished')
const unreplied = document.getElementById('btn-unreply')
const allLinks = document.querySelectorAll('.all')


all.addEventListener('click', () => {
    allLinks.forEach(link => {
        if(link.classList.contains('hidden')){
            link.classList.remove('hidden')
        }
    })
})

thrown.addEventListener('click', () => {
    allLinks.forEach(link => {
        if(link.classList.contains('thrown')){
            link.classList.remove('hidden')
        } else {
            link.classList.add('hidden')
        }
    })
})

fished.addEventListener('click', () => {
    allLinks.forEach(link => {
        if(link.classList.contains('fished')){
            link.classList.remove('hidden')
        } else {
            link.classList.add('hidden')
        }
    })
})

unreplied.addEventListener('click', () => {
    allLinks.forEach((link) => {
        if(link.classList.contains('unreply')){
            link.classList.remove('hidden')
        } else {
            link.classList.add('hidden')
        }
    })
})
