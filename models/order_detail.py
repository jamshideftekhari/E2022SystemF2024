class order_detail():
    def __init__(self, order_id, item_name, quantity, unit_price, country_code,vat_rate, discount_rate):
        self.order_id = order_id
        self.item_name = item_name 
        self.quantity = quantity
        self.unit_price = unit_price
        self.country_code = country_code
        self.vat_rate = vat_rate
        self.discount_rate = discount_rate

    def __str__(self):
        return f"Order ID: {self.order_id}, Item Name: {self.item_name}, Quantity: {self.quantity}, Unit Price: {self.unit_price}, Country Code: {self.country_code}, VAT Rate: {self.vat_rate}, Discount Rate: {self.discount_rate}"    
    
    def to_dict(self):
        return {
            "order_id": self.order_id,
            "item_name": self.item_name,
            "quantity": self.quantity,
            "unit_price": self.unit_price,
            "country_code": self.country_code,
            "vat_rate": self.vat_rate,
            "discount_rate": self.discount_rate
        }   