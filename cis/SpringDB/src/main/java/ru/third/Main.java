package ru.third;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import java.util.List;


public class Main {

    private final AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(Config.class);
    private final FurnitureDAO db = context.getBean("furnitureDAO", FurnitureDAO.class);

    public static void main(String[] args) {
        Main program = new Main();
        program.initDB();
    }

    public void printFurniture() {
        List<Furniture> furniture = null;
    }

    public void initDB() {
        db.create();
    }
}
