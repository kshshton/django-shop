let code;

document.querySelector(".renew-code").addEventListener('click', () => {
    let code = blikGenerator();
    console.log(code);
});
document.querySelector(".checkout-btn").addEventListener('click', () => {
    openForm()
});
document.getElementById('verify').addEventListener('click', () => {
    verifyData()
});

function openForm() {
    code = blikGenerator();
    console.log(code);
    let incomeTicker = 60;
    document.querySelector(".blik-popup").style.opacity = '1';
    document.querySelector(".blik-popup").style.zIndex = '99';

    window.setInterval(function(){
        if (incomeTicker > 0)
            incomeTicker--;
             document.getElementById("incomeTicker").innerHTML = "0:" + incomeTicker;
       }, 1000);

    setTimeout(() => window.location.reload(1), 60000);
}

function verifyData() {
    const url = "/order_execute/";
    let blikValue = document.getElementById('blik').value;

    if (blikValue == code) {
        alert('Request has been executed');
        fetch(url, {
            method:'GET',
            headers:{
                'Content-Type': 'applicaiton/json',
                'X-CSRFToken': csrftoken,
            }
        }).then(() => window.location.reload())
    }
}

function blikGenerator() {
    let code = "";

    function getRandomInt(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min)) + min;
    }

    for (let i = 0; i < 4; i++) {
        code += getRandomInt(0, 9)
    }

    return code;
}