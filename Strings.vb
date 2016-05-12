Public Class frmString
    Private Sub btnExit_Click(sender As Object, e As EventArgs) Handles btnExit.Click
        Me.Close()
    End Sub

    Private Sub btnCheck_Click(sender As Object, e As EventArgs) Handles btnCheck.Click
        Dim LBtrim, LAtrim, Concat, Pldrom, timStr As String
        Dim Afind As Integer = 0
        Dim WSidx As Integer
        Dim inter As Char

        ' Before and after the Trim '
        LBtrim = Len(txtInput.Text)
        LAtrim = Len(txtInput.Text.Trim())
        timStr = txtInput.Text.Trim()

        ' For loop to find whitespace, remove, and concatanate ' 
        For index = 0 To Len(timStr) - 1
            inter = timStr(index)
            If inter = " " Then
                WSidx = timStr.IndexOf(" ")
                Concat = timStr.Remove(WSidx, 1)
            End If
        Next

        ' For loop to find the upper and lower case a's '
        For i = 0 To Len(timStr) - 1
            inter = timStr(i)
            If (inter = "a") Or (inter = "A") Then
                Afind += 1
            End If
        Next

        ' Conditional find Palindrom and return True or False '
        If timStr = StrReverse(timStr) Then
            Pldrom = "Yes, " & timStr & " is a Palindrom"
        ElseIf timStr <> StrReverse(timStr) Then
            Pldrom = "No, " & timStr & " is not a palindrom"
        End If

        txtListBox.Items.Add("Length Before Trim :  " & LBtrim)
        txtListBox.Items.Add(vbNewLine)
        txtListBox.Items.Add("Length After Trim :  " & LAtrim)
        txtListBox.Items.Add(vbNewLine)
        txtListBox.Items.Add("There are :  " & Afind & " # of A's or a's")
        txtListBox.Items.Add(vbNewLine)
        txtListBox.Items.Add("String Without Whitespace :  " & Concat)
        txtListBox.Items.Add(vbNewLine)
        txtListBox.Items.Add("Is String a Palindrom?  " & Pldrom)

    End Sub

    Private Sub txtListBox_SelectedIndexChanged(sender As Object, e As EventArgs) Handles txtListBox.SelectedIndexChanged

    End Sub

    Private Sub btnClear_Click(sender As Object, e As EventArgs) Handles btnClear.Click
        txtListBox.Items.Clear()
        txtInput.Clear()

    End Sub
End Class
