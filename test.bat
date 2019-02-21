@echo off

SET /A "counter = 0"

:while
if %counter% leq 5 (
        echo %counter%
        SET /A "counter = counter+1"
        goto while
)
pause