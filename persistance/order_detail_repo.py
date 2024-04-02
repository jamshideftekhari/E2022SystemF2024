class OrderDetailRepository:
    def __init__(self):
        self.order_details = []

    def add_order_detail(self, order_detail):
        self.order_details.append(order_detail)

    def get_order_detail_by_order_number(self, order_number):
        for order_detail in self.order_details:
            if order_detail.order_number == order_number:
                return order_detail
        return None

    def update_order_detail(self, order_number, new_order_detail):
        for i, order_detail in enumerate(self.order_details):
            if order_detail.order_number == order_number:
                self.order_details[i] = new_order_detail
                return True
        return False

    def delete_order_detail(self, order_number):
        for i, order_detail in enumerate(self.order_details):
            if order_detail.order_number == order_number:
                del self.order_details[i]
                return True
        return False

    def get_all_order_details(self):
        return self.order_details
