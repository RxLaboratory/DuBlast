@echo off

:: The path to the addon
SET "addons_path=C:\Users\duduf\AppData\Roaming\Blender Foundation\Blender\3.3\scripts\addons"

:: The repo (current dir)
SET repoPath=%~dp0..

:: Need admin to create symlinks
@echo off
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)
:: Get back to original dir
pushd "%CD%"
CD /D "%~dp0"

SET src_name=dublast
SET "dublf_path=%repoPath%\..\DuBLF\dublf"
SET "dupyf_path=%repoPath%\..\..\Python\DuPYF\dupyf"

:: Remove current version
rd /s /q "%addons_path%\%src_name%"
md "%addons_path%\%src_name%"

:: Link main files
for /f %%a IN ('dir /b "%repoPath%\%src_name%\*.py"') do mklink "%addons_path%\%src_name%\%%a" "%repoPath%\%src_name%\%%a"

:: link dublf
md "%addons_path%\%src_name%\dublf"
for /f %%a IN ('dir /b "%dublf_path%\*.py"') do mklink "%addons_path%\%src_name%\dublf\%%a" "%dublf_path%\%%a"

:: link dupyf
for /f %%a IN ('dir /b "%dupyf_path%\*.py"') do mklink "%addons_path%\%src_name%\dublf\%%a" "%dupyf_path%\%%a"

echo "Done!"
pause