function handleOrderResponse(orderObject){
    console.log(orderObject)
}

function handleInvoiceResponse(invoiceObject){
    console.log(invoiceObject)
}

function saveOrder(order){
    fetch("http://localhost:5000/order/create", {
        method: "post",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
    },
    // Dit voegt de order toe aan de body van de post.
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
    fetch('http://localhost:5000/order/get?orderId=' + orderId)
    .then((response) => response.json())
    .then((responseJSON) => {
        handleOrderResponse(responseJSON);
    });
};

function getInvoice(orderId){
    if (orderId === ''){
        console.log('Please non-blanc argument');
        return null;
    };

    // fetch zonder errorhandling (niet netjes, eventueel aan te passen)
    fetch('http://localhost:5000/order/invoice?orderId=' + orderId)
    .then((response) => response.json())
    .then((responseJSON) => {
        handleInvoiceResponse(responseJSON);
        // hier kun je iets doen met de response. Bijv. een functie aanroepen die 
        // het object op het scherm toont. Gebruik hiervoor de functie handleOrderResponse 
        // deze kan dan de DOM manipuleren.
    });
};


order = new Object();
order.orderId = '123456';
order.wijn = 3;
order.bier = 2;

// De order zul je moeten aanpassen naar een
// 'valide' order, en dus niet meer met het voorbeeld.
// Gebruik hiervoor bijv. de horeca-app.
saveOrder(order);

// aanroep functie haal
//getInvoice('123456');
