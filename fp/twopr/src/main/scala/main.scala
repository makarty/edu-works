// Вариант 10.
// Вернуть номера строк (через пробел), содержащих более N (задается как параметр) пробелов подряд.

import scala.annotation.tailrec
import scala.io.Source


object Main{
  def main(args: Array[String]): Unit = {
    if(args.length < 2){
      println("Справка:\n" +
        "    N        - количество пробелов\n" +
        "    filename - входной файл")
      return
    }
    if(args(0).toIntOption.isEmpty){
      println("Ошибка! Нужно ввести целое число")
      return
    }
    val N = args(0).toInt
    if(N < 0){
      println("Ошибка! Нужно ввести положительное целое число")
      return
    }
    val filename = args(1)
    val file = Source.fromFile(filename)
    val lines = file.getLines().toList
    val result = processing(args(0).toInt, 0, lines.length, lines, List.empty)
    println("Результат: " + result.mkString(", "))
    file.close
  }

  @tailrec
  private def processing(N: Int, item: Int = 0, end: Int, lines: List[String], result: List[Int]): List[Int] = {
    if(item >= end){
      result
    } else {
      if(lines(item).contains(" " * (N + 1))){
        val res = result ++: List(item + 1)
        processing(N, item + 1, end, lines, res)
      } else{
        processing(N, item + 1, end, lines, result)
      }
    }
  }
}
