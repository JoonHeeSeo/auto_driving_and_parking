package com.example.app

import android.os.Bundle
import android.widget.Button
import android.widget.LinearLayout
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import com.example.app.network.ApolloClientManager
import com.example.app.utils.AlertDialogUtil
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class CustomParkingActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_custom_parking)

        val apolloManager = ApolloClientManager()

        val layout = findViewById<LinearLayout>(R.id.layout)

        lifecycleScope.launch(Dispatchers.IO) {
            val response = apolloManager.executeParkingLotQuery()

            if (response.data != null && response.data?.parkingLots != null) {
                for (parkingLot in response.data?.parkingLots!!) {

                    withContext(Dispatchers.Main) {
                        val buttonText = "주차장 이름: ${parkingLot?.parkingLotName}\n기본 요금: ${parkingLot?.standardRate}\n시간당 추가 요금: ${parkingLot?.overtimeRate}\n빈 자리수: ${parkingLot?.vacancy}"

                        val button = Button(this@CustomParkingActivity)
                        button.text = buttonText
                        button.textSize = 20f
                        button.setOnClickListener {
                            AlertDialogUtil.showCustomParkingDialog(this@CustomParkingActivity, parkingLot?.parkingLotId ?: "", parkingLot?.parkingLotName ?: "")
                        }

                        // 버튼을 추가
                        layout.addView(button)
                    }
                }
            } else if (response.hasErrors()) {
                println("Errors: ${response.errors}")
            }
        }
        
    }
}