function applyStyles() { 
    let text = document.getElementById('textInput').value 
    let output = document.getElementById('outputText') 
    output.innerHTML = text 
 
    if (document.getElementById('bold').checked) { 
        output.style.fontWeight = 'bold' 
    } 
 
    if (document.getElementById('italics').checked) { 
        output.style.fontStyle = 'italic' 
    } 
 
    if (document.getElementById('left').checked) { 
        output.style.textAlign = 'left' 
    }
    
    else if (document.getElementById('right').checked) { 
        output.style.textAlign = 'right' 
    }  
}