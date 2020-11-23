const path = require('path')

const Router = {
    universe: path.join(__dirname, '../../../','data','universe'),
    master: path.join(__dirname, '../../../','data','master'),
    stage: path.join(__dirname, '../../../','data','stage'),
    repo: path.join(__dirname, '../../../','repository','picasso'),
    reports: path.join(__dirname, '../../../','reports')
}

module.exports = Router;
