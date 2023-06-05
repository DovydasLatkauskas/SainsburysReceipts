package com.example.app

import org.scalatra._

class MyScalatraServlet extends ScalatraServlet {

  get("/") {
    views.html.hello()
  }
  

  get("/api") {
    "hello v2"
  }
  
}
