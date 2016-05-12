Public Class frmSwap
    Private Sub btnExit_Click(sender As Object, e As EventArgs) Handles btnExit.Click
        Me.Close()
    End Sub

    Private Sub btnSwap_Click(sender As Object, e As EventArgs) Handles btnSwap.Click
        Dim dbltxtNum1 As Double
        Dim dbltxtNum2 As Double
        Dim tempVal2 As Double

        dbltxtNum1 = CDbl(txtNum1.Text)
        dbltxtNum2 = CDbl(txtNum2.Text)
        tempVal2 = dbltxtNum1

        txtNum1.Text = CStr(txtNum2.Text)
        txtNum2.Text = CStr(tempVal2)

    End Sub

    Private Sub txtNum1_TextChanged(sender As Object, e As EventArgs) Handles txtNum1.TextChanged

    End Sub

    Private Sub txtNum2_TextChanged(sender As Object, e As EventArgs) Handles txtNum2.TextChanged

    End Sub
End Class
