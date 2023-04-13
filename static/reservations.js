'use strict'

    const getDate = document.querySelector('#select-date')
    getDate.addEventListener("submit", (evt) => {
    evt.preventDefault()
    document.getElementById("emailbox").classList.add("d-none")
    const formInputs = {
        date: document.querySelector('#selected-date').value,
      };
    console.log(formInputs)
    fetch('/showtimes', {
        method: 'post',
        body: JSON.stringify(formInputs),
        headers: {
        'Content-Type': 'application/json'
    }})
    .then((response) => response.json())
    .then((timeData) => {
        console.log(timeData)
        document.getElementById("remove").classList.remove("d-none");
        for (const time of timeData['avaliable']) {
        document.getElementById('times').innerHTML += `<option value=${time}>`
        }
      })
    })

const submittion = document.getElementById("submit-reservation")
submittion.addEventListener("submit", (evt) => {
  evt.preventDefault()
  evt.preventDefault()
    const formInputs = {
        date: document.querySelector('#selected-date').value,
        time: document.querySelector("#time").value,
      };
  console.log(formInputs)
  fetch('/newres', {
    method: 'post',
    body: JSON.stringify(formInputs),
        headers: {
        'Content-Type': 'application/json'
    }})
  .then((response) => response.json())
  .then((resData) => {
    console.log(resData)
  })
})

const showres = document.getElementById("seeres")
showres.addEventListener("click", (evt) => {
  evt.preventDefault()
  fetch('/seeres')
  .then((response) => response.json())
  .then((resData) => {
    console.log(resData)
    for (const res of resData['reservations']){
        document.getElementById('personal_res').innerHTML += `<li> Reservation Date: ${res[0]}   Time: ${res[1]} </li>`
    }
  })
})
