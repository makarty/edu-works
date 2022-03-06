package com.company;

public class TheEdge extends Region{
    private String name;
    private String climate;

    public TheEdge() {
        super();
        this.name = "Край";
        this.climate = "Климат";
    }

    @Override
    public String getInfo() {
        return "\nНазвание: " + name +
                "\nКлимат: " + climate +
                "\nПлощадь: " + super.getSquare() +
                "\nВнутренний валовый продукт: " + super.getGrossDomesticProduct();
    }

    public String getInfo(int num) {
        return "\nНазвание: " + this.name;
    }

    public String getName() {
        return name;
    }

    public String getClimate() {
        return climate;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setClimate(String climate) {
        this.climate = climate;
    }
}
