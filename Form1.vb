Public Class frmSales
    Private Sub TextBox1_TextChanged(sender As Object, e As EventArgs) Handles txtpackA.TextChanged


    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles btnCompute.Click
        Dim dblpackA, dblpackB, dblpackC, dblTotal, Rpack_A, Rpack_B, Rpack_C As Double
        Dim strMultiline As String

        ' Set package math to var.
        dblpackA = txtpackA.Text * 99
        dblpackB = txtpackB.Text * 199
        dblpackC = txtpackC.Text * 299
        dblTotal = Rpack_A + Rpack_B + Rpack_C
        strMultiline = txtMtL.Text

        ' Condition for A... each expression checkes # of units
        If (txtpackA.Text > 9) And (txtpackA.Text < 19) Then
            Rpack_A = dblpackA - (dblpackA * (20 / 100))
        ElseIf (txtpackA.Text > 20) And (txtpackA.Text < 49) Then
            Rpack_A = dblpackA - (dblpackA * (30 / 100))
        ElseIf (txtpackA.Text > 50) And (txtpackA.Text < 99) Then
            Rpack_A = dblpackA - (dblpackA * (40 / 100))
        ElseIf txtpackA.Text > 100 Then
            Rpack_A = dblpackA - (dblpackA * (50 / 100))
        Else
            Rpack_A = dblpackA
        End If

        ' Conditions for Package B
        If (txtpackB.Text > 9) And (txtpackB.Text < 19) Then
            Rpack_B = dblpackB - (dblpackB * (20 / 100))
        ElseIf (txtpackB.Text > 20) And (txtpackB.Text < 49) Then
            Rpack_B = dblpackB - (dblpackB * (30 / 100))
        ElseIf (txtpackB.Text > 50) And (txtpackB.Text < 99) Then
            Rpack_B = dblpackB - (dblpackB * (40 / 100))
        ElseIf txtpackB.Text > 100 Then
            Rpack_B = dblpackB - (dblpackB * (50 / 100))
        Else
            Rpack_B = dblpackB
        End If

        ' Conditions for Package C
        If (txtpackC.Text > 9) And (txtpackC.Text < 19) Then
            Rpack_C = dblpackC - (dblpackC * (20 / 100))
        ElseIf (txtpackC.Text > 20) And (txtpackC.Text < 49) Then
            Rpack_C = dblpackC - (dblpackC * (30 / 100))
        ElseIf (txtpackC.Text > 50) And (txtpackC.Text < 99) Then
            Rpack_C = dblpackC - (dblpackC * (40 / 100))
        ElseIf txtpackC.Text > 100 Then
            Rpack_C = dblpackC - (dblpackC * (50 / 100))
        Else
            Rpack_C = dblpackC
        End If

        ' Finally send result to multiline
        dblTotal = Rpack_A + Rpack_B + Rpack_C
        txtMtL.Text = "Package A Total: " + Rpack_A.ToString("c") + vbNewLine +
                      "Package B Total: " + Rpack_B.ToString("c") + vbNewLine +
                      "Package C Total: " + Rpack_C.ToString("c") + vbNewLine + vbNewLine +
                      "GrandTotal: " + dblTotal.ToString("c")
    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles lblClear.Click
        txtpackA.Clear()
        txtpackB.Clear()
        txtpackC.Clear()
        txtMtL.Clear()
    End Sub

    Private Sub Button3_Click(sender As Object, e As EventArgs) Handles btnExit.Click
        Me.Close()
    End Sub

    Private Sub Label2_Click(sender As Object, e As EventArgs) Handles lblpackA.Click

    End Sub

    Private Sub txtMtL_TextChanged(sender As Object, e As EventArgs) Handles txtMtL.TextChanged

    End Sub
End Class
