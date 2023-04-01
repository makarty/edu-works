package com.example.lab2;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {
    private Button oneRental;
    private Button twoRental;
    private Button threeRental;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        oneRental = findViewById(R.id.oneRental);
        twoRental = findViewById(R.id.twoRental);
        threeRental = findViewById(R.id.threeRental);
    }
}