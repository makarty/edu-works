import java.util.Objects;

public class Laptop extends PersonalComputer{
    private int batteryLifeHours;
    private String typeOfChargingConnector;

    public Laptop() {
        super();
        batteryLifeHours = 13;
        typeOfChargingConnector = "Type-C";
    }

    public Laptop(
            String name,
            String processor,
            int RAM,
            String OS,
            String videoCard,
            int systemBitDepth,
            int batteryLifeHours,
            String typeOfChargingConnector
    ) {
        super(name, processor, RAM, OS, videoCard, systemBitDepth);
        this.batteryLifeHours = batteryLifeHours;
        this.typeOfChargingConnector = typeOfChargingConnector;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Laptop laptop = (Laptop) o;
        return batteryLifeHours == laptop.batteryLifeHours && Objects.equals(typeOfChargingConnector, laptop.typeOfChargingConnector);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), batteryLifeHours, typeOfChargingConnector);
    }

    @Override
    public String toString() {
        return "Ноутбук " +
                "Название: " + getName() +
                "\nПроцессор: " + getProcessor() +
                "\nRAM: " + getName() +
                "\nOS: " + getOS() +
                "\nВидеокарта: " + getVideoCard() +
                "\nРазрядность системы: " + getSystemBitDepth() +
                "\nЧасы автономной работы батареи: " + batteryLifeHours +
                "\nРазъём для зарядки: " + typeOfChargingConnector;
    }
}
