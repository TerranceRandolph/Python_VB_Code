Public Class frmHospitalCharges
    Private Sub btnCalCharg(sender As Object, e As EventArgs) Handles btnClcCharg.Click
        Dim intLenStay, intMed, intSerg, intFee, intPhy, intStay, intMiscellious, intTotalAmt As Integer
        If DoubleCheck() = True Then
            intLenStay = CInt(txtLenSty.Text)
            intMed = CInt(txtMed.Text)
            intSerg = CInt(txtSerg.Text)
            intFee = CInt(txtFee.Text)
            intPhy = CInt(txtPhy.Text)
            intStay = CalcStayCharges(intLenStay)
            intMiscellious = CalsMiscCharges(intMed, intSerg, intFee, intPhy)
            intTotalAmt = TotalCharges(intStay, intMiscellious)
            txtTotal.Text = intTotalAmt.ToString("c")
        Else
            Me.Close()
        End If

    End Sub

    Function CalcStayCharges(ByVal intLenStay As Integer) As Integer
        Dim intSCost As Integer
        intSCost = intLenStay * 350
        Return intSCost
    End Function
    Function CalsMiscCharges(ByVal intMed As Integer, intSerg As Integer, intFee As Integer, intPhy As Integer) As Integer
        Dim MiscCharges As Integer
        MiscCharges = intMed + intSerg + intFee + intPhy
        Return MiscCharges
    End Function
    Function TotalCharges(ByVal intStay As Integer, Miscellious As Integer) As Integer
        Dim TotalAmt As Integer
        TotalAmt = intStay + Miscellious
        Return TotalAmt
    End Function
    Function ValidInput(ByRef inputText As String) As Boolean
        Dim int As Integer
        Try
            If Integer.TryParse(txtLenSty.Text, int) Then
                Return True
            Else
                Return False
            End If
        Catch ex As Exception
            Return False
        End Try

    End Function
    Function DoubleCheck() As Boolean
        Dim array() As String = {txtLenSty.Text, txtMed.Text, txtSerg.Text, txtFee.Text, txtPhy.Text}
        Dim Larray() As String = {lblStay.Text, lblMed.Text, lblSerg.Text, lblFee.Text, lblPhy.Text}
        Dim arraybool As Boolean
        For i = 0 To array.Length - 1
            Try
                If ValidInput(array(i)) = True And array(i) >= 0 Then
                    arraybool = True
                ElseIf array(i) < 0 Then
                    arraybool = False
                    MessageBox.Show("Please Correct Error: " & CStr(array(i)) & vbNewLine & CStr(Larray(i)) & " : Replace Negative with integer")
                End If
            Catch ex As Exception
                arraybool = False
                MessageBox.Show("Please Correct Error: " & CStr(array(i)) & vbNewLine & CStr(Larray(i)) & " : Replace String with integer")
            End Try
        Next
        If arraybool = True Then
            Return True
        Else
            Return False
        End If
    End Function
    Private Sub btnExit_Click(sender As Object, e As EventArgs) Handles btnExit.Click
        Me.Close()
    End Sub

    Private Sub btnClear_Click(sender As Object, e As EventArgs) Handles btnClear.Click
        txtLenSty.Clear()
        txtFee.Clear()
        txtMed.Clear()
        txtSerg.Clear()
        txtPhy.Clear()
        txtTotal.Clear()

    End Sub
End Class
