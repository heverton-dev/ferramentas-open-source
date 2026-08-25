# Script de sincronização de todos os forks da organização arsenal-open-source
# Uso: .\scripts\sync-arsenal.ps1

Write-Host "=== SINCRONIZANDO REPOSITÓRIOS DO ARSENAL-OPEN-SOURCE ===" -ForegroundColor Cyan

$repos = gh repo list arsenal-open-source --fork --limit 500 --json nameWithOwner -q '.[].nameWithOwner'

$total = $repos.Count
$sucessos = 0
$falhas = 0
$idx = 1

foreach ($repo in $repos) {
    Write-Host "[$idx/$total] Sincronizando: $repo..." -ForegroundColor Yellow
    gh repo sync $repo
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  -> Sincronizado com sucesso!" -ForegroundColor Green
        $sucessos++
    } else {
        Write-Host "  -> Falha ou sem alterações upstream" -ForegroundColor DarkGray
        $falhas++
    }
    $idx++
}

Write-Host "`n=== RESUMO DA SINCRONIZAÇÃO ===" -ForegroundColor Cyan
Write-Host "Total: $total | Sucessos: $sucessos | Falhas/Sem diff: $falhas"
