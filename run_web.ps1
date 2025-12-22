Write-Host "Starting Flask web app (webapp\app.py)"
$env:PYTHONPATH = (Join-Path $PSScriptRoot "src")
python -m webapp.app
