//Определите тип данных, представляющий информацию о
//карте в карточной игре. Каждая карта характеризуется одной
//из четырех мастей. Карта может быть младшей (от двойки до
//десятки), либо картинкой (валет, дама, король, туз).
//Определите функции:
//  a. isMinor - проверяет, что её аргумент является младшей
//    картой
//  b. sameSuit - проверяет, что переданные в неё карты -
//    одной масти
//  c. beats - проверяет, что карта, переданная ей в качестве
//    первого аргумента, бьёт карту, являющуюся вторым
//    аргументом
//  d. beats2 - аналогично beats, но принимает третьим
//    аргументом козырную масть
//  e. beatsList - принимает в качестве аргумента список карт,
//    карту и козырную масть; возвращает список карт из
//    первого аргумента, которые бьют указанную карту с
//    учетом козырной масти
//  f. функция, возвращающая по заданному списку карт
//    список чисел, каждое из которых является возможной
//    суммой очков указанных карт, рассчитанных по правилам
//    игры “блэк джек”: младшие карты считаются по номиналу,
//    валет, дама и король - 10 очков, туз может
//    рассматриваться как 11 или как 1 (возвращаются все
//    возможные варианты)
final case class Card(
         value: Int | String,
         suit: String,
){
  private val values = List(2, 3, 4, 5, 6, 7, 8, 9, 10, "валет", "дама", "король", "туз")

  def isMinor(): Boolean =
    if (
      !value.equals("валет") &
      !value.equals("дама") &
      !value.equals("король") &
      !value.equals("туз")
    ) {
      true
    } else {
      false
    }

  def sameSuit(card: Card): Boolean =
    if(this.suit.equals(card.suit)){
      true
    } else {
      false
    }

  def beats(card: Card): Boolean =
    if(values.indexOf(this.value) > values.indexOf(card.value)){
      true
    } else {
      false
    }

  def beats2(card: Card, trumpCard: String): Boolean =
    if (((this.suit.equals(trumpCard) & card.suit.equals(trumpCard)) |
      (!this.suit.equals(trumpCard) & !card.suit.equals(trumpCard))) &
      (values.indexOf(this.value) > values.indexOf(card.value))
    ) {
      true
    } else if(this.suit.equals(trumpCard) & !card.suit.equals(trumpCard)){
      true
    } else {
      false
    }

  def beatsList(): Boolean =
    true
}


object Main {
  def main(args: Array[String]): Unit =
    val threeOfHearts = Card(3, "черви")
    val threeOfSpades = Card(3, "бубны")
    val jackOfHearts = Card("jack", "черви")
    val aceOfSpades = Card("ace", "пики")
    println("Тройка червей младшая карта: " + threeOfHearts.isMinor())
    println("Тройка и туз одной масти: " + threeOfHearts.sameSuit(aceOfSpades))
    println("Туз бьёт тройку : " + aceOfSpades.beats(threeOfHearts))
    println("Тройка пик бьёт тройку червей, козырь - черви: " + threeOfSpades.beats2(threeOfHearts, "черви"))
}
