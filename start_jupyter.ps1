# Start Jupyter Lab and Auto-Open in Browser
# Fixed version that avoids file permission errors!

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Starting Jupyter Lab" -ForegroundColor Yellow
Write-Host "========================================`n" -ForegroundColor Cyan

# Change to ML_Projects directory
Set-Location "D:\ML_Projects"

# Activate virtual environment
& "D:\ML_Projects\ml_env\Scripts\Activate.ps1"

Write-Host "Starting Jupyter Lab (without auto-browser)..." -ForegroundColor Green
Write-Host "This avoids the file permission error!`n" -ForegroundColor White

# Start Jupyter Lab WITHOUT browser (this prevents the file:/// error)
# and run it in the foreground so we can capture output
$job = Start-Job -ScriptBlock {
    Set-Location "D:\ML_Projects"
    & "D:\ML_Projects\ml_env\Scripts\Activate.ps1"
    & "D:\ML_Projects\ml_env\Scripts\jupyter-lab.exe" --no-browser --port=8888
}

Write-Host "Waiting for Jupyter to start..." -ForegroundColor Yellow
Start-Sleep -Seconds 5

# Use jupyter lab list to get the URL
try {
    $listOutput = & "D:\ML_Projects\ml_env\Scripts\jupyter.exe" lab list 2>&1 | Out-String
    
    if ($listOutput -match "http://localhost:\d+/[^\s]+") {
        $url = $matches[0]
        Write-Host "✅ Jupyter Lab is ready!" -ForegroundColor Green
        Write-Host "   URL: $url`n" -ForegroundColor Cyan
        
        # Open browser with the URL
        Start-Process $url
        
        Write-Host "✅ Browser opened successfully!" -ForegroundColor Green
        Write-Host "`n⚠️  Keep this window open - Jupyter is running here" -ForegroundColor Yellow
        Write-Host "   Press Ctrl+C to stop Jupyter Lab`n" -ForegroundColor Yellow
        
        # Show job output
        Receive-Job -Job $job -Wait
    } else {
        Write-Host "⚠️  Jupyter is starting but URL not found yet." -ForegroundColor Yellow
        Write-Host "   Check below for the URL to copy:`n" -ForegroundColor Yellow
        Receive-Job -Job $job -Wait
    }
} catch {
    Write-Host "❌ Error getting URL. Showing Jupyter output:`n" -ForegroundColor Red
    Receive-Job -Job $job -Wait
}
