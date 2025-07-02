from typing import List

import product


class order:
    def __init__(self, products, product_no):
        self.products: List['product.product'] = products
        self.product_no: List[int] = product_no
