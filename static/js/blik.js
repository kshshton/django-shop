document.querySelector(".renew-code").addEventListener('click', () => console.log(blikGenerator()));
document.querySelector(".checkout-btn").addEventListener('click', () => code = openForm());
document.querySelectorAll('#verify').forEach(item => {
    item.addEventListener('click', () => {
        verifyData(code);
    });
})
let code;

const openForm = _ => {
    const code = blikGenerator();
    let incomeTicker = 60;
    document.querySelector(".blik-popup").style.opacity = '1';
    document.querySelector(".blik-popup").style.zIndex = '99';
    console.log(code);

    window.setInterval(() => {
        if (incomeTicker > 0)
            incomeTicker--;
             document.getElementById("incomeTicker").innerHTML = "0:" + incomeTicker;
       }, 1000);

    setTimeout(() => window.location.reload(1), 60000);

    return code;
}

const verifyData = code => {
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

const blikGenerator = _ => {
    let code = "";

    const getRandomInt = (min, max) => {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min)) + min;
    }

    for (let i = 0; i < 4; i++) {
        code += getRandomInt(0, 9)
    }

    return code;
}
