const bottles = document.querySelectorAll('.bottle')
const closeLetter = document.querySelectorAll('.throw-btn')

modalOpen = false

bottles.forEach((bottle) => {
  bottle.addEventListener('click', (e) => {
      let letter = e.target.nextElementSibling
      letter.style.display = "flex";
      modalOpen = true
  });
});

closeLetter.forEach(letter => {
  letter.addEventListener('click', (e) => {
    e.target.parentElement.parentElement.parentElement.style.display = "none";
      modalOpen = false

  })
})


function refreshPage(){
  if(modalOpen === false){
  window.location=window.location
  }else {
    setTimeout(refreshPage , 5000);
  }

}

setTimeout(refreshPage , 90000);

// Message variables
const messages = document.getElementById('msg');
const alert = new bootstrap.Alert(messages);

if (messages)
  setTimeout(function () {
    alert.close();
  }, 2500);
