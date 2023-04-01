package com.example.intro;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;

import com.yandex.mapkit.Animation;
import com.yandex.mapkit.MapKitFactory;
import com.yandex.mapkit.geometry.Point;
import com.yandex.mapkit.map.CameraPosition;
import com.yandex.mapkit.mapview.MapView;

public class MainActivity extends AppCompatActivity {
    private final String MAPKIT_API_KEY = "c8eb8bb9-5c88-4e98-97a5-29009ff65cf6";
    private final Point TARGET_LOCATION = new Point(56.027025, 92.941112);

    private MapView mapView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        MapKitFactory.setApiKey(MAPKIT_API_KEY);

        MapKitFactory.initialize(this);
        setContentView(R.layout.activity_main);
        super.onCreate(savedInstanceState);
        mapView = (MapView)findViewById(R.id.mapview);

        mapView.getMap().move(
                new CameraPosition(TARGET_LOCATION, 15.0f, 0.0f, 0.0f),
                new Animation(Animation.Type.SMOOTH, 5),
                null);
    }

    @Override
    protected void onStop() {
        mapView.onStop();
        MapKitFactory.getInstance().onStop();
        super.onStop();
    }

    @Override
    protected void onStart() {
        super.onStart();
        MapKitFactory.getInstance().onStart();
        mapView.onStart();
    }
}