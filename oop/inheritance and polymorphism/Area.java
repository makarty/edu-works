package com.company;

public class Area extends Region{
    private String name;
    private String characteristicsOfTheArea;

    public Area() {
        super();
        this.name = "Область";
        this.characteristicsOfTheArea = "Горная";
    }

    @Override
    public String getInfo() {
        return "\nНазвание: " + name +
                "\nХарактеристика местности: " + characteristicsOfTheArea +
                "\nПлощадь: " + super.getSquare() +
                "\nВнутренний валовый продукт: " + super.getGrossDomesticProduct();
    }

    public String getInfo(int num) {
        return "\nНазвание: " + this.name;
    }

    public String getName() {
        return name;
    }

    public String getCharacteristicsOfTheArea() {
        return characteristicsOfTheArea;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setCharacteristicsOfTheArea(String characteristicsOfTheArea) {
        this.characteristicsOfTheArea = characteristicsOfTheArea;
    }
}
