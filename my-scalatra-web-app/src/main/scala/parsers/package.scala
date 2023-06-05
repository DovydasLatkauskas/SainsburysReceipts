package parsers


abstract class Parser(file: String){
    
    def create_receipt(): Receipt
}


case class Receipt(
    name: String = "",
    price: Int = 0,
    unit_price: Int = 0,
    unit_measure: String = "",
    full_name: String = "",
    category: String = "",
    description: String = "",
    product_url: String = "",
    image_url: String = ""
)

class Veryfi(file: String) extends Parser(file) {
    def create_receipt(): Receipt = Receipt(name = "test")

}

