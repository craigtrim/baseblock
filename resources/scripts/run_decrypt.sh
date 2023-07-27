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
    PS> .\scripts\Run-Decrypt.ps1 <key>
#>

param(
    [Parameter(Mandatory = $True)] [System.String] $InputText
)
poetry run python .\baseblock\crypto_base.py "decrypt" $InputText


## --------------------------------------------------------------------------------------------------------------------------------------------------------- ##
## Purpose:         Encrypt Text
## --------------------------------------------------------------------------------------------------------------------------------------------------------- ##
## Sample Usage     .\scripts\Run-Decrypt.ps1 <key>
## --------------------------------------------------------------------------------------------------------------------------------------------------------- ##
