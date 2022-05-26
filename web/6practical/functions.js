/**
 * Сколько раз в последовательности встречается заданное число
 *
 * @param sequence - последовательность чисел
 * @param number - заданное число
 * @returns {number}
 */
function numCounter(sequence, number) {
    let result = 0;

    for (let item of sequence) {
        if (item == number)
            result += 1;
    }

    return result;
}

/**
 * Среднее арифметическое последовательности
 *
 * @param sequence - последовательность чисел
 * @returns {number}
 */
function arithmeticMean(sequence) {
    let result = 0;
    let quantity = sequence.length;

    for (let item of sequence) {
        result += item;
    }

    result = result / quantity;

    return result;
}

/**
 * Сколько нулей в последовательности
 *
 * @param sequence - последовательность чисел
 * @returns {number}
 */
function zeroCounter(sequence){
    let zero_count = 0;

    for (let item of sequence) {
        if (item == 0)
            zero_count++;
    }

    return zero_count;
}
