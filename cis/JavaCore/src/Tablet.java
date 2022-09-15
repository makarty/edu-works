import java.util.Objects;

public class Tablet extends PersonalComputer{
    private int cameraResolution;
    private String displayType;

    public Tablet() {
        cameraResolution = 8;
        displayType = "AMOLED";
    }

    public Tablet(
              String name,
              String processor,
              int RAM,
              String OS,
              String videoCard,
              int systemBitDepth,
              int cameraResolution,
              String displayType
    ) {
        super(name, processor, RAM, OS, videoCard, systemBitDepth);
        this.cameraResolution = cameraResolution;
        this.displayType = displayType;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Tablet tablet = (Tablet) o;
        return cameraResolution == tablet.cameraResolution && Objects.equals(displayType, tablet.displayType);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), cameraResolution, displayType);
    }

    @Override
    public String toString() {
        return "Планшет " +
                "Название: " + getName() +
                "\nПроцессор: " + getProcessor() +
                "\nRAM: " + getName() +
                "\nOS: " + getOS() +
                "\nВидеокарта: " + getVideoCard() +
                "\nРазрядность системы: " + getSystemBitDepth() +
                "\nРазрешение камеры(Мп): " + cameraResolution +
                "\nТип дисплея: " + displayType;
    }
}
