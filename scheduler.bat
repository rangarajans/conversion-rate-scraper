@echo off

:top
    python CurrencyScraper.py
    REM Set timeout time in seconds below - this is how long script will wait 
    REM before next run (unless manually intervened)
    timeout /t 120
    goto top
