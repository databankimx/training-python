# setup.ps1
#
# Runs the quickstart's setup steps in order (QUICKSTART.md, steps 2 to 7):
#   1. Checks that Python 3.10 or later is available (3.12 is the tested version).
#   2. Creates the repository environment (.venv) and installs the runner and lesson libraries.
#   3. Installs MathJax and Prism into lesson-runner\vendor (needs Node.js).
#   4. Creates the web applications environment (part-ii-projects\web-applications\.venv) and installs its packages.
#   5. Copies the VS Code settings into .vscode (backs up an existing file only if it's different).
#   6. Checks for the GitHub token used by Chapter 17.
#
# With -InstallMissing, the script uses winget to install Python 3.12 and Node.js if they're missing.
# Without it, the script only reports what's missing, and shows the winget commands to run.
#
# Safe to run again: each step checks what's already in place. Nothing here creates an admin account, runs a lesson,
# or changes machine-wide settings.
#
# Run from the repository root with:
#   powershell -ExecutionPolicy Bypass -File .\setup.ps1
#   powershell -ExecutionPolicy Bypass -File .\setup.ps1 -InstallMissing

param(
    [switch]$InstallMissing
)

$ErrorActionPreference = "Stop"
$root = $PSScriptRoot
Set-Location $root

$script:warnings = @()
$script:results = [ordered]@{}

function Write-Step([string]$title) {
    Write-Host ""
    Write-Host "== $title ==" -ForegroundColor Cyan
}

function Write-Note([string]$message) {
    Write-Host "   $message"
}

function Add-Warning([string]$message) {
    $script:warnings += $message
    Write-Host "   WARNING: $message" -ForegroundColor Yellow
}

function Stop-Setup([string]$message) {
    Write-Host ""
    Write-Host "SETUP STOPPED: $message" -ForegroundColor Red
    Write-Host "Fix the problem above, then run this script again. Steps already done will be skipped."
    exit 1
}

# Runs a program and stops the script if it returns a non-zero exit code. PowerShell doesn't do this for native programs by itself.
function Invoke-Checked([string]$program, [string[]]$arguments) {
    & $program @arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Command failed: $program $($arguments -join ' ')"
    }
}

# winget installs update the registry's PATH, but this PowerShell window still has the old one. Reload it, so new programs are found.
function Update-SessionPath {
    $machinePath = [Environment]::GetEnvironmentVariable("Path", "Machine")
    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
    $env:Path = "$machinePath;$userPath"
}

function Get-PythonVersion {
    try {
        $version = (& python -c "import sys; print('%d.%d' % sys.version_info[:2])" 2>$null)
        if ($LASTEXITCODE -eq 0 -and $version) {
            return $version.Trim()
        }
    } catch {
        return $null
    }
    return $null
}

# Installs a package with winget. Returns $true when it works, and $false otherwise, so the caller decides whether that's fatal.
function Install-WithWinget([string]$id, [string]$label) {
    if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
        Write-Note "winget isn't available on this computer, so $label can't be installed automatically."
        return $false
    }
    Write-Note "Installing $label with winget (package id: $id). This can take several minutes..."
    & winget install --id $id -e --accept-package-agreements --accept-source-agreements
    if ($LASTEXITCODE -ne 0) {
        Write-Note "winget didn't install $label (exit code $LASTEXITCODE). Company policy can block winget installs. Ask IT, or install it by hand."
        return $false
    }
    Update-SessionPath
    return $true
}

# 1. Python ---------------------------------------------------------------------------------------

Write-Step "1. Python 3.12 or later"
$pythonVersion = Get-PythonVersion
if (-not $pythonVersion) {
    if ($InstallMissing) {
        Write-Note "Python isn't on PATH, so it will be installed."
        if (Install-WithWinget "Python.Python.3.12" "Python 3.12") {
            $pythonVersion = Get-PythonVersion
        }
    }
    if (-not $pythonVersion) {
        Stop-Setup ("Python isn't installed, or isn't on PATH. Either:`n" +
            "   - run this script with -InstallMissing, which uses winget, or`n" +
            "   - install it yourself: winget install --id Python.Python.3.12 -e`n" +
            "     (or Python 3.12 from python.org, with 'Add python.exe to PATH' ticked).`n" +
            "   Then open a new PowerShell window and run this script again.")
    }
}
if ([version]$pythonVersion -lt [version]"3.10") {
    Stop-Setup "Python $pythonVersion was found. Python 3.12 or later is needed. Install 3.12 with: winget install --id Python.Python.3.12 -e"
}
Write-Note "Found Python $pythonVersion."

