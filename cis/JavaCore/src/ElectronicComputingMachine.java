import java.util.Objects;

public class ElectronicComputingMachine {
    private String name;
    private String processor;
    private int RAM;

    public ElectronicComputingMachine(){
        name = "ЭВМ";
        processor = "Процессор";
        RAM = 4;
    }

    public ElectronicComputingMachine(String name, String processor, int RAM) {
        this.name = name;
        this.processor = processor;
        this.RAM = RAM;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        ElectronicComputingMachine that = (ElectronicComputingMachine) o;
        return RAM == that.RAM && Objects.equals(name, that.name) && Objects.equals(processor, that.processor);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, processor, RAM);
    }

    public String getName() {
        return name;
    }

    public String getProcessor() {
        return processor;
    }

    public int getRAM() {
        return RAM;
    }

    @Override
    public String toString() {
        return "ЭВМ " +
                "Название: " + name +
                "\nПроцессор: " + processor +
                "\nRAM:" + RAM;
    }
}
