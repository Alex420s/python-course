#!/usr/bin/env bash
CHROME_VERSION="google-chrome-stable"

# Descargar e instalar Chrome
apt-get update
# Instala las herramientas wget y gnupg2.
# gnupg2 se usa para la autenticación de claves de firma, necesaria para verificar la autenticidad del software que se está instalando.
apt-get install -y wget gnupg2
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
apt-get update
apt-get install -y $CHROME_VERSION