$tkOk = $true
try { & python -c "import tkinter" 2>$null | Out-Null; if ($LASTEXITCODE -ne 0) { $tkOk = $false } } catch { $tkOk = $false }
if (-not $tkOk) {
    Add-Warning "tkinter isn't available. The Tkinter chapter needs it. winget doesn't always include it: run the Python 3.12 installer from python.org again, choose Modify, and tick 'tcl/tk and IDLE'."
}
$script:results["Python $pythonVersion"] = "ok"

# Node.js is only needed for the math and code display, so a missing Node.js is a warning, not a stop.
$npm = Get-Command npm -ErrorAction SilentlyContinue
if (-not $npm -and $InstallMissing) {
    Write-Note "Node.js isn't on PATH, so it will be installed."
    if (Install-WithWinget "OpenJS.NodeJS.LTS" "Node.js LTS") {
        $npm = Get-Command npm -ErrorAction SilentlyContinue
    }
}
if (-not $npm) {
    Add-Warning "Node.js (npm) isn't installed. Install it with: winget install --id OpenJS.NodeJS.LTS -e (or the LTS version from nodejs.org), then run this script again. Until then, lessons show math and code as plain text."
}

# 2. Repository environment -------------------------------------------------------------------------

Write-Step "2. Repository environment (.venv) and lesson libraries"
$repoPython = Join-Path $root ".venv\Scripts\python.exe"
if (Test-Path $repoPython) {
    Write-Note "The .venv already exists, so it's reused."
} else {
    Write-Note "Creating .venv in the repository root..."
    Invoke-Checked "python" @("-m", "venv", (Join-Path $root ".venv"))
}

Write-Note "Installing the runner's packages (lesson-runner\requirements.txt)..."
Invoke-Checked $repoPython @("-m", "pip", "install", "--upgrade", "pip")
Invoke-Checked $repoPython @("-m", "pip", "install", "-r", "lesson-runner\requirements.txt")

Write-Note "Installing the lesson libraries. This can take a few minutes the first time..."
$lessonLibraries = @(
    "pytest", "pygame", "matplotlib", "requests", "plotly", "sm-utils",
    "beautifulsoup4", "mechanicalsoup", "numpy", "pandas", "seaborn", "scipy",
    "pyperclip", "build", "twine", "pymongo", "mysql-connector-python"
)
Invoke-Checked $repoPython (@("-m", "pip", "install") + $lessonLibraries)

Invoke-Checked $repoPython @("-c", "import PySide6, markdown_it, pygame, matplotlib, pandas, pytest; print('Repository environment imports: ok')")
$script:results["Repository environment"] = "ok"

# 3. MathJax and Prism -------------------------------------------------------------------------------

Write-Step "3. MathJax and Prism (lesson math and code display)"
$vendor = Join-Path $root "lesson-runner\vendor"
$mathJaxFile = Join-Path $vendor "node_modules\mathjax\es5\tex-svg.js"
$prismFile = Join-Path $vendor "node_modules\prismjs\prism.js"
if ((Test-Path $mathJaxFile) -and (Test-Path $prismFile)) {
    Write-Note "MathJax and Prism are already installed."
    $script:results["MathJax and Prism"] = "ok"
} elseif (-not $npm) {
    Add-Warning "Skipped: Node.js isn't installed, so MathJax and Prism weren't set up. Lessons will show math and code as plain text until this is done."
    $script:results["MathJax and Prism"] = "skipped"
} else {
    Push-Location $vendor
    try {
        if (-not (Test-Path (Join-Path $vendor "package.json"))) {
            Invoke-Checked "npm" @("init", "-y")
        }
        Invoke-Checked "npm" @("install", "mathjax@3", "prismjs@1")
    } finally {
        Pop-Location
    }
    if ((Test-Path $mathJaxFile) -and (Test-Path $prismFile)) {
        Write-Note "MathJax and Prism installed."
        $script:results["MathJax and Prism"] = "ok"
    } else {
        Stop-Setup "npm finished, but the MathJax or Prism files weren't found under lesson-runner\vendor\node_modules."
    }
}

# 4. Web applications environment ----------------------------------------------------------------------

