import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    private static Scanner in = new Scanner(System.in);
    public static void main(String[] args) {
        final int addElement = 1;
        final int removeElement = 2;
        final int printElements = 3;
        final int comparisonElements = 4;
        final int exit = 5;

        int choice;
        ArrayList<ElectronicComputingMachine> elements = new ArrayList<>();

        while (true){
            printMenu();

            choice = intInput("Выберите действие: ", 1, 5);

            switch (choice){
                case addElement:
                    add(elements);
                    break;
                case removeElement:
                    remove(elements);
                    break;
                case printElements:
                    for (int i = 0; i < elements.size(); i++) {
                        System.out.println("\n" + elements.get(i));
                    }
                    break;
                case comparisonElements:
                    comparison(elements);
                    break;
            }
            if (choice == exit)
                break;
        }
    }

    public static void printMenu() {
        System.out.println("----------------------------------");
        System.out.println("1) Добавить новый элемент");
        System.out.println("2) Удалить Элемент по индексу");
        System.out.println("3) Вывести все элементы в консоль");
        System.out.println("4) Сравнение двух элементов");
        System.out.println("5) Выход");
        System.out.println("----------------------------------");
    }

    public static void printObjects() {
        System.out.println("1) ЭВМ");
        System.out.println("2) ПК");
        System.out.println("3) Ноутбук");
        System.out.println("4) Планшет");
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
            if (choice < minChoice | choice > maxChoice) {
                System.out.println("Ошибка! Число не входит в диапазон допустимых значений");
                continue;
            }
            break;
        }
        return choice;
    }

    public static void add(ArrayList<ElectronicComputingMachine> elements) {
        final int ECM = 1;
        final int PC = 2;
        final int laptop = 3;
        final int tablet = 4;
        ElectronicComputingMachine item = null;

        printObjects();
        int choice = intInput("Какой объект хотите добавить: ", 1, 4);

        switch (choice) {
            case ECM:
                item = new ElectronicComputingMachine();
                break;
            case PC:
                item = new PersonalComputer();
                break;
            case laptop:
                item = new Laptop();
                break;
            case tablet:
                item = new Tablet();
                break;
        }

        elements.add(item);
    }

    public static void remove(ArrayList<ElectronicComputingMachine> elements) {
        for (int i = 0; i < elements.size(); i++) {
            System.out.println("\n№" + (i + 1) + "\n" + elements.get(i));
        }
        int choice = intInput("Какой объект хотите удалить: ", 1, elements.size());
        elements.remove(choice - 1);
    }

    public static void comparison(ArrayList<ElectronicComputingMachine> elements) {
        for (int i = 0; i < elements.size(); i++) {
            System.out.println("\n№" + (i + 1) + "\n" + elements.get(i));
        }
        int firstElem = intInput("Выберите первый элемент для сравнения: ", 1, elements.size());
        int secondElem = intInput("Выберите второй элемент для сравнения: ", 1, elements.size());
        System.out.println(elements.get(firstElem - 1).equals(elements.get(secondElem - 1)));
    }
}