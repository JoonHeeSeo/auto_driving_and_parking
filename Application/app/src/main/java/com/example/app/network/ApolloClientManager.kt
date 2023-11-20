package com.example.app.network

import com.apollographql.apollo3.ApolloClient
import com.apollographql.apollo3.api.ApolloResponse
import com.simple.graphql.AutoParkingMutation
import com.simple.graphql.CarCallMutation
import com.simple.graphql.CarStatusQuery
import com.simple.graphql.CustomParkingMutation
import com.simple.graphql.ParkingLotQuery
import com.simple.graphql.TestTestQuery
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext

class ApolloClientManager {
    private val apolloClient = ApolloClient.Builder()
        // 로컬 환경
//        .serverUrl("http://10.0.2.2:8000/graphql")

        // 배포 환경
        .serverUrl("https://k9a408.p.ssafy.io/graphql")
        .build()

    suspend fun executeParkingLotQuery(): ApolloResponse<ParkingLotQuery.Data> {
        return withContext(Dispatchers.IO) {
            apolloClient.query(ParkingLotQuery()).execute()
        }
    }

    suspend fun executeCarStatusQuery(): ApolloResponse<CarStatusQuery.Data> {
        return withContext(Dispatchers.IO) {
            apolloClient.query(CarStatusQuery()).execute()
        }
    }

    suspend fun executeTestQuery(): ApolloResponse<TestTestQuery.Data> {
        return withContext(Dispatchers.IO) {
            apolloClient.query(TestTestQuery()).execute()
        }
    }

    suspend fun executeCarCallMutation(): ApolloResponse<CarCallMutation.Data> {
        return withContext(Dispatchers.IO) {
            apolloClient.mutation(CarCallMutation()).execute()
        }
    }

    suspend fun executeAutoParkingMutation(): ApolloResponse<AutoParkingMutation.Data> {
        return withContext(Dispatchers.IO) {
            apolloClient.mutation(AutoParkingMutation()).execute()
        }
    }

    suspend fun executeCustomParkingMutation(parkingLotId: String): ApolloResponse<CustomParkingMutation.Data> {
        return withContext(Dispatchers.IO) {
            apolloClient.mutation(CustomParkingMutation(parkingLotId)).execute()
        }
    }
}
