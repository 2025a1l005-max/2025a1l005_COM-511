mess = input().lower()

if("make a lot of money" in mess or "buy now" in mess or " subscribe this" in mess or "click this" in mess ):
    print("Spam!")
else:
    print("Not spam.")