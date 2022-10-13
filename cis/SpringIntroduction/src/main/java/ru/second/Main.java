package ru.second;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class Main {
    public static void main(String[] args) {
        ClassPathXmlApplicationContext context = new
                ClassPathXmlApplicationContext("applicationContext.xml");

        Employee employee = context.getBean("employee", Employee.class);
        Tablet tablet = context.getBean("tablet", Tablet.class);
        Laptop laptop = context.getBean("laptop", Laptop.class);

        System.out.println("Внедрение простого значения");
        System.out.println(laptop.getName());

        System.out.println("\nМетод, выводящий сообщение на основе вызова метода у зависимости");
        employee.printWorkStation();

        System.out.println("\nВнедрение простого значения из внешнего файла через setter");
        System.out.println(tablet.getOs());
        context.close();
    }
}
