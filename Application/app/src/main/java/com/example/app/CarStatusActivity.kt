package com.example.app

import android.annotation.SuppressLint
import android.os.Bundle
import android.widget.ImageView
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import com.example.app.network.ApolloClientManager
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

class CarStatusActivity : AppCompatActivity() {

    @SuppressLint("MissingInflatedId")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_car_status)

        val refreshImageView: ImageView = findViewById(R.id.refreshImageView)

        val dateTextView: TextView = findViewById(R.id.dateTextView)
        val timeTextView: TextView = findViewById(R.id.timeTextView)
        val velocityTextView: TextView = findViewById(R.id.velocityTextView)
        val batteryTextView: TextView = findViewById(R.id.batteryTextView)

        val apolloManager = ApolloClientManager()

        refreshImageView.setOnClickListener {
            refreshCarStatus(apolloManager, dateTextView, timeTextView, velocityTextView, batteryTextView)
            Toast.makeText(this@CarStatusActivity, "새로고침이 완료되었습니다.", Toast.LENGTH_SHORT).show()
        }

        refreshCarStatus(apolloManager, dateTextView, timeTextView, velocityTextView, batteryTextView)
    }

    private fun refreshCarStatus(apolloManager: ApolloClientManager, dateTextView: TextView, timeTextView: TextView, velocityTextView: TextView, batteryTextView: TextView) {
        lifecycleScope.launch(Dispatchers.IO) {
            val response = apolloManager.executeCarStatusQuery()

            if (response.data != null && response.data?.carStatus != null) {
                val carStatus = response.data?.carStatus!!

                val dateTime = LocalDateTime.parse(carStatus.time.toString(), DateTimeFormatter.ISO_DATE_TIME)
                val date = "날짜 : ${dateTime.toLocalDate()}"
                val time = "시간 : ${dateTime.toLocalTime()}"

                val velocity = "속도 : ${carStatus.velocity}"
                val battery = "배터리 : ${carStatus.battery}"

                withContext(Dispatchers.Main) {
                    dateTextView.text = date
                    timeTextView.text = time
                    velocityTextView.text = velocity
                    batteryTextView.text = battery
                }
            } else if (response.hasErrors()) {
                println("Errors: ${response.errors}")
            }
        }
    }
}
