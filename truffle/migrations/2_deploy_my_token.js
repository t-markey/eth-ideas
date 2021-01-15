const MyToken = artifacts.require('./MyTok.sol')
module.exports = function(deployer) {
  deployer.deploy(MyToken)
}
