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

            if (parseInt(amount) < parseInt(itemStock)) {
                amount = parseInt(amount) + 1
                existingItem.querySelector('input').setAttribute('value', amount)
    
                indexSale = sale.findIndex((obj => obj.id == item_id))
                sale[indexSale].amount = amount
                document.getElementById('sale').value = JSON.stringify(sale)
                totalAmount = totalAmount + 1
                update_prices(itemCost, "add")
            } else {
                console.log("Producto sin stock");
            }
            
        }
    }
    catch{
        const newItem = `
            <li class="list-group-item d-flex justify-content-between lh-sm p-3 ${item_id} align-items-center">
                <div>
                    <h6 class="my-0 col-8">${itemTitle}</h6> 
                </div>
                <div class="row align-items-center text-center">

                    <div class="col-3">
                        <i class="fas fa-minus-square fa-lg text-secondary" onclick="remove_item('${item_id}')"></i>
                    </div>

                    <div class="col-6">
                        <input type="number" name="" value="1" class="col-2 form-control-sm" min="1" max="${itemStock}" disabled style="width: 50px;">
                    </div>
                    <div class="col-3">
                        <i class="fas fa-plus-square text-secondary fa-lg" onclick="add_to_cart('${item_id}')"></i>
                    </div>
                        
                </div>
                <span class="text-muted item-price">${itemCost}</span>
            </li>
        `
        cart.insertAdjacentHTML('beforeend', newItem)
        sale.push({'id':item_id, 'amount':'1'})
        document.getElementById('sale').value = JSON.stringify(sale)
        totalAmount = totalAmount + 1
        update_prices(itemCost, "add")
    }

    
}


function remove_item(item_id) {

    const cart = document.getElementById('cart')
    const existingItem = cart.querySelector('li.'+ CSS.escape(item_id))
    const itemCost = existingItem.querySelector('.item-price').textContent
    let amount = existingItem.querySelector('input').getAttribute('value')

    amount = parseInt(amount) - 1
    existingItem.querySelector('input').setAttribute('value', amount)
    indexSale = sale.findIndex((obj => obj.id == item_id))
    sale[indexSale].amount = amount
    document.getElementById('sale').value = JSON.stringify(sale)
    totalAmount = totalAmount - 1

    if (amount = 1) {
        existingItem.remove()
        sale.splice(indexSale, 1)
        if(sale.length == 0) {
            document.getElementById('sale').value = ''
        } else {
            document.getElementById('sale').value = JSON.stringify(sale)
        }
    }

    update_prices(itemCost, 'remove')
}

function update_prices(itemCost, operation) {
    if (operation == "add") {
        subTotal = subTotal + parseInt(itemCost.replace('$', ''))
    } 
    if (operation == "remove") {
        subTotal = subTotal - parseInt(itemCost.replace('$', ''))
    }

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

