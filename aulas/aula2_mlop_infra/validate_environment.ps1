# MLOps Class II - Environment Validation Script
# PowerShell version for Windows users

Write-Host "🔍 MLOps Class II - Environment Validation" -ForegroundColor Cyan
Write-Host "=" * 50
Write-Host "⏰ Check time: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
Write-Host ""

function Test-Service {
    param(
        [string]$Name,
        [string]$Url
    )
    
    try {
        $response = Invoke-WebRequest -Uri $Url -TimeoutSec 5 -UseBasicParsing
        if ($response.StatusCode -eq 200) {
            Write-Host "✅ $Name`: Running (Status: $($response.StatusCode))" -ForegroundColor Green
            return $true
        } else {
            Write-Host "⚠️ $Name`: Unexpected status $($response.StatusCode)" -ForegroundColor Yellow
            return $false
        }
    } catch {
        Write-Host "❌ $Name`: Connection failed - $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

$services = @(
    @{Name="MLflow Server"; Url="http://localhost:5000/health"},
    @{Name="JupyterLab"; Url="http://localhost:8888"},
    @{Name="FastAPI"; Url="http://localhost:8080/health"}
)

$allGood = $true
foreach ($service in $services) {
    $result = Test-Service -Name $service.Name -Url $service.Url
    if (-not $result) {
        $allGood = $false
    }
}

Write-Host ""
Write-Host "=" * 50

if ($allGood) {
    Write-Host "🎉 All services are running correctly!" -ForegroundColor Green
    Write-Host "📚 Ready to start the notebook: notebooks/tracking_mlflow.ipynb"
    Write-Host ""
    Write-Host "Quick links:"
    Write-Host "• JupyterLab: http://localhost:8888"
    Write-Host "• MLflow UI: http://localhost:5000"
    Write-Host "• API: http://localhost:8080"
} else {
    Write-Host "⚠️ Some services are not responding." -ForegroundColor Yellow
    Write-Host "💡 Try running: docker-compose up -d"
    Write-Host "📋 Then check: docker-compose ps"
    exit 1
}
