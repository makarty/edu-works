package ru.first;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;

@Component
public class Laptop implements PersonalComputer{
    private String name;

    public Laptop(){
        name = "Lenovo IdeaPad 5 15ARE05";
    }
    @PostConstruct
    public void init(){
        System.out.println("Laptop: я родился");
    }

    @PreDestroy
    public void destroy(){
        System.out.println("Laptop: я умер");
    }

    @Override
    public String getName() {
        return name;
    }
}
