//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "hardhat/console.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

contract ProtectedFile {
    
    // Uploader Struct: Checks for its access
    struct Uploader {
        address uploaderId;
        uint8 upload_count;
        uint32 upload_bytes; 
    }

    struct File {
        string file_name;
        uint32 file_size;
        string link;
        address uploadedBy;
    }
    mapping(address => Uploader) public uploaders;
    mapping(string => File) public files;

    constructor(){
        console.log("Welcome to ProtectedFile: ",msg.sender);
    }

    function uploadFile(string memory file_id, string memory _file_name, uint32 _file_size, string memory _link) public returns (string memory) {
        // Uploading File Information
        files[file_id].file_name = _file_name;
        files[file_id].file_size = _file_size;
        files[file_id].link = _link;
        files[file_id].uploadedBy = msg.sender;

        // Uploader Info Update
        uploaders[msg.sender].upload_count += 1;
        uploaders[msg.sender].upload_bytes += _file_size;
        return "Successfully Uploaded";
    }
    
    function getUserInfo(address userId) public view returns (address, uint8, uint32) {
        // return (Strings.toHexString(uint160(msg.sender), 20),Strings.toString(uploaders[msg.sender].upload_count));
        return (userId, uploaders[userId].upload_count, uploaders[userId].upload_bytes);
    }

    function getFileInfo(string memory file_id) public view returns (string memory, uint32, address) {
        // return (Strings.toHexString(uint160(msg.sender), 20),Strings.toString(uploaders[msg.sender].upload_count));
        return (files[file_id].file_name, files[file_id].file_size, files[file_id].uploadedBy);
    }

    function downloadFile(string memory file_id) public view returns (string memory){
        return files[file_id].link;
    }

    function removeFile(string memory file_id) public returns (string memory){
        require(files[file_id].uploadedBy == msg.sender, "Invalid Access");
        delete files[file_id];
        return "File Removed";
    }
}