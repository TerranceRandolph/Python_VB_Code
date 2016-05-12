Public Class frmStudentInfo
    Private Sub pbStudent_Click(sender As Object, e As EventArgs) Handles pbStudent.Click

    End Sub

    Private Sub btnMessage_Click(sender As Object, e As EventArgs) Handles btnMessage.Click
        Dim strtxtFirst_Name As String
        Dim strtxtLast_Name As String
        Dim inttxtCell_Num As Double
        Dim strResult As String

        strtxtFirst_Name = txtFirst_Name.Text
        strtxtLast_Name = txtLast_Name.Text
        inttxtCell_Num = txtCell_Num.Text
        strResult = "First Name: " + txtFirst_Name.Text &
                    vbNewLine & " Last Name: " + txtLast_Name.Text &
                    vbNewLine & " Cell Number: " + CStr(txtCell_Num.Text)

        MessageBox.Show(strResult)
        Me.lblStatus.Text = "First Name: " + txtFirst_Name.Text & " - Last Name: " +
                             txtLast_Name.Text & " - Cell Number: " + CStr(txtCell_Num.Text)

    End Sub

    Private Sub txtFirst_Name_TextChanged(sender As Object, e As EventArgs) Handles txtFirst_Name.TextChanged

    End Sub

    Private Sub frmStudentInfo_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub

    Private Sub txtLast_Name_TextChanged(sender As Object, e As EventArgs) Handles txtLast_Name.TextChanged

    End Sub

    Private Sub txtCell_Num_TextChanged(sender As Object, e As EventArgs) Handles txtCell_Num.TextChanged

    End Sub

    Private Sub btnClose_Click(sender As Object, e As EventArgs) Handles btnClose.Click
        Me.Close()
    End Sub

    Private Sub btnClear_Click(sender As Object, e As EventArgs) Handles btnClear.Click
        txtFirst_Name.Clear()
        txtLast_Name.Clear()
        txtCell_Num.Clear()

    End Sub

    Private Sub lblStatus_Click(sender As Object, e As EventArgs) Handles lblStatus.Click

    End Sub
End Class
