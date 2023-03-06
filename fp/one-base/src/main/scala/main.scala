// Вариант 10
// Запрещено использовать var-переменные
// Запрещено использовать циклы со счётчиком
// Для форматирования вывода использовать метод formatted или аналогичные способы

import scala.math.{pow, abs, log}
import scala.annotation.tailrec
import scala.io.StdIn.readLine
import scala.util.CommandLineParser as CLP


@tailrec
def taylorSeries(x: Double, xLast: Double, N: Int, dx: Double, error: Double, res: List[Double]): List[Double] = {
  if (abs(x) < abs(xLast)){
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


@main
def main(args: Array[String]): Unit = {
  // Добавить проверки
  println(args.mkString("Array(", ", ", ")"))
  val t = taylorSeries(0.9, 0.4, 0, -0.1, 0.000001, List.empty)
  val res = formatResult(t, 0, " x     f(x)      T(x)  Ti\n")
  println(res)
}
