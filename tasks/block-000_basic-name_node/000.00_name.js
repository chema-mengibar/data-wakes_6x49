const exec = require("child_process").exec;
const fs = require("fs");

const Router = require("../config/Router");

const outputDir = `${Router.stage}\\targetDir`;
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir);
}

// Task here
