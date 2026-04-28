# ✂️ Premiere Auto Cut Extension

A lightweight Adobe Premiere Pro panel that automatically removes silence from clips and imports the cleaned timeline with a single click.

Built for editors who want speed, not repetitive trimming.

---

## 🚀 What it does

1. Select a video clip in Premiere
2. Click **Auto-Cut Clip**
3. Silence is removed automatically
4. A new edited timeline is imported

No manual cutting. No timeline scrubbing.

---

## ✨ Features

* 🎯 One-click auto-cut workflow
* ⚡ Uses Auto-Editor for fast silence removal
* 📥 Automatically imports XML timeline into Premiere
* 🧩 Clean panel UI inside Premiere
* 🛠 Works directly with selected clips

---

## 🛠 Requirements

Before using this extension, make sure you have:

* Adobe Premiere Pro
* Python 3.x installed
* Auto-Editor installed

Install Auto-Editor:

pip install auto-editor

Verify installation:

auto-editor --help

---

## 📦 Installation

### Option 1 (Recommended)

1. Download this repository
2. Run:

python build_plugin.py

3. Move the generated folder to:

C:\Program Files (x86)\Common Files\Adobe\CEP\extensions\

4. Restart Premiere Pro

---

### Option 2 (Manual)

1. Copy the plugin folder
2. Paste it into:

C:\Program Files (x86)\Common Files\Adobe\CEP\extensions\

3. Restart Premiere Pro

---

## ▶️ How to Use

1. Open Premiere Pro
2. Import your video
3. Select the clip in the Project panel
4. Open the extension panel
5. Click **Auto-Cut Clip**

The edited version will appear automatically in your timeline.

---

## ⚠️ Notes & Troubleshooting

* If nothing happens:

  * Make sure a clip is selected
  * Make sure Auto-Editor is installed

* If you get an error:

  * Try running Auto-Editor manually in terminal
  * Ensure it is added to your system PATH

* Large files may take time to process

---

## 🧠 How it works

* The extension retrieves the selected clip path from Premiere
* Runs Auto-Editor via a local command
* Generates an XML timeline
* Imports the timeline back into Premiere

---

## 🔐 Safety

* No data is uploaded anywhere
* All processing happens locally on your machine

---

## 📜 License

MIT

---

## 💡 Future Ideas

* Built-in Auto-Editor installer
* Preset cutting modes (aggressive / balanced)
* UI settings panel

---

## 🤝 Contributing

Feel free to fork, improve, or suggest features.

---

Make editing less clicking, more creating 🎬

------------------------------------------------------------------------------------

## 🔗 Works with OBS Overlay

Pair this with the OBS notification overlay for a smoother workflow:

👉 **OBS Notification Overlay**

* See recording status live
* Get visual feedback while capturing
* Combine recording + auto-editing workflow

➡️ https://github.com/gamerz-workflows/obs-shadowplay-overlay
