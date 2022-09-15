import java.util.Objects;

public class PersonalComputer extends ElectronicComputingMachine{
    private String OS;
    private String videoCard;
    private int systemBitDepth;

    public PersonalComputer() {
        super();
        OS = "Windows";
        videoCard = "Видеокарта";
        systemBitDepth = 64;
    }

    public PersonalComputer(String name, String processor, int RAM, String OS, String videoCard, int systemBitDepth) {
        super(name, processor, RAM);
        this.OS = OS;
        this.videoCard = videoCard;
        this.systemBitDepth = systemBitDepth;
    }

    public String getOS() {
        return OS;
    }

    public String getVideoCard() {
        return videoCard;
    }

    public int getSystemBitDepth() {
        return systemBitDepth;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        PersonalComputer that = (PersonalComputer) o;
        return systemBitDepth == that.systemBitDepth && Objects.equals(OS, that.OS) && Objects.equals(videoCard, that.videoCard);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), OS, videoCard, systemBitDepth);
    }

    @Override
    public String toString() {
        return "ПК " +
                "Название: " + getName() +
                "\nПроцессор: " + getProcessor() +
                "\nRAM: " + getName() +
                "\nOS: " + OS +
                "\nВидеокарта: " + videoCard +
                "\nРазрядность системы: " + systemBitDepth;
    }
}
