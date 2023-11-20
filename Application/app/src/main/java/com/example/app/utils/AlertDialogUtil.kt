package com.example.app.utils
import android.content.Context
import androidx.appcompat.app.AlertDialog
import com.example.app.network.BackendRequestActions
import com.example.app.network.BackendRequestManager

object AlertDialogUtil {

    fun showCarCallDialog(context: Context) {
        showAlertDialog(context, 1, "차량 호출", "차량을 호출하시겠습니까?", BackendRequestActions.CarCallAction())
    }
    fun showAutoParkingDialog(context: Context) {
        showAlertDialog(context, 2, "자동 주차", "차량을 자동으로 주차하시겠습니까?", BackendRequestActions.AutoParkingAction())
    }
    fun showCustomParkingDialog(context: Context, parkingLotId: String, parkingLotName: String) {
        showAlertDialog(context, 3, "임의 주차", "차량을 ${parkingLotName}에 주차하시겠습니까?", BackendRequestActions.CustomParkingAction(parkingLotId))
    }

    fun showAlertDialog(context: Context, type: Long, title: String, message: String, action: BackendRequestManager) {
        // type : 1 차량 호출, 2 자동 주차, 3 임의 주차
        AlertDialog.Builder(context).apply{
            setTitle(title)
            setMessage(message)
            setPositiveButton(android.R.string.yes) { dialog, which ->
                action.performAction(context)
            }
            setNegativeButton(android.R.string.no, null)
        }.create().show()
    }
}