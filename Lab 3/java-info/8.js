alert( null || 2 || undefined ); // 2

alert( alert(1) || 2 || alert(3) ); // 1, then 2

alert( 1 && null && 2 ); // null

alert( alert(1) && alert(2) ); // 1, then undefined

alert( null || 2 && 3 || 4 ); // 3

let age;

if(!(age > 14 && age < 90));
if (age < 14 || age > 90);

if (-1 || 0) alert( 'first' ); // will run
if (-1 && 0) alert( 'second' ); // won't run
if (null || -1 && 1) alert( 'third' ); //will run

