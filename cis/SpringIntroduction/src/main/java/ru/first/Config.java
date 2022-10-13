package ru.first;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;


@Configuration
@ComponentScan("ru.first")
@PropertySource("classpath:Tablet.properties")
public class Config {

    // Внедрение простого значения
    @Bean
    public String name(){
        return "Xiaomi Pad 5";
    }
}
