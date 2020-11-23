const fs = require("fs");
const path = require("path");

const tasksFlagsCnt = fs.readFileSync(path.join(__dirname, "task-flags.json"));
const tasksFlags = JSON.parse(tasksFlagsCnt);

const tasksConfig = {
  runner_flags: {
    ignore_manual_tasks: false,
    ignore_optional_flag: true,
  },
  blocks: {
    block_a: [
      { id: "1", type: "manual", description: "Description of the task" },
      {
        id: "2",
        type: "script",
        cmd: "node tasks/block_a/task-file-name",
        requires_flags: ["task_1_flag"],
      },
    ],
  },
  blocks_priority: ["block_a"],
};

function execShellCommand(cmd) {
  const exec = require("child_process").exec;
  return new Promise((resolve, reject) => {
    exec(cmd, (error, stdout, stderr) => {
      if (error) {
        console.warn(error);
      }
      resolve(stdout ? stdout : stderr);
    });
  });
}

function runTask(_blockName, _id) {
  /*
   * Description:
   * return task-cmd as promise
   *
   * Usage:
   * const taskResult = await runTask('block_a', '4');
   * console.log(taskResult)
   * */
  const task = tasksConfig.blocks[_blockName].find((taskItem) => {
    return taskItem.id === _id;
  });
  return execShellCommand(task.cmd);
}

async function init() {
  console.log("Walk, don`t run!");

  const tt0 = await runTask("block_a", "2");

  console.log(tt0, tt1, tt2, tt3, tt4);
}

init();

/*
    const scriptTasks = tasksConfig.blocks.block_a
        .filter( taskItem =>{
            return taskItem.type === 'script'
        })

    scriptTasks.forEach( async function(taskItem){
        const taskResult = await execShellCommand(taskItem.cmd);
        console.log(taskItem.id, taskResult)
    })
*/
