All data is added to the 201704_raw_data file. use less >> 201704_raw_data.txt
to add the data. BE CAREFUL!! use ">>", not ">" one overwrites the file and the
other appends to the file and Linux is a cruel mistress and will not ask twice. 

After adding all data, strip data using something like 
grep 20170407 201704_raw_data.txt | sort >> cleaned_data/20170407.txt
This is will searh for the date and put the date in the file.

This file can then be transfered to the correct directory for graphing and
comparisons. 
