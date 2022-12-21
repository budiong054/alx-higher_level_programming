#!/usr/bin/node
const { FilesManager } = require('turbodepot-node');
const filesManager = new FilesManager();
const argv = process.argv;
filesManager.mergeFiles([argv[2], argv[3]], argv[4], '\n');
