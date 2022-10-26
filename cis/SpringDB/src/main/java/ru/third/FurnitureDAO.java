package ru.third;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.stereotype.Component;
import org.springframework.jdbc.core.JdbcTemplate;

import javax.sql.DataSource;
import java.util.List;

@Component
public class FurnitureDAO {
    JdbcTemplate jdbcTemplate;

    @Autowired
    public void setDataSource(DataSource dataSource) {
        this.jdbcTemplate = new JdbcTemplate(dataSource);
    }

    public void create() {
        jdbcTemplate.execute("DROP TABLE IF EXISTS furniture");
        jdbcTemplate.execute("CREATE TABLE furniture(id integer NOT NULL PRIMARY KEY, name VARCHAR NOt NULL," +
                "model VARCHAR NOT NULL, material VARCHAR NOT NULL, price REAL NOT NULL, volume REAL NOT NULL)");
    }

    public List<Furniture> findAll() {
        return jdbcTemplate.query("SELECT * FROM furniture", new BeanPropertyRowMapper<>(Furniture.class));
    }

    public List<Furniture> findByName(String name) {
        return jdbcTemplate.query("SELECT * FROM furniture WHERE name=?", new BeanPropertyRowMapper<>(Furniture.class), name);
    }

    public List<Furniture> findById(int id) {
        return jdbcTemplate.query("SELECT * FROM furniture WHERE id=?", new BeanPropertyRowMapper<>(Furniture.class), id);
    }

    public List<Furniture> findByModel(String model) {
        return jdbcTemplate.query("SELECT * FROM furniture WHERE model=?", new BeanPropertyRowMapper<>(Furniture.class), model);
    }

    public List<Furniture> findByMaterial(String material) {
        return jdbcTemplate.query("SELECT * FROM furniture WHERE material=?", new BeanPropertyRowMapper<>(Furniture.class), material);
    }

    public int insert(Furniture furniture) {
        return jdbcTemplate.update("INSERT INTO furniture (name, model, material, price, volume) VALUES (?, ?, ?, ?, ?)",
                furniture.getName(),
                furniture.getModel(),
                furniture.getMaterial(),
                furniture.getPrice(),
                furniture.getVolume()
        );
    }

    public int updateById(int id, String name, String model, String material, float price, float volume) {
        return jdbcTemplate.update("UPDATE furniture SET name = ?, model = ?, material = ?, price = ?, volume = ? WHERE id = ?",
                name,
                model,
                material,
                price,
                volume,
                id
        );
    }

    public int deleteById(int id) {
        return jdbcTemplate.update("DELETE FROM furniture WHERE id = ?", id);
    }

    public void insertExampleData() {
        Furniture furniture[] = {
                new Furniture("Стул", "д1", "Дуб", 120, 540),
                new Furniture("Стол", "ст02", "Камень", 350, 650),
                new Furniture("Стол", "д56", "Железо", 400, 700),
                new Furniture("Шкаф", "шк98", "Осина", 500, 1000),
                new Furniture("Тумбочка", "тб", "Красное дерево", 222, 300),
                new Furniture("Комод", "е1", "Сосна", 100, 430),
        };
        for (Furniture furniture1: furniture) {
            insert(furniture1);
        }
    }
}
