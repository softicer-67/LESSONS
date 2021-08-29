const root = document.getElementById('root')

const cart = [
  {name: 'product_1', price: 5}, 
  {name: 'product_2', price: 15},
  {name: 'product_3', price: 34}
]

let sum = 0

if (cart.length === 0) {
  root.textContent = 'Корзина пуста'
} else {
  cart.forEach(el => sum += el.price)
  root.textContent = `В корзине: ${cart.length} товаров на сумму ${sum}`
}