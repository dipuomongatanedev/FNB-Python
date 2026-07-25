contacts = {
   
    "crystal": "0829742261",
    "lesedi": "0631293239",
    "thato": "0692395432"
}
name=input("enter the name of the friend you want to look up")

if name in contacts:
    print(f"Found! {name}'s number is {contacts[name]}")
else:
    print("Contact not found.")