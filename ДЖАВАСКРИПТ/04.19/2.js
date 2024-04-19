// let button = document.querySelector("#btn")
// let div = document.querySelector("#main")


// button.addEventListener("click", function(event){
//     for(let i = -200; i < 0; i++){
//         setTimeout(() => { div.style.marginLeft = `${i}px`, 10; }, 100);  
//     }
// })


class BankAccount{
    constructor(owner, balance = 0){ 
        this.owner = owner 
        this.balance = balance 
    }

    deposit(amount){ 
        this.balance += amount 
        if (amount > 0){ 
            console.log("нелья") 
        } 
    }

    withdraw(amount){ 
        this.balance -= amount 
        if (amount > this.balance){ 
            console.log("нет денег") 
        } 
    } 
}

let as = new BankAccount("я")

as.deposit(-1)
as.withdraw(0)