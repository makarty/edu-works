import java.util.Random;
import java.util.Scanner;
import java.util.concurrent.Semaphore;


public class Main {
    private static Scanner in = new Scanner(System.in);
    public static void main(String[] args) throws InterruptedException {
        int N;
        int numberOfAircraft;
        while (true) {
            System.out.print("Введите количество взлётно-посадочных полос: ");
            if (in.hasNextInt()) {
                N = in.nextInt();
                in.nextLine();
                if (N < 0){
                    System.out.println("Ошибка! Нужно ввести положительное число");
                    continue;
                }else if (N == 0){
                    System.out.println("Ошибка! N не должен быть нулём");
                    continue;
                }
                break;
            } else {
                System.out.println("Ошибка! Нужно ввести число");
                in.nextLine();
                continue;
            }
        }
        while (true) {
            System.out.print("Введите количество самолётов: ");
            if (in.hasNextInt()) {
                numberOfAircraft = in.nextInt();
                in.nextLine();
                if (numberOfAircraft < 0){
                    System.out.println("Ошибка! Нужно ввести положительное число");
                    continue;
                }
                break;
            } else {
                System.out.println("Ошибка! Нужно ввести число");
                in.nextLine();
            }
        }
        final Semaphore runway = new Semaphore(N);
        Plain[] plains = new Plain[numberOfAircraft];
        for (int i = 0; i < numberOfAircraft; i++)
            plains[i] = new Plain(runway, ("Boeing70" + i));
        for (int i = 0; i < numberOfAircraft; i++)
            plains[i].start();
        for (int i = 0; i < numberOfAircraft; i++){
            if (plains[i].getLanded())
                plains[i].interrupt();
        }
    }
}
class Plain extends Thread{
    private final Semaphore runway;
    private static final Random randomTimer = new Random();
    private boolean landed = false;
    private String name;
    public Plain(Semaphore runway, String name) {
        super();
        this.runway = runway;
        this.name = name;
    }
    @Override
    public void run() {
        while (true) {
            try {
                if (!landed){
                    if (runway.availablePermits() <= 0){
                        say("Ожидаю разрешение на посадку");
                    }
                    runway.acquire();
                    say("Совершаю на посадку");
                    sleep(randomTimer.nextInt(0, 1000));
                    landed = true;
                    say("Посадка завершена, полоса свободна");
                    runway.release();
                    sleep(randomTimer.nextInt(0, 1000));
                }
            } catch (InterruptedException ignored) {}
        }
    }
    public void say(String text){
        System.out.println("Пилот самолёта " + name + ": " + text);
    }
    public boolean getLanded(){
        return landed;
    }
}
