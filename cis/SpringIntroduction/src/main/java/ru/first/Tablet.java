package ru.first;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;

@Component
public class Tablet implements PersonalComputer{
    private String name;
    private String os;

    @PostConstruct
    public void init(){
        System.out.println("Tablet: я родился");
    }

    @PreDestroy
    public void destroy(){
        System.out.println("Tablet: я умер");
    }

    // Внедрение простого значения
    @Autowired
    public Tablet(String name){
        this.name = name;
    }

    // Внедрение простого значения из внешнего файла через setter
    @Value("${Tablet.os}")
    public void setOs(String os) {
        this.os = os;
    }

    public String getName(){
        return name;
    }

    public String getOs(){
        return os;
    }
}
