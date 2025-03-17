import re
my_text = "jkdhsdhglkgkldgj kjhdfkjdgkjdk jhfdjfkjdk ijbdfjkfkjd hjdfhjfgjh jbdkjgkjsgn jihdjkhgkjds djhbdjhfb. Another number is kdgkjsdhgjkhglhs jhfjkdghkj jdfkjdsjkfhdsjlf jkdshgjsfhdglsd kdgjsdhglk 666 444 4567 idhfidshgkjl hfdiuahfiuds jhfiuadshfiuf 2223-456-8768 jhfbjkadsf ghfsiaghfkkfsh geuihiuhtiouerhwtpn ehoihtioewht ihfiuaf 111-222-4444"
pattern = re.compile(r"\d{3}-\d{3}-\d{4}")  
pattern_matches_in_text = pattern.search(my_text)
# searching in the text, as the object from the search method
if pattern_matches_in_text:
    actual_number = pattern_matches_in_text.group()
    print(f"Phone number found: {actual_number}")
else:
	print("Number not found")