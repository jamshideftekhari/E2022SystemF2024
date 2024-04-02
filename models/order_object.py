class order():
    def __init__(self, order_id, item_name, quantity, unit_price, subtotal, vat_price, discount_price, total_price, vat_id, discount_id):
        self.order_id = order_id
        self.product_id = item_name
        self.quantity = quantity
        self.unit_price = unit_price
        self.subtotal = subtotal
        self.vat_price = vat_price
        self.discount_price = discount_price
        self.total_price = total_price
        self.vat_id = vat_id
        self.discount_id = discount_id