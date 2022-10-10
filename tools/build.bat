@echo off

:: The repo (current dir)
SET repoPath=%~dp0..

:: Output path
SET outputPath=%~dp0\build

SET "src_name=dublast"
SET "dublf_path=%repoPath%\..\DuBLF\dublf"

rd /s /q "%outputPath%\%src_name%"
md "%outputPath%\%src_name%"

:: copy main files
for /f %%a IN ('dir /b "%repoPath%\%src_name%\*.py"') do copy "%repoPath%\%src_name%\%%a" "%outputPath%\%src_name%\%%a"

:: copy dublf
md "%outputPath%\%src_name%\dublf"
for /f %%a IN ('dir /b "%dublf_path%\*.py"') do copy "%dublf_path%\%%a" "%outputPath%\%src_name%\dublf\%%a" 

echo "Done!"
pause