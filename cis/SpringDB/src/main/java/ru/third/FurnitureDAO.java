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

    public List<Furniture> findAll() {
        return jdbcTemplate.query("SELECT * FROM furniture", new BeanPropertyRowMapper<Furniture>(Furniture.class));
    }

    public void create() {
        jdbcTemplate.execute("CREATE TABLE IF NOT EXISTS furniture(id integer NOT NULL PRIMARY KEY, name VARCHAR NOt NULL," +
                "model VARCHAR NOT NULL, material VARCHAR NOT NULL, price REAL NOT NULL, volume REAL NOT NULL)");
    }

    public int insert(Furniture furniture) {
        return jdbcTemplate.update("INSERT INTO furniture VALUES (?, ?, ?, ?, ?)",
                furniture.getName(),
                furniture.getModel(),
                furniture.getMaterial(),
                furniture.getPrice(),
                furniture.getVolume());
    }
}
