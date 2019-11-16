from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime
from web3 import Web3
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e36106119a10a327dd4fd993dfad8262'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  #3 forward slashes for relative path sqlite for easy deployment of database
db = SQLAlchemy(app)  #Create a database instance

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

#def count()


voter_1 = '0x076E4EB4B08eE2AF74A8C27ffBF9E0A4CC0c86c9'
party_a = '0xE0aD2dD9851b60b8FE23827E6aC21018788F95EF' # BJP
party_b = '0x998F8324a9262bFF9Cd5dba0e9679E865b7D8B32' #
party_c = '0x4f541619F081DA24a86826980F4f75fDd40328A0'
party_d = '0x09524678C56B9f7DeE4E8FcA3aBf6f120172c7B3'

private_key='56de1bc16eb8bacf9b6f7da8422b30823bfac49d94b69303f801e0c95b66d9ad'

#balance_a=balance_b=balance_c=balance_d=0

@app.route('/')
@app.route('/login', methods = ['GET', 'POST'])
def login():
	'''
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == '1' and form.password.data == '1':
			flash('You have been logged in!', 'success')
			return render_template(url_for('voting'))
		else:
			flash('Login Unsuccessful. Please check username and password.', 'danger')
	'''

	return render_template('index.html')


@app.route('/voting')
def voting():
	return render_template('clist.html')







@app.route('/partya')
def partya():

	dict_id={'0x076E4EB4B08eE2AF74A8C27ffBF9E0A4CC0c86c9':'ad3da590851b2bde65b56d77a1b57a8a1cd15f2e9d7d3fa588bfd9682ad7d9cb','0x7836B142b0925f2E4f307d45B05F41594b5CA1Ec':'8e8f7e8d037f98489caf6a8bac8a3dc8795a6c90e6f0d404c54399fbefac592a','0x1CeAfd8B440146212bc86b1FeA70673c56c5A552':'afd7221d3866b2d38fdd62ac4d1f868d421e887cc3dfb9b951a0f44328b83d34'
	,'0x87C42f607Abb820049AfEF7482C648670049dE1e':'56de1bc16eb8bacf9b6f7da8422b30823bfac49d94b69303f801e0c95b66d9ad','0x12C8E72f4E6B4a5B49c6AB69687D5fCa425Da545':'49dc005a16997f83b92ed21ef60230dff9483f3d3e12b0772168eb446163e12b','0x54a79C20158B57132d40fc675C2C779BCD1078F0':'99e11feccebd3bdc91cf425bee92c3c3f4bd166a9fa94b5624abf09eb4efe834'}

	key=random.choice(list(dict_id.keys()))
	voter_1=key
	private_key= dict_id[key]
	nonce = web3.eth.getTransactionCount(voter_1)
	tx={'nonce':nonce,	'to':party_a, 'value':web3.toWei(1, 'ether'),'gas':2000000, 'gasPrice':0}
	signed_tx = web3.eth.account.signTransaction(tx, private_key)

	tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
	curr_hash=web3.toHex(tx_hash) #To print


	block_current=web3.eth.getBlock('latest')
	block_no=block_current['number'] #To print


	current_for_timestamp=web3.eth.getBlock(block_no)
	time_stamp=current_for_timestamp['timestamp'] # To print
	
	if block_current['number']>1:
		prev_block=web3.eth.getTransactionByBlock(block_no-1,0)
		prev_hash=prev_block['hash']
		prev_hash=web3.toHex(prev_hash)# To print
	else :
		prev_hash=0 #or this to Print
	balance_a=web3.eth.getBalance(party_a)
	balance_a=web3.fromWei(balance_a,'ether') #To print
	balance_a-=100
	return render_template('party_a.html',curr_hash=curr_hash,block_no=block_no,time_stamp=time_stamp,prev_hash=prev_hash,balance_a=balance_a)






@app.route('/partyb')
def partyb():

	dict_id={'0x076E4EB4B08eE2AF74A8C27ffBF9E0A4CC0c86c9':'ad3da590851b2bde65b56d77a1b57a8a1cd15f2e9d7d3fa588bfd9682ad7d9cb','0x7836B142b0925f2E4f307d45B05F41594b5CA1Ec':'8e8f7e8d037f98489caf6a8bac8a3dc8795a6c90e6f0d404c54399fbefac592a','0x1CeAfd8B440146212bc86b1FeA70673c56c5A552':'afd7221d3866b2d38fdd62ac4d1f868d421e887cc3dfb9b951a0f44328b83d34'
	,'0x87C42f607Abb820049AfEF7482C648670049dE1e':'56de1bc16eb8bacf9b6f7da8422b30823bfac49d94b69303f801e0c95b66d9ad','0x12C8E72f4E6B4a5B49c6AB69687D5fCa425Da545':'49dc005a16997f83b92ed21ef60230dff9483f3d3e12b0772168eb446163e12b','0x54a79C20158B57132d40fc675C2C779BCD1078F0':'99e11feccebd3bdc91cf425bee92c3c3f4bd166a9fa94b5624abf09eb4efe834'}

	key=random.choice(list(dict_id.keys()))
	voter_1=key
	private_key= dict_id[key]
	nonce = web3.eth.getTransactionCount(voter_1)
	tx={'nonce':nonce,	'to':party_b, 'value':web3.toWei(1, 'ether'),'gas':2000000, 'gasPrice':0}
	signed_tx = web3.eth.account.signTransaction(tx, private_key)

	tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
	curr_hash=web3.toHex(tx_hash) #To print


	block_current=web3.eth.getBlock('latest')
	block_no=block_current['number'] #To print


	current_for_timestamp=web3.eth.getBlock(block_no)
	time_stamp=current_for_timestamp['timestamp'] # To print
	
	if block_current['number']>1:
		prev_block=web3.eth.getTransactionByBlock(block_no-1,0)
		prev_hash=prev_block['hash']
		prev_hash=web3.toHex(prev_hash)# To print
	else :
		prev_hash=0 #or this to Print
	balance_b=web3.eth.getBalance(party_b)
	balance_b=web3.fromWei(balance_b,'ether') #To print
	balance_b-=100
	return render_template('party_b.html',curr_hash=curr_hash,block_no=block_no,time_stamp=time_stamp,prev_hash=prev_hash,balance_b=balance_b)




