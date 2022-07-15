<#
    .SYNOPSIS
    Ecrypt Text

    .DESCRIPTION
    Encrypt any Input Text

    .INPUTS
    None. You cannot pipe objects to Add-Extension.

    .OUTPUTS
    Single txt File

    .EXAMPLE
    PS> .\scripts\Run-Encrypt.ps1 "012345"
#>

param(
    [Parameter(Mandatory = $True)] [System.String] $InputText
)
poetry run python .\baseblock\crypto_base.py "encrypt" $InputText


## --------------------------------------------------------------------------------------------------------------------------------------------------------- ##
## Purpose:         Encrypt Text
## --------------------------------------------------------------------------------------------------------------------------------------------------------- ##
## Sample Usage     .\scripts\Run-Encrypt.ps1 "012345"
## --------------------------------------------------------------------------------------------------------------------------------------------------------- ##
