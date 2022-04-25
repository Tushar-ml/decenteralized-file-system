
# Decenteralized Uncensored system

Checkout the dApp: http://decenter-protect.herokuapp.com/

## Steps to Follow:
Before Clicking on above link, let's walthrough the prerequisites to test:
* Enable Metamask or prefered wallet extension in your browser. [Metamask Extension](https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn?hl=en)
* Switch to Ropsten Test Network.
* Ask for Test Ether from Faucets, if you don't have any. [Test Ether for Ropsten](https://faucet.egorfine.com/)
* Open the above app and enjoy. (Don't Judge on UI, I am a Backend Guy :sweat_smile:)

## Features:
* **Upload File:** You can upload the file, and press submit. After that Click on Add to Contract, to add it in blockchain. Some Gas Fees will be taken.
* **User Info:** You can get Info related to user, to checkout this feature, copy and paste your id from wallet into given box, following details will be popped up:
	* User Id
	* Uploaded File Count
	* Total Bytes Uploaded
* **File Info:** You can get Info related to File like filename, file size and uploaded by, by entering file id. You can get file id from Go to Directory button in bottom of the page.
* **Download File:** You can download the file by entering FileId
* **Remove File:** You can remove any file from contract if you are the owner of that file, otherwise it will not remove it. (Here Gas Fees is charged).

## Technology Used:
* Python
* Solidity
* Docker
* Storj (Decentralized Cloud Storage)
* HTML
* Heroku
