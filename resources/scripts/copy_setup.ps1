<#
.SYNOPSIS
This script handles the setup of a Python project by extracting the setup.py file from a tar.gz archive.

.DESCRIPTION
This script removes the existing setup.py file (if it exists), extracts the setup.py file from a tar.gz archive,
and moves it to the current directory.

.PARAMETER File
The path to the tar.gz archive containing the setup.py file.

.PARAMETER ProjectName
The name of the Python project.

.PARAMETER ProjectVersion
The version of the Python project.

.NOTES
Author: Your Name
Version: 1.0
Copyright: (c) Your Organization
#>

# Standard PowerShell header (optional but recommended)
<#
.SAMPLE
PS> .\SetupPythonProject.ps1 -File "C:\path\to\project.tar.gz" -ProjectName "baseblock" -ProjectVersion "0.1.41"
#>

param (
    [string]$File = 'setup.py',
    [string]$ProjectName = "baseblock",
    [string]$ProjectVersion = "0.1.41"
)

# Remove the existing setup.py file if it exists
if (Test-Path -Path $File -PathType Leaf) {
    Remove-Item $File
}

# Extract the setup.py file from the tar.gz archive
Push-Location dist
tar -xf ".\$ProjectName-$ProjectVersion.tar.gz"
Move-Item ".\$ProjectName-$ProjectVersion\setup.py" ../.
Remove-Item "$ProjectName-$ProjectVersion" -Recurse
Pop-Location
