* change yoking csv file
cd "/Users/feibai/otreenew/yoking"

import delimited yoking.csv

sort participantcode

drop if participantid_in_session!=105

 export delimited using "/Users/feibai/otreenew/yoking/yokingnew.csv", replace
