package ru.first;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class Main {
    public static void main(String[] args) {
        System.out.println("init методы");
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(Config.class);

        Tablet tablet = context.getBean("tablet", Tablet.class);
        Employee employee = context.getBean("employee", Employee.class);

        System.out.println("\nВнедрение простого значения");
        System.out.println("Модель планшета: " + tablet.getName());

        System.out.println("\nВнедрение простого значения из внешнего файла через setter");
        System.out.println("ОС планшета: " + tablet.getOs());

        System.out.println("\nМетод, выводящий сообщение на основе вызова метода у зависимости");
        employee.printWorkStation();

        System.out.println("\nDestroy методы");
        context.close();
    }
}
