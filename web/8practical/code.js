const time = {
    hour: 0,
    minute: 0
}

const timeNewObj = new Object();
timeNewObj.hour = 0;
timeNewObj.minute = 0;

const timeWithSeconds = Object.create(time);
timeWithSeconds.second = 0;

// Доступ к свойствам объекта на запись
time['hour'] = 16;
timeNewObj.hour = 9;

// Доступ к свойствам объекта на чтение
console.log("Точечная запись"
            + "(time.hour) " + time.hour);
console.log("Квадратные скобки"
            + "(timeNewObj['hour']) " + timeNewObj['hour']);

// Конструктор
function Person(name, surname, age) {
    this.name = name;
    this.surname = surname;
    this.age = age;

    this.getFullName = function () {
        return this.surname + " " + this.name;
    }

    this.sayHello = function () {
        console.log("Привет! Меня зовут " + this.name + ". "
                    + "Мне " + this.age + " лет");
    }
}

let me = new Person("Артём", "Макаров", 19);
me.sayHello();
console.log("Полное имя: " + me.getFullName());

// Расширение Array
Array.prototype.mean = function () {
    let sum = 0;

    for (let item of this) {
        sum += item;
    }

    return sum / this.length;
};

const maxRandom = 25;
const minRandom = 5;
let someRandom = Math.floor(Math.random() * maxRandom) + minRandom;
let someArray = []

for (let i = 0; i < someRandom; i++){
    someArray.push(i);
}

console.log("Элементы массива: "
            + someArray + "\n"
            + "Среднее арифметическое массива: " + someArray.mean());
