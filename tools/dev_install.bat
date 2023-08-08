@echo off

:: The path to Blender
SET "blender_config_path=%appData%\Blender Foundation\Blender\3.6"

:: The repo and dependencies
SET repoPath=%~dp0..
SET src_name=dublast
SET "dublf_path=%repoPath%\..\DuBLF\dublf"

:: Need admin to create symlinks
@echo off
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)
:: Get back to original dir
pushd "%CD%"
CD /D "%~dp0"

:: get/create scripts path
md "%blender_config_path%\scripts"
md "%blender_config_path%\scripts\addons"
SET "addons_path=%blender_config_path%\scripts\addons"

:: Remove current version
rd /s /q "%addons_path%\%src_name%"
md "%addons_path%\%src_name%"

:: Link main files
for /f %%a IN ('dir /b "%repoPath%\%src_name%\*.py"') do mklink "%addons_path%\%src_name%\%%a" "%repoPath%\%src_name%\%%a"

:: link dublf
md "%addons_path%\%src_name%\dublf"
for /f %%a IN ('dir /b "%dublf_path%\*.py"') do mklink "%addons_path%\%src_name%\dublf\%%a" "%dublf_path%\%%a"

echo "Done!"
pause