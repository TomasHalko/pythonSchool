mortalKombat_Characters = {"SubZero": "Ice", "Scorpion": "Fire", "Liu Kang": "Kung Fu", "Raiden": "Lightning"}
print(mortalKombat_Characters)

mortalKombat_Characters["Tomas"] = "Jiu Jitsu"
print(mortalKombat_Characters)

print(mortalKombat_Characters["SubZero"])

mortalKombat_Characters.pop("Scorpion")
print(mortalKombat_Characters)