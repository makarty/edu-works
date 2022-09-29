package ru.second;

public class Employee {
    private Laptop workStation;

    public Employee(Laptop workStation){
        this.workStation = workStation;
    }

    public void printWorkStation(){
        System.out.print("Я работаю на " + workStation.getName());
    }
}
