# REST api serivce for getting the details of indian banks
### Hosted at https://obscure-gorge-31969.herokuapp.com/api
## Working
### It has two url end points
- One for getting the details of the branch using ifsc code.
- other for getting details all the branches of some bank in a particular city given the name and city.
- First url for getting the details of one branch using ifsc code<br />
https://obscure-gorge-31969.herokuapp.com/api/branch_details/?ifsc=<IFSC_CODE> <br/>
For e,g if you want to find the branch details with ifsc code = SBIN0001567 then url will be like this

https://obscure-gorge-31969.herokuapp.com/api/branch_details/?ifsc=SBIN0001567

- Second url for getting the details of all the branches with the given bank name and city is <br />
https://obscure-gorge-31969.herokuapp.com/api/branches_list/?name=<BANK_NAME>&city=<CITY_NAME> <br />

For e,g if you want to list all the branches of city=MUMBAI of bank name=STATE BANK OF INDIA then url will be like this <br />

https://obscure-gorge-31969.herokuapp.com/api/branches_list/?name=STATE%20BANK%20OF%20INDIA&city=MUMBAI
