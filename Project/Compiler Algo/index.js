let express = require("express");
let path = require("path");
let bodyParser = require("body-parser");
let compiler = require("compilex");

let options = {stats : true};
compiler.init(options);
let app = express();
app.use(bodyParser());
app.get("/", function (req, res) {
  res.sendfile(__dirname + "/index.html");
});
app.post("/yourresult", function (req, res) {
  let code = req.body.code;
  let input = req.body.input;
  let withinput = req.body.withinput;
  let language = req.body.language;
  if (language === "C" || language === "C++") {
    if (withinput === "true") {
      let envData = { OS: "windows", cmd: "g++", options: { timeout: 100000 } };
      compiler.compileCPPWithInput(envData, code, input, function (data) {
          res.send(data.output);
        
      });
    } else {
      let envData = { OS: "windows", cmd: "g++", options: { timeout: 100000 } };
      compiler.compileCPP(envData, code, function (data) {
        res.send(data);
      });
    }
  }
  if (language === "Python") {
    if (withinput === "true") {
      let envData = { OS: "windows", options: { timeout: 100000 } };
      compiler.compilePythonWithInput(envData, code, input, function (data) { 
          res.send(data.output);
        
      });
    } else {
      let envData = { OS: "windows",options: { timeout: 100000 } };
      compiler.compilePython(envData, code, function (data) {
        res.send(data);
      });
    }
  }
  if (language === "Java") {
    if (withinput === "true") {
       let envData = { OS: "windows" ,options: { timeout: 100000 } };
       compiler.compileJavaWithInput( envData , code , input ,  function(data){
          res.send(data.output);
    });
    } else {
      let envData = { OS: "windows",options: { timeout: 100000 }  };
      compiler.compileJava( envData , code , function(data){
          res.send(data);
      
    });
    }
  }
  if(language == 'C#'){
    if(withinput == 'true'){
      let envData = {OS:"windows", options : {timeout:100000}};
      compiler.compileCSWithInput(envData,code,function(data){
        res.send(data);
      });
    }else{
      let envData = {OS:"windows", options : {timeout:100000}};
      compiler.compileCS(envData,code,function(data){
        res.send(data);
      });
    }
  }
});
app.get("/fullStat", function (req, res) {
  compiler.fullStat(function (data) {
    res.send(data);
  });
});

app.listen(1337, function(){
  console.log('Port:', this.address().port);
});
compiler.flushSync();