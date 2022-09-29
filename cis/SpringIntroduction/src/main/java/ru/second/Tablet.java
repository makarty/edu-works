package ru.second;

public class Tablet implements PersonalComputer{
    private String name;
    private String os;

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
