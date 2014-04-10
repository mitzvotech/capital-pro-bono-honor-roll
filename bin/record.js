var mongoose = require('mongoose');

var recordschema = mongoose.Schema({
	year: Number,
	bar_number: Number,
	organization: String,
	organization_id: Number,
	first_name: String,
	middle_name: String,
	last_name: String,
	high_honor_roll: Boolean,
	email_address: String,
	phone_number: String,
	date_entered:Date
});

var Record = mongoose.model('Record',recordschema);

module.exports = Record