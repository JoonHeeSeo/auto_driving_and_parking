package com.example.app

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import com.example.app.utils.AlertDialogUtil

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // 차량 상태 확인
        val carStatus: Button = findViewById(R.id.car_status)
        carStatus.setOnClickListener {
            val intent = Intent(this, CarStatusActivity::class.java)
            startActivity(intent)
        }

        // 차량 호출
        val callCarButton: Button = findViewById(R.id.call_car)
        callCarButton.setOnClickListener {
            AlertDialogUtil.showCarCallDialog(this)
        }

        // 자동 주차
        val autoParkingButton: Button = findViewById(R.id.auto_parking)
        autoParkingButton.setOnClickListener {
            AlertDialogUtil.showAutoParkingDialog(this)
        }

        // 임의 주차
        val customParking: Button = findViewById(R.id.custom_parking)
        customParking.setOnClickListener {
            val intent = Intent(this, CustomParkingActivity::class.java)
            startActivity(intent)
        }

    }
}