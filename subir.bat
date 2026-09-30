@echo off
echo Subiendo cambios a GitHub...
git add .
git commit -m "Actualizacion del catalogo"
git push origin main
echo.
echo ===================================
echo   ¡Pagina actualizada con exito!
echo ===================================
pause
