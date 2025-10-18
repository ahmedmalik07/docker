param(
  [string]$ProjectDir = "C:\Users\ahmed\Desktop\WinterArc\docker_project_week14",
  [string]$ScreenshotsDir = "C:\Users\ahmed\Desktop\WinterArc\docker_project_week14\screenshots"
)

if (-not (Test-Path $ScreenshotsDir)) {
  New-Item -ItemType Directory -Path $ScreenshotsDir | Out-Null
}

Write-Host "Using project dir: $ProjectDir"
Push-Location $ProjectDir

Write-Host "Starting docker-compose (detached)"
docker-compose up --build -d

Start-Sleep -Seconds 3

$logFile = Join-Path $ScreenshotsDir "compose_logs.txt"
Write-Host "Saving compose logs to $logFile"
try { docker-compose logs --no-color > $logFile } catch { "Logs capture failed: $_" | Out-File $logFile }

$psFile = Join-Path $ScreenshotsDir "docker_ps.txt"
Write-Host "Saving docker ps to $psFile"
try { docker ps --format "table {{.ID}}	{{.Image}}	{{.Status}}	{{.Ports}}" > $psFile } catch { "docker ps failed: $_" | Out-File $psFile }

# Screenshot: try to capture the primary screen, but fail gracefully
$pngFile = Join-Path $ScreenshotsDir "compose_screenshot.png"
Write-Host "Attempting to capture full-screen screenshot to $pngFile"
try {
  Add-Type -AssemblyName System.Windows.Forms, System.Drawing
  $bounds = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
  $bmp = New-Object System.Drawing.Bitmap $bounds.Width, $bounds.Height
  $gfx = [System.Drawing.Graphics]::FromImage($bmp)
  $gfx.CopyFromScreen($bounds.X, $bounds.Y, 0, 0, $bmp.Size)
  $bmp.Save($pngFile, [System.Drawing.Imaging.ImageFormat]::Png)
  $gfx.Dispose()
  $bmp.Dispose()
  Write-Host "Screenshot saved to $pngFile"
} catch {
  Write-Warning "Screenshot failed: $_"
  $errFile = Join-Path $ScreenshotsDir "screenshot_error.txt"
  "Screenshot error: $_" | Out-File $errFile
}

Write-Host "Done. Files written to $ScreenshotsDir"

Pop-Location
