const fs = require("fs");
const path = require('path');

var root = __dirname;

var allFiles = [];


searchDir(root);

// console.log(allFiles);
for (let i = 0; i < allFiles.length; i++) {
    trimFile(allFiles[i]);
}


function searchDir(dir) {
    var files = fs.readdirSync(dir);

    for (var i = 0; i < files.length; i++) {
        var curPath = path.join(dir, files[i]);
        var fileStat = fs.statSync(curPath);
        if (fileStat.isDirectory()) {
            searchDir(curPath);
        } else {
            allFiles.push(curPath)
        }
    }
}

function trimFile(filePath) {
    if (filePath.includes(".md")) {
        let cnt = 0;
        let data = fs.readFileSync(filePath);
        let content = data.toString();

        while (content.includes('C:\\Users\\Chao\\我的坚果云\\Notes\\')) {
            content = content.replace('C:\\Users\\Chao\\我的坚果云\\Notes\\', '');
            cnt++
        }

        while (content.includes('C:\\Users\\Chao\\AppData\\Roaming\\Typora\\typora-user-images')) {
            content = content.replace('C:\\Users\\Chao\\AppData\\Roaming\\Typora\\typora-user-images', 'images');
            cnt++
        }

        if (cnt > 0) {
            fs.writeFileSync(filePath, content);
            console.log(filePath + " " + cnt);
        }
    }
}
