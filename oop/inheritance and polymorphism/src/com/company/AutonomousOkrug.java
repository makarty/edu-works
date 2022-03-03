package com.company;

public class AutonomousOkrug extends Region{
    private String name;
    private boolean accessToTheSea;

    public AutonomousOkrug() {
        super();
        this.name = "Автономный округ";
        this.accessToTheSea = false;
    }

    @Override
    public String getInfo() {
        return "\nНазвание: " + name +
                "\nНаличие выхода к морю: " + accessToTheSea +
                "\nПлощадь: " + super.getSquare() +
                "\nВнутренний валовый продукт: " + super.getGrossDomesticProduct();
    }

    public String getInfo(int num) {
        return "\nНазвание: " + this.name;
    }

    public String getName() {
        return name;
    }

    public boolean isAccessToTheSea() {
        return accessToTheSea;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAccessToTheSea(boolean accessToTheSea) {
        this.accessToTheSea = accessToTheSea;
    }
}
