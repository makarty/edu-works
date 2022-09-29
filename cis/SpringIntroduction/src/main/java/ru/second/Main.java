package ru.second;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class Main {
    public static void main(String[] args) {
        ClassPathXmlApplicationContext context = new
                ClassPathXmlApplicationContext("applicationContext.xml");
        Employee testBean = context.getBean("employee", Employee.class);
        testBean.printWorkStation();
        context.close();
    }
}
