function addMessage() { 
    let name = document.getElementById('name').value.trim() 
    let message = document.getElementById('message').value.trim() 
 
    let messageContainer = document.createElement('div') 
    messageContainer.classList.add('message') 
 
    let messageHeader = document.createElement('div') 
    messageHeader.textContent = `Имя: ${name}`;
    messageHeader.classList.add('message-header') 
 
    let messageBody = document.createElement('div') 
    messageBody.textContent = message
    messageBody.classList.add('message-body') 
 
    messageContainer.appendChild(messageHeader) 
    messageContainer.appendChild(messageBody) 
 
    let messagesList = document.getElementById('messagesList') 
    messagesList.appendChild(messageContainer) 
 
    
    let date = new Date().toDateString();
    let time = document.createElement('span') 
    time.textContent = ` ${date}` 
    messageHeader.appendChild(time)

    document.getElementById('name').value = '' 
    document.getElementById('message').value = '' 
}