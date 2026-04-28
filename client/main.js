var csInterface = new CSInterface();
var fs = require('fs');
var child_process = require('child_process');

document.getElementById("runBtn").addEventListener("click", function() {
    var status = document.getElementById("status");
    status.innerText = "🔍 Finding clip...";
    status.style.color = "#FFD700";

    csInterface.evalScript('getSelectedFilepath()', function(result) {
        if (result === "false" || !result) {
            status.innerText = "❌ No clip selected!\nPlease select a video in the Project Bin.";
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
            var cleanXmlPath = xmlPath.replace(/\\/g, "\\\\");

            status.innerText = "📥 Importing Timeline...";
            csInterface.evalScript('importXML("' + cleanXmlPath + '")', function(res){
                status.innerText = "✅ Done! Look at your timeline.";
                status.style.color = "#55FF55";
            });
        });
    });
});