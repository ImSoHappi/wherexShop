let subTotal = 0
let discount = 0
let iva = 0
let total = 0
let sale = []
let totalAmount = 0

function add_to_cart(item_id) {
    const item = document.getElementById(item_id).closest('.card-body')
    const itemTitle = item.querySelector('.card-title').textContent
    const itemCost = item.querySelector('.price').textContent
    const itemStock = item.querySelector('.stock').textContent.split(' ')[0]
    const cart = document.getElementById('cart')
    const existingItem = cart.querySelector('li.'+ CSS.escape(item_id))

    try {
        if(existingItem.querySelector('h6').textContent === itemTitle) {

            let amount = existingItem.querySelector('input').getAttribute('value')
            amount = Number(amount) + 1
            existingItem.querySelector('input').setAttribute('value', amount)

            indexSale = sale.findIndex((obj => obj.id == item_id))
            sale[indexSale].amount = amount
            document.getElementById('sale').value = JSON.stringify(sale)
            totalAmount = totalAmount + 1
            
        }
    }
    catch{
        const newItem = `
            <li class="list-group-item d-flex justify-content-between lh-sm p-3 ${item_id}">
                <div class="row">
                    <h6 class="my-0 col-8">${itemTitle}</h6> <input type="number" name="" value="1" class="col-4" min="1" max="${itemStock}">
                </div>
                <span class="text-muted">${itemCost}</span>
            </li>
        `
        cart.insertAdjacentHTML('beforeend', newItem)
        sale.push({'id':item_id, 'amount':'1'})
        document.getElementById('sale').value = JSON.stringify(sale)
        totalAmount = totalAmount + 1
    }

    update_prices(itemCost)
}

function update_prices(itemCost) {
    subTotal = subTotal + parseInt(itemCost.replace('$', ''))
    discount = subTotal * 0.10
    iva = (subTotal - discount) * 0.15
    total = subTotal - discount + iva

    document.getElementById('subtotal').innerHTML = subTotal
    document.getElementById('subtot').value = subTotal
    document.getElementById('discount').innerHTML = Math.round(discount)
    document.getElementById('disc').value = Math.round(discount)
    document.getElementById('iva').innerHTML = Math.round(iva)
    document.getElementById('iv').value = Math.round(iva)
    document.getElementById('total').innerHTML = Math.round(total)
    document.getElementById('tot').value = Math.round(total)
    document.getElementById('amountCount').innerHTML = totalAmount
}

