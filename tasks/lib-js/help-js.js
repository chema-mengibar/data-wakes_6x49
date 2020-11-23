// Read file to JSON
const filePath = `${sourceFolder}\\${file}`;
const contentObj = JSON.parse(fs.readFileSync(filePath));

// Make dir
const outputDir = `${dirPath}\\subDir1\\subDir2`;
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir);
}
