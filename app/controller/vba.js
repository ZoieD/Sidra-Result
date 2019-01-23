'use strict';

const fs = require('fs');
const path = require('path');
const sendToWormhole = require('stream-wormhole');
const PythonShell = require('python-shell').PythonShell;

module.exports = app => {
    class VbaController extends app.Controller {
        * vba() {
            const ctx = this.ctx;
            ctx.body = yield ctx.renderView('vba.tpl');
        }

        * upload() {
            const ctx = this.ctx;
            const stream = yield ctx.getFileStream();
            const saveFileName = new Date().getTime() + stream.filename;
            let filepath = path.join(this.app.config.baseDir, `app/public/uploads/${saveFileName}`);

            if (stream.fields.title === 'mock-error') {
                filepath = path.join(this.app.config.baseDir, `app/public/uploads/not-exists/dir/${saveFileName}`);
            } else if (stream.fields.title === 'mock-read-error') {
                filepath = path.join(this.app.config.baseDir, `app/public/uploads/read-error-${saveFileName}`);
            }
            this.logger.warn('Saving %s to %s', stream.filename, filepath);
            try {
                yield saveStream(stream, filepath);
            } catch (err) {
                yield sendToWormhole(stream);
                throw err;
            }
            const result = yield handlePython(filepath);
            // console.log(ctx.request.header.host);
            if(result) {
                const url = result[0].replace(/\[|]/g, '');
                const name =  path.basename(url, '.xls');
                const dirName = '/public/uploads/' + name + '.xls';
                console.log('xxxxxxxxx',ctx.request.header.host + dirName);
                // yield this.ctx.curl(ctx.request.header.host + dirName);

                ctx.redirect('http://' + ctx.request.header.host + dirName);
            }

        }
    }

    return VbaController;
};

function saveStream(stream, filepath) {
    return new Promise((resolve, reject) => {
        if (filepath.indexOf('/read-error-') > 0) {
            stream.once('readable', () => {
                const buf = stream.read(10240);
                console.log('read %d bytes', buf.length);
                setTimeout(() => {
                    reject(new Error('mock read error'));
                }, 1000);
            });
        } else {
            const ws = fs.createWriteStream(filepath);
            stream.pipe(ws);
            ws.on('error', reject);
            ws.on('finish', resolve);
        }
    });
}

function handlePython(path){
    let options = {
        mode: 'text',
        pythonPath: 'C:/Users/Dou-Zi.Dou/AppData/Local/Continuum/anaconda3/envs/tutorials/python.exe',
        pythonOptions: ['-u'],
        scriptPath: 'C:/Users/Dou-Zi.Dou/Downloads/Calculators/grf_to_excel/app/controller/vba',
        args: [path]
    };
    return new Promise((resolve, reject)=>{
        PythonShell.run('run.py', options, function (err, results) {
            if (err) throw err;
            resolve(results);
        })
    })
}
