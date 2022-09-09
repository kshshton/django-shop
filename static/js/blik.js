setTimeout(() => window.location.reload(1), 7000);
const url = "/order_execute/"
let code = blikGenerator();
console.log(code);

document.getElementById('verify').addEventListener('click', () => {
    verifyData();
})

function verifyData() {
    let blikValue = document.getElementById('blik').value;

    if (blikValue == code) {
        alert('Payment has been executed');
        fetch(url, {
            method:'GET',
            headers:{
                'Content-Type': 'applicaiton/json',
                'X-CSRFToken': csrftoken,
            }
        }).then(() => location.href = '/products')
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