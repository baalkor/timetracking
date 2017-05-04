function init(myKey){
AES_Init();
var key = string2Bin(myKey);
AES_ExpandKey(key);
return key;
}

function encrypt ( inputStr,key ) {
var block = string2Bin(inputStr);
AES_Encrypt(block, key);
var data=bin2String(block);
return data;
}
function decrypt ( inputStr,key ) {
block = string2Bin(inputStr);
AES_Decrypt(block, key);
var data=bin2String(block);
return data;
}
function encryptLongString ( xMyString,key ) {
myString = xMyString.toString();
if(myString.length>16){
var data='';
for(var i=0;i<myString.length;i=i+16){
data+=encrypt(myString.substring(i,16),key);
}
return data;
}else{
return encrypt(myString,key);
}
}
function decryptLongString ( myString,key ) {
if(myString.length>16){
var data='';
for(var i=0;i<myString.length;i=i+16){
data+=decrypt(myString.substring(i,16),key);
}
return data;
}else{
return decrypt(myString,key);
}
}
function finish(){
AES_Done();
}
function bin2String(array) {
var result = "";
for (var i = 0; i < array.length; i++) {
result += String.fromCharCode(parseInt(array[i], 2));
}
return result;
}
function string2Bin(str) {
var result = [];
for (var i = 0; i < str.length; i++) {
result.push(str.charCodeAt(i));
}
return result;
}

function bin2String(array) {
return String.fromCharCode.apply(String, array);
}