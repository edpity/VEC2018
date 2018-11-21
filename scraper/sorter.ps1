Get-ChildItem -Path GitHubDir\VEC2018\scraper\data *.zip -File | sort LastWriteTime -Descending | select -Skip 1 |Remove-Item
Get-ChildItem -Path GitHubDir\VEC2018\scraper\data\xml *.xml -File | sort LastWriteTime -Descending | select -Skip 0 |Remove-Item
Get-ChildItem -Filter *.zip -Recurse GitHubDir\VEC2018\scraper\data | % { $_.FullName } |Split-Path | Get-Unique | % { cd $_; &'C:\Program Files\7-Zip\7z.exe' x *.zip "-oGitHubDir\VEC2018\scraper\data\xml" }
Get-ChildItem -Path GitHubDir\VEC2018\scraper\data\xml -Filter "*State*" -Recurse | Rename-Item -NewName("Data.xml")
Get-ChildItem -Path GitHubDir\VEC2018\scraper\data *.zip -File | sort LastWriteTime -Descending | select -Skip 0 |Remove-Item