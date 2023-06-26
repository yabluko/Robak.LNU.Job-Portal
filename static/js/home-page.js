const divElement = document.querySelectorAll('.leftside__list__li');
console.log(divElement);


divElement.forEach(div => {
    div.addEventListener('click', function handleCliker(event){
        event.currentTarget.style.backgroundColor = '#0073b138';
    });
})