document.addEventListener('DOMContentLoaded', function () {
    const quickViewButtons = document.querySelectorAll('.quick-view-button');
    const modal = document.getElementById('product-modal');
    const closeButton = document.querySelector('.custom-close-button');
    const cartIcon = document.getElementById('cart-icon');
    const cartSidebar = document.getElementById('cart-sidebar');
    const closeCart = document.querySelector('.close-cart');

    const isFeaturesPage = document.body.classList.contains('features-page');
    if (isFeaturesPage) {
        if (cartIcon) {
            cartIcon.style.pointerEvents = 'none';
        }
        setupQuantityButtons();
    } else {
        if (cartIcon) {
            cartIcon.addEventListener('click', function () {
                cartSidebar.style.width = '300px';
                fetchCartItems();
            });
        }
    }

    if (quickViewButtons.length > 0) {
        quickViewButtons.forEach(button => {
            button.addEventListener('click', function () {
                const productId = button.getAttribute('data-id');
                fetch(`/product/${productId}`)
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Network response was not ok');
                        }
                        return response.json();
                    })
                    .then(product => {
                        document.getElementById('modal-image').src = product.product_picture_url;
                        document.getElementById('modal-name').innerText = product.product_name;
                        document.getElementById('modal-price').innerText = `${product.product_price}₺`;
                        document.getElementById('modal-description').innerText = product.product_description;
                        document.querySelector('.btn-primary').dataset.id = product.product_id;
                        modal.style.display = 'block';
                    })
                    .catch(error => {
                        console.error('There has been a problem with your fetch operation:', error);
                    });
            });
        });
    }

    if (closeButton) {
        closeButton.addEventListener('click', function () {
            modal.style.display = 'none';
        });
    }

    if (window) {
        window.addEventListener('click', function (event) {
            if (event.target === modal) {
                modal.style.display = 'none';
            }
        });
    }

    const addToCartButton = document.querySelector('.btn-primary');
    if (addToCartButton) {
        addToCartButton.addEventListener('click', function () {
            const productId = this.dataset.id;
            const quantity = document.getElementById('modal-quantity').value;

            fetch('/add_to_cart', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrf_token')  // Assuming you're using Flask-WTF for CSRF protection
                },
                body: JSON.stringify({ product_id: productId, quantity: quantity })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    modal.style.display = 'none';
                    updateCartCount();
                    if (cartSidebar.style.width !== '0px') {
                        fetchCartItems();
                    }
                } else {
                    alert('Failed to add item to cart.');
                }
            });
        });
    }

    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    if (addToCartButtons.length > 0) {
        addToCartButtons.forEach(button => {
            button.addEventListener('click', function () {
                const productId = button.closest('.product-card').querySelector('.quick-view-button').dataset.id;
                const quantity = 1; // Default quantity for direct add-to-cart button

                fetch('/add_to_cart', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrf_token')  // Assuming you're using Flask-WTF for CSRF protection
                    },
                    body: JSON.stringify({ product_id: productId, quantity: quantity })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        updateCartCount();
                        if (cartSidebar.style.width !== '0px') {
                            fetchCartItems();
                        }
                    } else {
                        alert('Failed to add item to cart.');
                    }
                });
            });
        });
    }

    if (closeCart) {
        closeCart.addEventListener('click', function () {
            cartSidebar.style.width = '0';
        });
    }

    function fetchCartItems() {
        fetch('/cart_items')
            .then(response => response.json())
            .then(data => {
                const cartBody = document.querySelector('.cart-body');
                cartBody.innerHTML = '';
                let totalPrice = 0;

                data.cart_items.forEach(item => {
                    const itemDiv = document.createElement('div');
                    itemDiv.className = 'cart-item';
                    itemDiv.innerHTML = `
                        <div class="cart-item-content">
                            <img src="${item.product_picture_url}" alt="${item.product_name}" class="cart-item-image">
                            <div>
                                <p>${item.product_name} - ${item.quantity} x ${item.product_price}₺</p>
                                <div class="quantity-controls">
                                    <button class="quantity-decrease" data-id="${item.product_id}">-</button>
                                    <span>${item.quantity}</span>
                                    <button class="quantity-increase" data-id="${item.product_id}">+</button>
                                </div>
                            </div>
                        </div>
                    `;
                    cartBody.appendChild(itemDiv);
                    totalPrice += item.total_price;
                });

                document.getElementById('total-price').innerText = totalPrice;

                setupQuantityButtons();
            });
    }

    function updateCartQuantity(productId, change) {
        fetch('/update_cart_quantity', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrf_token')  
            },
            body: JSON.stringify({ product_id: productId, change: change })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Update the UI directly for the features page
                if (isFeaturesPage) {
                    const itemElement = document.querySelector(`.cart-item .quantity-controls [data-id="${productId}"]`).parentElement;
                    const quantityElement = itemElement.querySelector('span');
                    const productNameElement = itemElement.previousElementSibling;
                    const productPrice = parseFloat(productNameElement.innerText.split(' x ')[1].replace('₺', ''));
                    let newQuantity = parseInt(quantityElement.innerText) + change;

                    if (newQuantity <= 0) {
                        newQuantity = 0;
                        itemElement.closest('.cart-item').remove();
                    } else {
                        quantityElement.innerText = newQuantity;
                    }

                    // Update product name element to reflect the new total quantity and price for this product
                    productNameElement.innerHTML = `${productNameElement.innerText.split(' - ')[0]} - ${newQuantity} x ${productPrice}₺`;

                    let totalElement = document.getElementById('total-price');
                    let totalPrice = parseFloat(totalElement.innerText);
                    totalPrice += (change * productPrice);
                    totalElement.innerText = totalPrice.toFixed(2);
                } else {
                    fetchCartItems();
                }
                updateCartCount();
            } else {
                alert('Failed to update cart quantity.');
            }
        });
    }

    function updateCartCount() {
        const cartCount = document.querySelector('.cart-count');
        fetch('/cart_items')
            .then(response => response.json())
            .then(data => {
                cartCount.innerText = data.cart_items.length;
            });
    }

    function setupQuantityButtons() {
        const quantityDecreaseButtons = document.querySelectorAll('.quantity-decrease');
        if (quantityDecreaseButtons.length > 0) {
            quantityDecreaseButtons.forEach(button => {
                button.addEventListener('click', function () {
                    updateCartQuantity(this.dataset.id, -1);
                });
            });
        }

        const quantityIncreaseButtons = document.querySelectorAll('.quantity-increase');
        if (quantityIncreaseButtons.length > 0) {
            quantityIncreaseButtons.forEach(button => {
                button.addEventListener('click', function () {
                    updateCartQuantity(this.dataset.id, 1);
                });
            });
        }
    }

    // Helper function to get CSRF token from cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});

