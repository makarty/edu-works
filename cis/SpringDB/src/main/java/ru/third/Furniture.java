package ru.third;


public class Furniture  {
    public int id;
    private String name;
    private String model;
    private String material;
    private int price;
    private int volume;

    public Furniture(){}

    public Furniture(Integer id, String name, String model, String material, int price, int volume) {
        this.id = id;
        this.name = name;
        this.model = model;
        this.material = material;
        this.price = price;
        this.volume = volume;
    }

    public Furniture(String name, String model, String material, int price, int volume) {
        this.id = 0;
        this.name = name;
        this.model = model;
        this.material = material;
        this.price = price;
        this.volume = volume;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public void setMaterial(String material) {
        this.material = material;
    }

    public void setVolume(int volume) {
        this.volume = volume;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getModel() {
        return model;
    }

    public int getPrice() {
        return price;
    }

    public int getVolume() {
        return volume;
    }

    public String getMaterial() {
        return material;
    }

    @Override
    public String toString() {
        return "Furniture{" +
                "name='" + name + '\'' +
                ", model='" + model + '\'' +
                ", material='" + material + '\'' +
                ", price=" + price +
                ", volume=" + volume +
                '}';
    }
}