fetch('http://localhost:5000/').then((response)=>{
    return response.json()
}).then((data)=>{
    console.log(data.data)
}).catch((e)=>{
    console.log(e)
});

fetch('http://localhost:5000/person').then((response)=>{
    return response.json()
}).then((data)=>{
    renderData(data.data)
    console.log(data.data)
}).catch((e)=>{
    console.log(e)
});

function renderData(data){
    nameElem = document.createElement('h2');
    ageElem = document.createElement('p');
    hrElem = document.createElement('hr')

    nameElem.innerText = `${data.firstName} ${data.name}.`;
    ageElem.innerText = `${data.age} jaar.`;

    document.body.appendChild(nameElem);
    document.body.appendChild(ageElem);
    document.body.appendChild(hrElem);
}

