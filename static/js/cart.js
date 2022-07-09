const addButtons = document.querySelectorAll('.add-button');

for (let i = 0; i < addButtons.length; i++) {
    addButtons[i].addEventListener('click', function() {
        let itemId = this.dataset.item;
        let action = this.dataset.action;
        console.log('itemId: ', itemId, 'action: ', action);

        if (user === 'AnonymousUser') {
            console.log('Not logged');
        } else {
            updateUserOrder(itemId, action);
        }
    });
}

function updateUserOrder(itemId, action) {
    console.log('User is logged in, sending data...')

    const url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'itemId': itemId, 'action': action})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data: ', data)
    })
}