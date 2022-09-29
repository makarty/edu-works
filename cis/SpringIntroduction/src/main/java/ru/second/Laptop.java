package ru.second;

public class Laptop implements PersonalComputer{
    private String name;

    public Laptop(String name) {
        this.name = name;
    }

    public String getName(){
        return name;
    }
}
