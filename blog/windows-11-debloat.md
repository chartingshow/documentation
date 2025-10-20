# Windows 11 Debloat and Ad Removal Script

Here's a safe, all-in-one **PowerShell command** that cleans up Windows 11's junk apps and disables ads/recommendations in the Start menu and Settings:

### PowerShell One-Liner Debloat Script

Run this as **Administrator** (right-click _Start → Windows PowerShell (Admin)_ or _Terminal (Admin)_), then paste:

```powershell
# Remove common preinstalled junk and disable ads/recommendations
$appPatterns = @(
  "*xbox*", "*tiktok*", "*spotify*", "*clipchamp*", "*news*", "*weather*",
  "*candycrush*", "*onenote*", "*getstarted*", "*linkedin*", "*netflix*",
  "*primevideo*", "*disney*", "*solitaire*"
)
foreach ($pattern in $appPatterns) {
  Get-AppxPackage $pattern -AllUsers | Remove-AppxPackage -ErrorAction SilentlyContinue
}

# Disable Start menu and Settings suggestions
New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Start" -Name "ShowRecommendations" -Value 0 -PropertyType DWord -Force | Out-Null
New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" -Name "Start_TrackProgs" -Value 0 -PropertyType DWord -Force | Out-Null
New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" -Name "Start_TrackDocs" -Value 0 -PropertyType DWord -Force | Out-Null
New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" -Name "SubscribedContent-338389Enabled" -Value 0 -PropertyType DWord -Force | Out-Null
New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" -Name "SubscribedContent-310093Enabled" -Value 0 -PropertyType DWord -Force | Out-Null
New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" -Name "SubscribedContent-353698Enabled" -Value 0 -PropertyType DWord -Force | Out-Null

# Clear Start pinned apps (requires Windows 11 22H2+)
if (Get-Command Unpin-StartApp -ErrorAction SilentlyContinue) {
  Get-StartApps | ForEach-Object { Unpin-StartApp $_.Name }
}

Write-Host "`n✅ Junk removed and Start menu cleaned! Restart or sign out to apply all changes." -ForegroundColor Green
```

### What This Does

- Removes most unwanted bundled apps (TikTok, Spotify, Xbox, Weather, etc.)
- Disables Start menu “recommendations” and “suggested” content
- Stops Settings app ads/promotions
- Optionally unpins all apps from Start if your build supports it
- Safe to run; does not remove essential system components

### Note

- Some apps may reappear after major Windows updates, you can rerun the script as needed.
- To restore any removed apps, you can reinstall them from the Microsoft Store.
