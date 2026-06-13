const { app, BrowserWindow, session, ipcMain } = require('electron');
const path = require('path');

function createWindow() {
  const mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
      enableRemoteModule: true,
    },
  });

  mainWindow.loadFile('index.html');
  // mainWindow.webContents.openDevTools(); // Optional: Open DevTools

  // Handle IPC requests to update headers
  ipcMain.on('set-headers', (event, { userAgent, cookie }) => {
    // Clear existing headers
    session.defaultSession.webRequest.onBeforeSendHeaders(null);

    // Set new headers
    session.defaultSession.webRequest.onBeforeSendHeaders((details, callback) => {
      details.requestHeaders['User-Agent'] = userAgent;
      details.requestHeaders['Cookie'] = cookie;
      callback({ cancel: false, requestHeaders: details.requestHeaders });
    });

    // Notify the renderer process that headers are set
    event.reply('headers-set');
  });
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});