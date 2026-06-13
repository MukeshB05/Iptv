# Dhara - A Modern Streaming App

Dhara is a modern streaming application built with **Electron**, **HLS.js**, and **Plyr**. It allows users to stream live TV channels, manage favorites, and search for channels effortlessly. The app is designed to be lightweight, user-friendly, and highly customizable. 

**Disclaimer**: Dhara is merely a wrapper and a fun project. It does not host any content itself and is not intended to harm or infringe on any copyrights. All channel links and data are sourced from third-party repositories, and Dhara acts as a front-end interface for streaming.


![dhara-1z-OUg-Nv-R0p.png](https://i.postimg.cc/bNPXNX83/dhara-1z-OUg-Nv-R0p.png) 

---

## Features

1. **Live TV Streaming**:
   - Stream live TV channels using HLS (HTTP Live Streaming) protocol.
   - Supports adaptive bitrate streaming for smooth playback.

2. **Favorites Management**:
   - Add or remove channels to/from your favorites list.
   - Favorites are saved locally using `localStorage`.

3. **Search Functionality**:
   - Quickly search for channels by name.

4. **Responsive Design**:
   - Works seamlessly on both desktop and mobile devices.

5. **Customizable Headers**:
   - Set custom `User-Agent` and `Cookie` headers for each channel.

6. **Video Player**:
   - Built with **Plyr**, a modern and customizable HTML5 video player.
   - Supports fullscreen mode, volume control, and playback speed.

7. **Cross-Platform**:
   - Built with **Electron**, making it compatible with Windows, macOS, and Linux.

---

## Prerequisites

Before building and running Dhara locally, ensure you have the following installed:

- **Node.js** (v16 or higher)
- **npm** (v8 or higher)
- **Git** (optional, for cloning the repository)

---

## How to Build and Run Locally

### Step 1: Clone the Repository
If you have Git installed, clone the repository using the following command:
```bash
git clone https://github.com/your-username/dhara.git
cd dhara
```

Alternatively, you can download the repository as a ZIP file and extract it.

### Step 2: Install Dependencies
Navigate to the project directory and install the required dependencies:
```bash
npm install
```

### Step 3: Run the App
To start the app in development mode, use the following command:
```bash
npm start
```

This will launch the Electron app with the development tools enabled.

---

## Building for Production

To package the app for production, follow these steps:

### Step 1: Install Electron Forge
If you haven't already installed Electron Forge globally, do so with:
```bash
npm install -g @electron-forge/cli
```

### Step 2: Package the App
Run the following command to package the app for your current platform:
```bash
npm run package
```

This will create a distributable package in the `out` directory.

### Step 3: Create Installers
To create platform-specific installers (e.g., `.exe`, `.dmg`, `.deb`), use:
```bash
npm run make
```

The installers will be generated in the `out/make` directory.

---

## Project Structure

```
dhara/
├── main.js               # Main Electron process file
├── index.html            # Main HTML file for the app
├── styles.css            # Global styles for the app
├── package.json          # Project dependencies and scripts
├── icon/                 # App icons for different platforms
├── out/                  # Output directory for packaged builds
└── README.md             # This file
```

---

## Customization

### Adding Channels
To add or modify channels, update the `channels` array in the `index.html` file. Each channel should have the following structure:
```json
{
  "name": "Channel Name",
  "logo": "https://path-to-logo.png",
  "link": "https://path-to-stream.m3u8",
  "userAgent": "Custom User-Agent",
  "cookie": "Custom Cookie"
}
```

### Changing the App Icon
Replace the icons in the `icon/` directory with your own. Ensure the filenames remain the same:
- `icon.ico` (Windows)
- `icon.png` (Linux/macOS)

### Modifying Styles
The app's styles are defined in the `<style>` block within `index.html`. You can customize the colors, fonts, and layout as needed.

---

## Troubleshooting

### 1. HLS Playback Issues
- Ensure the stream URL is valid and accessible.
- Check the browser console for any HLS-related errors.
- If using Safari, ensure the stream supports native HLS playback.

### 2. Build Errors
- Ensure all dependencies are installed correctly by running `npm install`.
- If the build fails, try clearing the `node_modules` directory and reinstalling dependencies:
  ```bash
  rm -rf node_modules
  npm install
  ```

### 3. App Crashes on Launch
- Check the terminal for any error messages.
- Ensure the `main.js` file is correctly configured and points to the right HTML file.

---

## Credits

Dhara uses channel links and headers sourced from the following repository:
- **[Toffee-Channels-Link-Headers](https://github.com/byte-capsule/Toffee-Channels-Link-Headers)** by [byte-capsule](https://github.com/byte-capsule).

Special thanks to the original creators and copyright owners of the content. Dhara is merely a wrapper and does not host or distribute any content. It is intended for educational and personal use only.

---

## Contributing

Contributions are welcome! If you'd like to contribute to Dhara, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request on GitHub.

---

## License

Dhara is licensed under the **MIT License**.

---

## Acknowledgments

- **Electron**: For providing the framework to build cross-platform desktop apps.
- **HLS.js**: For enabling HLS playback in browsers that don't natively support it.
- **Plyr**: For the beautiful and functional video player.
- **[byte-capsule](https://github.com/byte-capsule)**: For providing the channel links and headers.

---

Enjoy streaming with Dhara! 🎥
