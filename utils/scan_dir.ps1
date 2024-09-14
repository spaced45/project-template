# Define the paths
$rootPath = 'C:\Users\ville\OneDrive\Documents\VSCode\project-template'
$exportPath = 'C:\Users\ville\OneDrive\Documents\VSCode\project-template\utils\directory_structure.txt'

# Get all items at the root level
$items = Get-ChildItem -Path $rootPath -Directory

# Filter out .git and venv folders
$filteredItems = $items | Where-Object { $_.Name -ne '.git' -and $_.Name -ne 'venv' }

# Create or clear the export file
New-Item -Path $exportPath -ItemType File -Force | Out-Null

# Write the directory structure to the text file
foreach ($item in $filteredItems) {
    $item.FullName | Out-File -FilePath $exportPath -Append
}

Write-Host "Directory structure has been exported to $exportPath"
