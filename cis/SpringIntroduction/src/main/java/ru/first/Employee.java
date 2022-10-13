package ru.first;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;


@Component
public class Employee {
    private ru.first.Tablet workStation;

    // Внедрение зависимости по ссылке через конструктор
    @Autowired
    public Employee(Tablet workStation){
        this.workStation = workStation;
    }

    @PostConstruct
    public void init(){
        System.out.println("Employee: я родился");
    }

    @PreDestroy
    public void destroy(){
        System.out.println("Employee: я умер");
    }

    // Метод, выводящий сообщение на основе вызова метода у зависимости
    public void printWorkStation(){
        System.out.println("Employee: я работаю на " + workStation.getName());
    }
}
