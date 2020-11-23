const fs = require("fs");

function saveData(fileContent, outputDir, fileName) {
  const content = JSON.stringify(fileContent, null, "\t");
  const filePath = `${outputDir}\\${fileName}`;
  fs.writeFile(filePath, content, (err) => {
    if (err) return err;
  });
}

exports.saveData = saveData;
