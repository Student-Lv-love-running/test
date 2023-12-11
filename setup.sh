mkdir -p ~/.streamlit/

echo "\
[server]
headless = true
enableCORS = false
enableXsrfProtection = false
port = $PORT
[client]
showErrorDetails = true
[browser]
gatherUsageStats = false
[theme]
base='dark'
primaryColor='#f63366'
backgroundColor='#0e1117'
secondaryBackgroundColor='#262730'
textColor='#ffffff'
font='sans serif'
[deprecation]
showMenu = false
" > ~/.streamlit/config.toml
