package com.company;

import java.util.ArrayList;

public abstract class Region {
    private String regionName;
    private float square;
    private float grossDomesticProduct;
    private static ArrayList<Region> heirs = new ArrayList<>();

    public Region() {
        this.square = 100;
        this.grossDomesticProduct = 1000;
    }

    public Region(float square, float grossDomesticProduct) {
        this.square = square;
        this.grossDomesticProduct = grossDomesticProduct;
    }

    public abstract String getInfo();
    public abstract String getInfo(int num);

    public float getSquare() {
        return square;
    }

    public float getGrossDomesticProduct() {
        return grossDomesticProduct;
    }

    public String getRegionName() {
        return regionName;
    }

    public static Region getHeirs(int index) {
        return heirs.get(index);
    }

    public static void getInfoHeirs() {
        for (int i = 0; i < heirs.size(); i++){
            System.out.println("------------------------------------------------");
            System.out.println("Наследник " + (i + 1) + ": " + Region.getHeirs(i).getInfo());
            System.out.println("------------------------------------------------");
        }
    }

    public void setSquare(float square) {
        this.square = square;
    }

    public static void setHeirs(Region region) {
        heirs.add(region);
    }

    public void setGrossDomesticProduct(float grossDomesticProduct) {
        this.grossDomesticProduct = grossDomesticProduct;
    }

    public void setRegionName(String regionName) {
        this.regionName = regionName;
    }

    @Override
    public String toString() {
        return "\nНазвание региона: " + regionName +
                "\nПлощадь" + square +
                "\nВВП региона:" + grossDomesticProduct;
    }
}
