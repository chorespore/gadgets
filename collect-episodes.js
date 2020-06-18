const fs = require("fs");
const path = require("path");

const root = path.join(__dirname)
const dst = path.join(root, 'dst');

if (!fs.existsSync(dst)) {
    fs.mkdirSync(dst);
}

scan(root)

function scan(dir) {
    let pa = fs.readdirSync(dir);
    pa.forEach(function (ele, index) {
        let info = fs.statSync(dir + "/" + ele);
        if (info.isDirectory() && !ele.endsWith('dst')) {
            scan(dir + "/" + ele);
        } else {
            if (ele.endsWith('mkv')) {
                let sourceFile = path.join(dir, ele);
                let destPath = path.join(dst, ele);
                fs.renameSync(sourceFile, destPath);
                console.log(sourceFile + ' => ' + destPath);
            }
        }
    })
}
