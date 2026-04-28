import os
import urllib.request

# Name of the plugin folder
plugin_name = "AutoCutPlugin"
base_path = os.path.join(os.getcwd(), plugin_name)

# 1. Create Folder Structure
folders = ["CSXS", "client", "host"]
for folder in folders:
    os.makedirs(os.path.join(base_path, folder), exist_ok=True)

print(f"📂 Created folder structure in {base_path}")

# 2. Define File Contents

manifest_xml = """<?xml version="1.0" encoding="UTF-8"?>
<ExtensionManifest Version="7.0" ExtensionBundleId="com.autocut.free" ExtensionBundleVersion="1.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <ExtensionList>
        <Extension Id="com.autocut.panel" Version="1.0.0" />
    </ExtensionList>
    <ExecutionEnvironment>
        <HostList>
            <Host Name="PPRO" Version="[12.0,99.9]" />
        </HostList>
        <LocaleList>
            <Locale Code="All" />
        </LocaleList>
        <RequiredRuntimeList>
            <RequiredRuntime Name="CSXS" Version="9.0" />
        </RequiredRuntimeList>
    </ExecutionEnvironment>
    <DispatchInfoList>
        <Extension Id="com.autocut.panel">
            <DispatchInfo>
                <Resources>
                    <MainPath>./client/index.html</MainPath>
                    <ScriptPath>./host/index.jsx</ScriptPath>
                    <CEFCommandLine>
                        <Parameter>--enable-nodejs</Parameter>
                        <Parameter>--mixed-context</Parameter>
                    </CEFCommandLine>
                </Resources>
                <UI>
                    <Type>Panel</Type>
                    <Menu>Auto Cut Free</Menu>
                    <Geometry>
                        <Size><Height>300</Height><Width>300</Width></Size>
                    </Geometry>
                </UI>
            </DispatchInfo>
        </Extension>
    </DispatchInfoList>
</ExtensionManifest>"""

index_html = """<!DOCTYPE html>
<html>
<head>
    <style>
        body { background-color: #1d1d1d; color: #b0b0b0; font-family: 'Segoe UI', sans-serif; padding: 15px; display: flex; flex-direction: column; align-items: center; }
        h3 { color: #ffffff; margin-bottom: 10px; }
        button { 
            background: #3EA6FF; color: white; border: none; padding: 12px 20px; 
            width: 100%; font-weight: bold; cursor: pointer; border-radius: 4px; transition: 0.2s;
        }
        button:hover { background: #2684D8; }
        #status { margin-top: 15px; font-size: 12px; color: #888; text-align: center; }
        .note { font-size: 10px; color: #555; margin-top: 20px; }
    </style>
</head>
<body>
    <h3>✂️ Auto Cut Free</h3>
    <p style="font-size: 13px; text-align: center;">Select a clip in your project bin and click below.</p>
    <button id="runBtn">Auto-Cut Clip</button>
    <p id="status">Ready...</p>
    <p class="note">Powered by Auto-Editor</p>

    <script src="CSInterface.js"></script>
    <script src="main.js"></script>
</body>
</html>"""

main_js = """var csInterface = new CSInterface();
var fs = require('fs');
var child_process = require('child_process');

document.getElementById("runBtn").addEventListener("click", function() {
    var status = document.getElementById("status");
    status.innerText = "🔍 Finding clip...";
    status.style.color = "#FFD700";

    csInterface.evalScript('getSelectedFilepath()', function(result) {
        if (result === "false" || !result) {
            status.innerText = "❌ No clip selected!\\nPlease select a video in the Project Bin.";
            status.style.color = "#FF5555";
            return;
        }

        var videoPath = result;
        status.innerText = "⏳ Processing... This may take a minute.";
        
        // This command runs auto-editor. 
        // If it fails, you may need to replace 'auto-editor' with the full path to the exe.
        var command = 'auto-editor "' + videoPath + '" --export premiere';

        child_process.exec(command, function(error, stdout, stderr) {
            if (error) {
                status.innerText = "❌ Error: " + error.message;
                alert("Error: Make sure Python and Auto-Editor are installed and added to PATH.");
                return;
            }

            var xmlPath = videoPath.substring(0, videoPath.lastIndexOf(".")) + ".xml";
            
            // Fix for Windows paths having backslashes
            var cleanXmlPath = xmlPath.replace(/\\\\/g, "\\\\\\\\");

            status.innerText = "📥 Importing Timeline...";
            csInterface.evalScript('importXML("' + cleanXmlPath + '")', function(res){
                status.innerText = "✅ Done! Look at your timeline.";
                status.style.color = "#55FF55";
            });
        });
    });
});"""

index_jsx = """function getSelectedFilepath() {
    var view = app.project.activeItem; 
    if (app.project.rootItem.children.numItems > 0) {
        for (var i = 0; i < app.project.rootItem.children.numItems; i++){
            var item = app.project.rootItem.children[i];
            if (item.isSelected()) {
                return item.getMediaPath();
            }
        }
    }
    return "false";
}

function importXML(xmlPath) {
    if (xmlPath) {
        app.project.importFiles([xmlPath], 1, app.project.rootItem, 0);
    }
}"""

# 3. Write files
with open(os.path.join(base_path, "CSXS", "manifest.xml"), "w", encoding="utf-8") as f: f.write(manifest_xml)
with open(os.path.join(base_path, "client", "index.html"), "w", encoding="utf-8") as f: f.write(index_html)
with open(os.path.join(base_path, "client", "main.js"), "w", encoding="utf-8") as f: f.write(main_js)
with open(os.path.join(base_path, "host", "index.jsx"), "w", encoding="utf-8") as f: f.write(index_jsx)

print("📝 Written all code files.")

# 4. Download Adobe CSInterface.js automatically
print("⬇️  Downloading CSInterface.js...")
url = "https://raw.githubusercontent.com/Adobe-CEP/CEP-Resources/master/CEP_9.x/CSInterface.js"
urllib.request.urlretrieve(url, os.path.join(base_path, "client", "CSInterface.js"))

print(f"✅ SUCCESS! Plugin created at: {base_path}")
print("👉 MOVE THIS FOLDER TO: C:\\Program Files (x86)\\Common Files\\Adobe\\CEP\\extensions\\")