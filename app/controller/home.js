'use strict';
// import {PythonShell} from 'python-shell';
const PythonShell = require('python-shell').PythonShell;

module.exports = app => {
  class HomeController extends app.Controller {
    * index() {
      const ctx = this.ctx;
      ctx.body = yield ctx.renderView('index.tpl');
    }

    async calculate() {
      const ctx = this.ctx;
      const body = ctx.request.body;
      const result = await handlePython(body.n, body.ll, body.hh, body.lh, body.za, body.lra, body.w)
      const pressure = result[0].split(/[\n]/g)[1].replace(/\[|]/g,'');
      const impulses = result[1].replace(/\[|]/g,'');
      const t0 = result[2].replace(/\[|]/g,'');
      if( result ) {
        // ctx.redirect('/')
        await ctx.render('index.tpl', {pressure: pressure, impulses: impulses, t0: t0})
      }
    }
  }
  return HomeController;
};
function handlePython(n, ll, hh, lh, za, lra, w){
  let options = {
    mode: 'text',
    pythonPath: 'C:/Users/Dou-Zi.Dou/AppData/Local/Continuum/anaconda3/envs/tutorials/python.exe',
    pythonOptions: ['-u'],
    scriptPath: 'C:/Users/Dou-Zi.Dou/Downloads/Calculators/grf_to_excel/app/controller/python',
    // n, ll, hh, lh, za, lra
    args: [n, ll, hh, lh, za, lra, w]
  };
  return new Promise((resolve, reject)=>{
    PythonShell.run('run.py', options, function (err, results) {
      if (err) throw err;
      resolve(results);
    })
  })
}
