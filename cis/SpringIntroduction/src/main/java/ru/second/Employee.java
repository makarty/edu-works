package ru.second;

public class Employee {
    private Laptop workStation;

    public Employee(Laptop workStation){
        this.workStation = workStation;
    }

    // Метод, выводящий сообщение на основе вызова метода у зависимости
    public void printWorkStation(){
        System.out.println("Я работаю на " + workStation.getName());
    }
}
