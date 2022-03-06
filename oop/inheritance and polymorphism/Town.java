package com.company;

public class Town {
    private String name;
    private Region region;

    public Town() {
        this.name = "Город";
    }

    public Town(String name, Region region) {
        this.name = name;
        this.region = region;
    }

    public String getName() {
        return name;
    }

    public Region getRegion() {
        return region;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setRegion(Region region) {
        this.region = region;
    }
}
