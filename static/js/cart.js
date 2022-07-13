var addButtons = document.getElementsByClassName('add-button');

for (var i = 0; i < addButtons.length; i++) {
    addButtons[i].addEventListener('click', function() {
        var productObjectId = this.dataset.object;
        var action = this.dataset.action;
        console.log('productObjectId: ', productObjectId, 'action: ', action);

        if (user === 'AnonymousUser') {
            addCookieItem(productObjectId, action)
        } else {
            updateUserOrder(productObjectId, action);
        }
    });
}

function updateUserOrder(productObjectId, action) {
    console.log('User is logged in, sending data...')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productObjectId': productObjectId, 'action': action})
    })

    .then((response) => {
        return response.json();
    })

    .then((data) => {
        location.reload()
    });
}

function addCookieItem(productObjectId, action){
	console.log('User is not authenticated')

	if (action == 'add'){
		if (cart[productObjectId] == undefined){
		cart[productObjectId] = {'quantity':1}

		}else{
			cart[productObjectId]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[productObjectId]['quantity'] -= 1

		if (cart[productObjectId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productObjectId];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	location.reload()
}