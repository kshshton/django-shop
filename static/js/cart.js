const addButtons = document.querySelectorAll('.add-button');

for (let i = 0; i < addButtons.length; i++) {
    addButtons[i].addEventListener('click', function() {
        let itemId = this.dataset.item;
        let action = this.dataset.action;
        console.log('itemId: ', itemId, 'action: ', action);

        if (user === 'AnonymousUser') {
            console.log('Not logged');
        } else {
            console.log('Adding item to ' + user + '\'s cart')
        }
    });
}