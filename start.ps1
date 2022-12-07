$filenameArray = Get-ChildItem "./inupt"

for ($i = 0; $i -lt $filenameArray.Count; $i+=2) {
    $GenTextPath = $filenameArray[$($i+1)]
    $DefTextPath = $filenameArray[$($i+0)]
    echo "$GenTextPath , $DefTextPath , $($i/2).out"
    Invoke-Expression("python main.py '$GenTextPath' '$DefTextPath' '$($i/2).out'")
}