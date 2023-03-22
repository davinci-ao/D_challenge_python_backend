function handleOrderResponse(orderObject){
    console.log(orderObject)
}

function saveOrder(order){
    fetch("http://localhost:5000/order/create", {
        method: "post",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
    },
    // voeg je order toe aan de body van de POST.
    body: JSON.stringify(order)        
    })
    .then( (response) => { 
        console.log(response)
    });
}

function getOrder(orderId){
    if (orderId === ''){
        console.log('Please non-blanc argument');
        return null;
    };

    // fetch zonder errorhandling (niet netjes, eventueel aan te passen)
    fetch('http://localhost:5000/order/get?orderId='+orderId)
    .then((response) => response.json())
    .then((responseJSON) => {
        handleOrderResponse(responseJSON);
        // hier kun je iets doen met de response. Bijv. een functie aanroepen die 
        // het object op het scherm toont.
    });
};

order = new Object();
order.orderId = 'aap';
order.wijn = 3;
order.bier = 2;
saveOrder(order);
// haal een order op uit de backend
getOrder('12345');
