package com.example.app

import org.scalatra.test.scalatest._

class MyScalatraServletTests extends ScalatraFunSuite {

  addServlet(classOf[MyScalatraServlet], "/*")

  test("GET / on MyScalatraServlet should return status 200") {
    get("/") {
      status should equal (200)
    }
  }

}