@app.route('/partyc')
def partyc():

	dict_id={'0x076E4EB4B08eE2AF74A8C27ffBF9E0A4CC0c86c9':'ad3da590851b2bde65b56d77a1b57a8a1cd15f2e9d7d3fa588bfd9682ad7d9cb','0x7836B142b0925f2E4f307d45B05F41594b5CA1Ec':'8e8f7e8d037f98489caf6a8bac8a3dc8795a6c90e6f0d404c54399fbefac592a','0x1CeAfd8B440146212bc86b1FeA70673c56c5A552':'afd7221d3866b2d38fdd62ac4d1f868d421e887cc3dfb9b951a0f44328b83d34'
	,'0x87C42f607Abb820049AfEF7482C648670049dE1e':'56de1bc16eb8bacf9b6f7da8422b30823bfac49d94b69303f801e0c95b66d9ad','0x12C8E72f4E6B4a5B49c6AB69687D5fCa425Da545':'49dc005a16997f83b92ed21ef60230dff9483f3d3e12b0772168eb446163e12b','0x54a79C20158B57132d40fc675C2C779BCD1078F0':'99e11feccebd3bdc91cf425bee92c3c3f4bd166a9fa94b5624abf09eb4efe834'}

	key=random.choice(list(dict_id.keys()))
	voter_1=key
	private_key= dict_id[key]
	nonce = web3.eth.getTransactionCount(voter_1)
	tx={'nonce':nonce,	'to':party_c, 'value':web3.toWei(1, 'ether'),'gas':2000000, 'gasPrice':0}
	signed_tx = web3.eth.account.signTransaction(tx, private_key)

	tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
	curr_hash=web3.toHex(tx_hash) #To print


	block_current=web3.eth.getBlock('latest')
	block_no=block_current['number'] #To print


	current_for_timestamp=web3.eth.getBlock(block_no)
	time_stamp=current_for_timestamp['timestamp'] # To print
	
	if block_current['number']>1:
		prev_block=web3.eth.getTransactionByBlock(block_no-1,0)
		prev_hash=prev_block['hash']
		prev_hash=web3.toHex(prev_hash)# To print
	else :
		prev_hash=0 #or this to Print
	balance_c=web3.eth.getBalance(party_c)
	balance_c=web3.fromWei(balance_c,'ether') #To print
	balance_c-=100
	return render_template('party_c.html',curr_hash=curr_hash,block_no=block_no,time_stamp=time_stamp,prev_hash=prev_hash,balance_c=balance_c)







@app.route('/partyd')
def partyd():

	dict_id={'0x076E4EB4B08eE2AF74A8C27ffBF9E0A4CC0c86c9':'ad3da590851b2bde65b56d77a1b57a8a1cd15f2e9d7d3fa588bfd9682ad7d9cb','0x7836B142b0925f2E4f307d45B05F41594b5CA1Ec':'8e8f7e8d037f98489caf6a8bac8a3dc8795a6c90e6f0d404c54399fbefac592a','0x1CeAfd8B440146212bc86b1FeA70673c56c5A552':'afd7221d3866b2d38fdd62ac4d1f868d421e887cc3dfb9b951a0f44328b83d34'
	,'0x87C42f607Abb820049AfEF7482C648670049dE1e':'56de1bc16eb8bacf9b6f7da8422b30823bfac49d94b69303f801e0c95b66d9ad','0x12C8E72f4E6B4a5B49c6AB69687D5fCa425Da545':'49dc005a16997f83b92ed21ef60230dff9483f3d3e12b0772168eb446163e12b','0x54a79C20158B57132d40fc675C2C779BCD1078F0':'99e11feccebd3bdc91cf425bee92c3c3f4bd166a9fa94b5624abf09eb4efe834'}

	key=random.choice(list(dict_id.keys()))
	voter_1=key
	private_key= dict_id[key]
	nonce = web3.eth.getTransactionCount(voter_1)
	tx={'nonce':nonce,	'to':party_d, 'value':web3.toWei(1, 'ether'),'gas':2000000, 'gasPrice':0}
	signed_tx = web3.eth.account.signTransaction(tx, private_key)

	tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
	curr_hash=web3.toHex(tx_hash) #To print


	block_current=web3.eth.getBlock('latest')
	block_no=block_current['number'] #To print


	current_for_timestamp=web3.eth.getBlock(block_no)
	time_stamp=current_for_timestamp['timestamp'] # To print
	
	if block_current['number']>1:
		prev_block=web3.eth.getTransactionByBlock(block_no-1,0)
		prev_hash=prev_block['hash']
		prev_hash=web3.toHex(prev_hash)# To print
	else :
		prev_hash=0 #or this to Print
	balance_d=web3.eth.getBalance(party_d)
	balance_d=web3.fromWei(balance_d,'ether') #To print
	balance_d-=100
	return render_template('party_d.html',curr_hash=curr_hash,block_no=block_no,time_stamp=time_stamp,prev_hash=prev_hash,balance_d=balance_d)




if __name__ == '__main__':
	app.run(debug=True)
