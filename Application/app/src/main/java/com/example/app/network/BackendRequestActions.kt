package com.example.app.network

import android.content.Context
import android.util.Log
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

class BackendRequestActions {

    // 차량 호출
    class CarCallAction: BackendRequestManager {
        override fun performAction(context: Context) {
            val apolloClientManager = ApolloClientManager()
            CoroutineScope(Dispatchers.IO).launch {
                val response = apolloClientManager.executeCarCallMutation()
                Log.d("CarCallAction", "Response: $response")
            }
        }
    }

    // 자동 주차
    class AutoParkingAction: BackendRequestManager {
        override fun performAction(context: Context) {
            val apolloClientManager = ApolloClientManager()
            CoroutineScope(Dispatchers.IO).launch {
                val response = apolloClientManager.executeAutoParkingMutation()
                Log.d("AutoParkingAction", "Response: $response")
            }
        }
    }

    // 임의 주차
    class CustomParkingAction(private val parkingLotId: String): BackendRequestManager {
        override fun performAction(context: Context) {
            val apolloClientManager = ApolloClientManager()
            CoroutineScope(Dispatchers.IO).launch {
                val response = apolloClientManager.executeCustomParkingMutation(parkingLotId)
                Log.d("CustomParkingAction", "Response: $response")
            }
        }
    }

}