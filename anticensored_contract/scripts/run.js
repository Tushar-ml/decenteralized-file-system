const main = async () => {
    const [owner, randomPerson] = await hre.ethers.getSigners();
    const ProtectedFileFactory = await hre.ethers.getContractFactory("ProtectedFile");
    const fileContract = await ProtectedFileFactory.deploy();
    await fileContract.deployed();
    console.log("Contract deployed to:", fileContract.address);

    // let upload = await fileContract.uploadFile('74734676r76r','practicesol',456,'https://www.google.com');
    // await upload.wait();

    upload = await fileContract.connect(randomPerson).uploadFile('74734676r5r','differentsol',1000,'https://www.google.com');
    await upload.wait();

    let uploadCount = await fileContract.getUserInfo(randomPerson.address);
    console.log(uploadCount);

    let fileLink = await fileContract.downloadFile('74734676r5r');
    await fileLink.wait();

    let fileInfo = await fileContract.getFileInfo('74734676r5r');
    console.log(fileInfo);

    let removeFile = await fileContract.removeFile('74734676r5r')
    await removeFile.wait();

    fileInfo = await fileContract.getFileInfo('74734676r5r');
    console.log(fileInfo);
  };
  
  const runMain = async () => {
    try {
      await main();
      process.exit(0); // exit Node process without error
    } catch (error) {
      console.log(error);
      process.exit(1); // exit Node process while indicating 'Uncaught Fatal Exception' error
    }
    // Read more about Node exit ('process.exit(num)') status codes here: https://stackoverflow.com/a/47163396/7974948
  };
  
  runMain();