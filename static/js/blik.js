
let code;

document.querySelector(".renew-code").addEventListener('click', () => console.log(blikGenerator()));
document.querySelector(".checkout-btn").addEventListener('click', () => code = openForm());
document.querySelectorAll('#verify').forEach(item => {
  item.addEventListener('click', () => {
    verifyData(code);
  });
})

const blikGenerator = () => {
  return "xxxx".replaceAll("x", () => Math.floor(Math.random() * 10));
}

const openForm = () => {
  const code = blikGenerator();
  let incomeTicker = 60;
  document.querySelector(".blik-popup").style.opacity = '1';
  document.querySelector(".blik-popup").style.zIndex = '99';
  console.log(code);

  window.setInterval(() => {
    incomeTicker > 0 ? incomeTicker-- : "00"
    document.getElementById("incomeTicker").innerHTML = "0:" + incomeTicker;
  }, 1000);

  setTimeout(() => window.location.reload(1), 60000);

  return code;
}

const verifyData = (code) => {
  const url = "/order_execute/";
  const blikValue = document.getElementById('blik').value;

  if (blikValue !== code) {
    return;
  }

  alert('Request has been executed');
  fetch(url, {
      method:'GET',
      headers:{
          'Content-Type': 'applicaiton/json',
          'X-CSRFToken': csrftoken,
      }
  }).then(() => window.location.reload())
}
