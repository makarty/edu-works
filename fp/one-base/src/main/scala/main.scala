// Вариант 10
// Запрещено использовать var-переменные
// Запрещено использовать циклы со счётчиком
// Для форматирования вывода использовать метод formatted или аналогичные способы

import scala.math.{abs, log, pow}
import scala.annotation.tailrec
import scala.io.StdIn.readLine


object Main{
  def main(args: Array[String]): Unit = {
    if (parseDouble(args(0)) == false
      || parseDouble(args(1)) == false
      || parseDouble(args(2)) == false
      || parseDouble(args(3)) == false) {
      println("Ошибка! Недопустимый тип")
      return
    }
    if (abs(args(0).toDouble) >= 1){
    }
    if ((abs(args(0).toDouble) > abs(args(1).toDouble) & args(2).toDouble < 0) |
      (abs(args(0).toDouble) < abs(args(1).toDouble) & args(2).toDouble > 0)){
      println("Ошибка! Неправильный шаг")
      return
    }
    println(args.mkString("Array(", ", ", ")"))
    val t = taylorSeries(args(0).toDouble, args(1).toDouble, 0, args(2).toDouble, args(3).toDouble, List.empty)
    val res = formatResult(t, 0, " x     f(x)      T(x)  Ti\n")
    println(res)
  }

  def parseDouble(s: String) = {
    try {
      Some(s.toDouble)
    } catch {
      case _ => false
    }
  }


  @tailrec
  def taylorSeries(x: Double, xLast: Double, N: Int, dx: Double, error: Double, res: List[Double]): List[Double] = {
    if (abs(x) > abs(xLast)) {
      res
    } else {
      val fx = f(x)
      val (tx, iterations) = taylor(x, N, error, 0, 0)
      val result = res ++: List(x, fx, tx, iterations.toDouble)
      taylorSeries(x + dx, xLast, N + 1, dx, error, result)
    }
  }


  def f(x: Double): Double = {
    val arth = 0.5 * log((1 + x) / (1 - x))
    arth
  }


  @tailrec
  def taylor(x: Double, N: Int, error: Double, acc: Double, iterations: Int): (Double, Int) = {
    val result = pow(x, 2 * N + 1) / (2 * N + 1)
    if (abs(result) < error) {
      (acc, iterations)
    } else {
      taylor(x, N + 1, error, acc + result, iterations + 1)
    }
  }


  @tailrec
  def formatResult(arr: List[Double], iter: Int, result: String, str: String = "%.2f %f %f %d\n"): String = {
    if (iter >= arr.length) {
      result
    } else {
      val res = result + str.format(arr(iter), arr(iter + 1), arr(iter + 2), arr(iter + 3).toInt)
      formatResult(arr, iter + 4, res)
    }
  }
}
