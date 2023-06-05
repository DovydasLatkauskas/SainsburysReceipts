package app

import parsers._
import org.scalatra._

// object Main extends App {
//   println("Hello, World!")
//   val a = new Veryfi("").create_receipt()
//   println(a)
// }


class MainServlet extends ScalatraServlet{
    get("/") {
    <html>
      <body>
        <h1>Hello, world!</h1>
        <a href="api">API: return receipt</a>.
      </body>
    </html>
    }


    get("/api") {
      val a = new Veryfi("").create_receipt()
      a.name
    }

}