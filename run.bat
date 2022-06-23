@echo off
pytest -v -m "sanity" --html=./Reports/sanity_report.html testCases/ --browser chrome  
pause
rem pytest -v -m "sanity and regresion" --html=./Reports/sanityreg_report.html testCases/ --browser chrome  
rem pytest -v -m "sanity or regression" --html=./Reports/sanityreg_report.html testCases/ --browser chrome  
rem pytest -v -m "regresssion" --html=./Reports/regression_report.html testCases/ --browser chrome  

rem pytest -v -m "sanity" --html=./Reports/sanity_report.html testCases/ --browser firefox
rem pytest -v -m "sanity and regresion" --html=./Reports/sanityreg_report.html testCases/ --browser firefox
rem pytest -v -m "sanity or regression" --html=./Reports/sanityreg_report.html testCases/ --browser firefox
rem pytest -v -m "regresssion" --html=./Reports/regression_report.html testCases/ --browser firefox