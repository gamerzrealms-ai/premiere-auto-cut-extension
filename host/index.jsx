function getSelectedFilepath() {
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
}