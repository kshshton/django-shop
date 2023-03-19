const addButtons = document.querySelectorAll('.update-button').forEach(item => {
    item.addEventListener('click', (e) => {
        let productId = e.target.dataset.product;
        let action = e.target.dataset.action;
        console.log('productId: ', productId, 'action: ', action);
        console.log('User: ', user)
        user === 'AnonymousUser' ? addCookieItem(productId, action) : updateUserOrder(productId, action);
    });
})

const updateUserOrder = (productId, action) => {
    const url = '/update_item/'
    console.log('User is logged in, sending data...')

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })
    .then(() => {
        location.reload();
    })
}

const addCookieItem = (productId, action) => {
	console.log('User is not authenticated')

	if (action == 'add') {
		if (cart[productId] == undefined) {
		cart[productId] = {'quantity': 1}
		} else {
			cart[productId]['quantity'] += 1
		}
	}
	if (action == 'remove') {
		cart[productId]['quantity'] -= 1
		if (cart[productId]['quantity'] <= 0) {
			console.log('Item should be deleted')
			delete cart[productId];
		}
	}

	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	location.reload()
}