Write-Step "4. Web applications environment (Django and Flask chapters)"
$webDir = Join-Path $root "part-ii-projects\web-applications"
$webPython = Join-Path $webDir ".venv\Scripts\python.exe"
if (Test-Path $webPython) {
    Write-Note "The web .venv already exists, so it's reused."
} else {
    Write-Note "Creating part-ii-projects\web-applications\.venv..."
    Invoke-Checked "python" @("-m", "venv", (Join-Path $webDir ".venv"))
}

Push-Location $webDir
try {
    Write-Note "Installing the Django packages (chapter 20, step 1)..."
    Invoke-Checked $webPython @("-m", "pip", "install", "-r", "ch20-styling-and-deploying\lessons\01-bootstrap-setup\requirements.txt")
    Write-Note "Installing the Flask packages (Part III, S25, step 1)..."
    Invoke-Checked $webPython @("-m", "pip", "install", "-r", "..\..\part-iii-beyond-the-book\s25-flask-learning-log\01-flask-setup\requirements.txt")
    Invoke-Checked $webPython @("-c", "import django, django_bootstrap5, flask, sqlalchemy; print('Web environment imports: ok')")
} finally {
    Pop-Location
}
$script:results["Web environment"] = "ok"

# 5. VS Code settings --------------------------------------------------------------------------------

Write-Step "5. VS Code settings"
$vscodeSource = Join-Path $root "resources\vscode\settings.json"
$vscodeDir = Join-Path $root ".vscode"
$vscodeTarget = Join-Path $vscodeDir "settings.json"
New-Item -ItemType Directory -Force $vscodeDir | Out-Null

$sourceHash = (Get-FileHash $vscodeSource -Algorithm SHA256).Hash
if (Test-Path $vscodeTarget) {
    $targetHash = (Get-FileHash $vscodeTarget -Algorithm SHA256).Hash
    if ($targetHash -eq $sourceHash) {
        Write-Note "The VS Code settings are already in place."
        $script:results["VS Code settings"] = "ok"
    } else {
        $backup = Join-Path $vscodeDir ("settings.json.backup-" + (Get-Date -Format "yyyyMMdd-HHmmss"))
        Copy-Item $vscodeTarget $backup
        Copy-Item $vscodeSource $vscodeTarget -Force
        Write-Note "Replaced the existing settings. Your old file is saved as $(Split-Path $backup -Leaf)."
        Write-Note "Reload VS Code (Ctrl+Shift+P, then Developer: Reload Window)."
        $script:results["VS Code settings"] = "updated"
    }
} else {
    Copy-Item $vscodeSource $vscodeTarget
    Write-Note "Copied the VS Code settings. Reload VS Code (Ctrl+Shift+P, then Developer: Reload Window)."
    $script:results["VS Code settings"] = "ok"
}

# 6. GitHub token (Chapter 17) -------------------------------------------------------------------------

Write-Step "6. GitHub token (Data Visualization, Chapter 17)"
$token = [Environment]::GetEnvironmentVariable("GITHUB_TRAINING_TOKEN", "User")
if (-not $token) { $token = $env:GITHUB_TRAINING_TOKEN }
if ($token) {
    Write-Note "GITHUB_TRAINING_TOKEN is set."
    $script:results["GitHub token"] = "ok"
} else {
    Add-Warning "GITHUB_TRAINING_TOKEN isn't set. Chapter 17 needs it, or GitHub's rate limit will stop the exercises. See part-ii-projects\data-visualization\github-token-setup.md."
    $script:results["GitHub token"] = "not set (needed for Chapter 17)"
}

# Summary -------------------------------------------------------------------------------------------

Write-Step "Summary"
foreach ($item in $script:results.GetEnumerator()) {
    Write-Host ("   {0,-30} {1}" -f $item.Key, $item.Value)
}

if ($script:warnings.Count -gt 0) {
    Write-Host ""
    Write-Host "Things to do:" -ForegroundColor Yellow
    foreach ($warning in $script:warnings) {
        Write-Host "   - $warning"
    }
}

Write-Host ""
Write-Host "Setup finished. To start the lesson runner, run this from the repository root:" -ForegroundColor Green
Write-Host "   .venv\Scripts\python.exe lesson-runner\app.py"
Write-Host ""
Write-Host "The first web run asks for an admin username and password. That step can't be done by this script."
