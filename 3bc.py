### Three Black Crows Psuedocode

Input ticker
Set 3bc = zero
Set j = 7 //counter for each daily close
[c] = Get last seven days closing prices 7 down to 1 //'Today is zero'

For j < 7 --1 
	If c[j] is < c[j+1] 
		3bc = 3bc + 1
	Else 
		3bc = 0
End For

