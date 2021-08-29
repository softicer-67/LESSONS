const root = document.getElementById('root')

let list = []

class Product {
  constructor(name, price, description) {
    this.name = name
    this.price = price
    this.description = description
  }
  
  add() {
    list.push(this)
  }
  
  toHTML() {
    return `
      <div>
        <h1>${this.name}</h1>
        <h2>${this.price}</h2>
        <p>${this.description}</p>
      </div>
    `
  }
}

const car = new Product('BMW', 25000, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
const mac = new Product('Apple', 2700, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
const phone = new Product('iPhone', 900, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')

car.add()
mac.add()
phone.add()

root.innerHTML = list.map(el => el.toHTML()).join('')