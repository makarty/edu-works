package com.company;

public class Main {

    public static void main(String[] args) {
        Region ar = new Area();
        Town town = new Town();
        Region.setHeirs(ar);
        Region.setHeirs(new TheEdge());
        Region.setHeirs(new AutonomousOkrug());
        town.setRegion(ar);
	    System.out.println("Информация об объекте: " + ar.getInfo());
        System.out.println("------------------------------------------");
	    System.out.println("Информация об имени объекта: " + ar.getInfo(1));
        Region.getInfoHeirs();
    }
}
