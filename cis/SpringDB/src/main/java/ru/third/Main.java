// Вариант 11. Мебель

package ru.third;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import java.util.List;
import java.util.Scanner;

public class Main {

    private static Scanner in = new Scanner(System.in);

    private final AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(Config.class);
    private final FurnitureDAO db = context.getBean("furnitureDAO", FurnitureDAO.class);

    public static void main(String[] args) {
        int choice = 6;

        final int append = 1;
        final int print = 2;
        final int edit = 3;
        final int delete = 4;
        final int search = 5;
        final int exit = 6;

        Main program = new Main();
        program.initDB();
        while (true) {
            printMenu();
            choice = intInput("Выберите действие: ", 1, 6);
            switch (choice) {
                case append -> program.append();
                case print -> program.printFurniture();
                case edit -> program.editFields();
                case delete -> program.delete();
                case search -> program.search();
            }
            if (choice == exit)
                break;
        }

    }

    public void printFurniture() {
        List<Furniture> furniture = db.findAll();
        for(Furniture furniture1: furniture) {
            System.out.println(furniture1);
        }
    }

    public void initDB() {
        db.create();
        db.insertExampleData();
    }

    public void append() {
        String name = strInput("Введите название мебели: ");
        String model = strInput("Введите модель мебели: ");
        String material = strInput("Введите материал мебели: ");
        int price = intInput("Введите цену: ", 0, 1000000);
        int volume = intInput("Введите размер мебели: ", 0, 1000000);

        db.insert(new Furniture(name, model, material, price, volume));
    }

    public void editFields() {
        int id = intInput("Введите id редактируемой записи: ", 0, 1000000);
        String name = strInput("Введите название мебели: ");
        String model = strInput("Введите модель мебели: ");
        String material = strInput("Введите материал мебели: ");
        int price = intInput("Введите цену: ", 0, 1000000);
        int volume = intInput("Введите размер мебели: ", 0, 1000000);
        db.updateById(id, name, model, material, price, volume);
    }

    public void delete() {
        int id = intInput("Введите id удаляемой записи: ", 0, 1000000);
        db.deleteById(id);
    }

    public void search() {

        final int findById = 1;
        final int findByName = 2;
        final int findByModel = 3;
        final int findByMaterial = 4;

        printFields();
        int choice = intInput("Выберите поле, по которому будет осуществляться поиск: ", 1, 4);
        switch (choice) {
            case findById:
                int id = intInput("Введите id записи: ", 0, 1000000);
                for(Furniture furniture: db.findById(id)) {
                    System.out.println(furniture);
                }

                break;
            case findByName:
                String name = strInput("Введите имя: ");
                for(Furniture furniture: db.findByName(name)) {
                    System.out.println(furniture);
                }
                break;
            case findByModel:
                String model = strInput("Введите модель: ");
                for(Furniture furniture: db.findByModel(model)) {
                    System.out.println(furniture);
                }
                break;
            case findByMaterial:
                String material = strInput("Введите материал: ");
                for(Furniture furniture: db.findByMaterial(material)) {
                    System.out.println(furniture);
                }
                break;
        }
    }

    public static void printMenu() {
        System.out.println("1) Добавить запись");
        System.out.println("2) Вывести все записи на экран");
        System.out.println("3) Редактировать запись по id");
        System.out.println("4) Удалить запись по id");
        System.out.println("5) Поиск записи");
        System.out.println("6) Выход");
    }
    public static void printFields() {
        System.out.println("1) id");
        System.out.println("2) name");
        System.out.println("3) model");
        System.out.println("4) material");
    }
    public static int intInput(String text, int minChoice, int maxChoice) {
        int choice;
        while (true){
            System.out.print(text);
            if (!in.hasNextInt()){
                System.out.println("Ошибка! Нужно ввести число");
                in.nextLine();
                continue;
            }
            choice = in.nextInt();
            in.nextLine();
            if (choice < minChoice | choice > maxChoice) {
                System.out.println("Ошибка! Число не входит в диапазон допустимых значений");
                continue;
            }
            break;
        }
        return choice;
    }

    public static float floatInput(String text, int minChoice, int maxChoice) {
        float choice;
        while (true){
            System.out.print(text);
            if (!in.hasNextFloat()){
                System.out.println("Ошибка! Нужно ввести число");
                in.nextLine();
                continue;
            }
            choice = in.nextFloat();
            in.nextLine();
            if (choice < minChoice | choice > maxChoice) {
                System.out.println("Ошибка! Число не входит в диапазон допустимых значений");
                continue;
            }
            break;
        }
        return choice;
    }

    public static String strInput(String text) {
        String str;
        System.out.print(text);
        str = in.nextLine();
        return str;
    }
}
