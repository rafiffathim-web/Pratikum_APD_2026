formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50]]

# formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50]]
# print(formula1)
# # Output
# ['Suzuka', 10, True, 20.3, ['Lewis Hamilton', 2]]

# formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50]]
# print(formula1[3])
# # Output
# 20.30
# print(formula1[4][0])
# # Output
# "Lewis Hamilton"

print("add")

sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
print(sirkuit)
# Output
['Suzuka', 'Monza', 'Silverstone', 'Marina Bay']
sirkuit.append("Spa-Francorchamps")
print(sirkuit)
# Output
['Suzuka', 'Monza', 'Silverstone', 'Marina Bay', 'Spa-Francorchamps']

sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
print(sirkuit)
# Output
['Suzuka', 'Monza', 'Silverstone', 'Marina Bay']
sirkuit.extend(["Spa-Francorchamps", "Interlagos"])
print(sirkuit)
# Output
['Suzuka', 'Monza', 'Silverstone', 'Marina Bay', 'Spa-Francorchamps',
'Interlagos']

sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
print(sirkuit)
# Output
['Suzuka', 'Monza', 'Silverstone', 'Marina Bay']
sirkuit.insert(2, "Interlagos")
print(sirkuit)
# Output
['Suzuka', 'Monza', 'Interlagos', 'Silverstone', 'Marina Bay']


print("update")


sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
print(sirkuit)
# Output
['Suzuka', 'Monza', 'Silverstone', 'Marina Bay']
sirkuit[1] = "Monza Italia"
print(sirkuit)
# Output
['Suzuka', 'Monza Italia', 'Silverstone', 'Marina Bay']

sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
print(sirkuit)
# Output
['Suzuka', 'Monza', 'Silverstone', 'Marina Bay']
sirkuit[0:2] = ["Sepang", "Mugello"]
print(sirkuit)
# Output
['Sepang', 'Mugello', 'Silverstone', 'Marina Bay']

print("delete")

sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
print(sirkuit)
# Output
['Suzuka', 'Monza', 'Silverstone', 'Marina Bay']
del sirkuit[2]
print(sirkuit)
# Output
['Suzuka', 'Monza', 'Marina Bay']

sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
print(sirkuit)
# Output
['Suzuka', 'Monza', 'Silverstone', 'Marina Bay']
sirkuit.remove("Suzuka")
print(sirkuit)
# Output
['Monza', 'Silverstone', 'Marina Bay']

sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
print(sirkuit)
# Output
['Suzuka', 'Monza', 'Silverstone', 'Marina Bay']
ambil_sirkuit = sirkuit.pop(2)
print(ambil_sirkuit)
# Output
# Silverstone

print("Slicing List")

driver = ["Hamilton", "Verstappen", "Leclerc", "Sainz", "Russell",
"Antoneli", "Norris"]
print(driver[0:6:2])
# Output
['Hamilton', 'Leclerc', 'Russell']

print("Operator Pada List")

team1 = ["Mercedes", "Ferrari", "MacLaren"]
team2 = ["Red Bull", "Alpine", "Aston Martin"]
gabung_team = team1 + team2
print(gabung_team)
# Output
['Mercedes', 'Ferrari', 'MacLaren', 'Red Bull', 'Alpine', 'Aston Martin']

juara_WDC = ["MacLaren", "Red Bull"]
juara = juara_WDC * 3
print(juara)
# Output
['MacLaren', 'Red Bull', 'MacLaren', 'Red Bull', 'MacLaren', 'Red Bull']

print("Nested List")

line_up = [
["Ferrari", "Leclerc", 16],
["Mercedes", "Hamilton", 44],
["Red Bull", "Verstappen", 1],
["McLaren", "Norris", 4]
]
print(line_up[2][1])
# Output
# Verstappen

line_up = [
["Ferrari", "Leclerc", 16],
["Mercedes", "Hamilton", 44],
["Red Bull", "Verstappen", 1],
["McLaren", "Norris", 4]
]
for i in line_up:
    for j in i:
        print(j)

# Output
# Ferrari
# Leclerc
# 16
# Mercedes
# Hamilton
# 44
# Red Bull
# Verstappen
# 1
# McLaren
# Norris
# 4


print("B.Tuple")


print("Membuat Tuple (Create Tuple)")

chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))

print("Menampilkan Tuple (Read Tuple)")

print(chara)
# Output
('Yukari', 20, True, 150.4, ['Odette', 25], ('Yukino', 22))
chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
print(chara[2])
print(chara[-1])
print(chara[4][0])

# Output
True
('Yukino', 22)
# Odette

print("Memperbarui Tuple (Update Tuple)")

listchara = list(chara)
listchara.append("Yui ")
chara = tuple(listchara)
print(chara)
# Output
('Yukari', 20, True, 150.4, ['Odette', 25], ('Yukino', 22), 'Yui ')

chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
listchara = list(chara)
listchara.extend(["Kohaku", "Hikaru"])
chara = tuple(listchara)
print(chara)
# Output
('Yukari', 20, True, 150.4, ['Odette', 25], ('Yukino', 22), 'Kohaku', 'Hikaru')

chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
listchara = list(chara)
listchara.insert(2, "Senku")
chara = tuple(listchara)
print(chara)
# Output
('Yukari', 20, 'Senku', True, 150.4, ['Odette', 25], ('Yukino', 22))

chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
listchara = list(chara)
listchara[2] = False
chara = tuple(listchara)
print(chara)
# Output
('Yukari', 20, False, 150.4, ['Odette', 25], ('Yukino', 22))

chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
listchara = list(chara)
listchara[0:2] = ["Senku", 17]
chara = tuple(listchara)
print(chara)
# Output
('Senku', 17, True, 150.4, ['Odette', 25], ('Yukino', 22))

print("Menghapus Tuple (Delete Tuple)")

chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
listchara = list(chara)
del listchara[3]
chara = tuple(listchara)
print(chara)
# Output
('Yukari', 20, True, ['Odette', 25], ('Yukino', 22))

chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
listchara = list(chara)
listchara.remove("Yukari")
chara = tuple(listchara)
print(chara)
# Output
(20, True, 150.4, ['Odette', 25], ('Yukino', 22))

chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
listchara = list(chara)
hapus_chara = listchara.pop(1)
chara = tuple(listchara)
print(chara)
print(hapus_chara)
# Output
('Yukari', True, 150.4, ['Odette', 25], ('Yukino', 22))
20

print("Slicing Tuple")

chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
print(chara[0:5:2])
# Output
('Yukari', True, ['Odette', 25])

print("Unpack Tuple")

chara = ("Yukari", "Yukino", "Odette", "Senku")
(Persona, Oregairu, Genshin, DrStone) = chara
print(Persona)
print(Oregairu)
# Output
# Yukari
# Yukino

chara = ("Yukari", "Yukino", "Odette", "Senku")
(Persona, Oregairu, *anime) = chara
print(Persona)
print(Oregairu)
print(anime)
#Output
# Yukari
# Yukino
['Odette', 'Senku']

print("Operator Pada Tuple")

chara = ("Yukari", "Yukino", "Odette", "Senku")
umur = (20, 22, 25, 17)
join = chara + umur
print(join)
# Output
('Yukari', 'Yukino', 'Odette', 'Senku', 20, 22, 25, 17)

chara = ("Yukari", 20)
gandakan = chara * 3
print(gandakan)
# Output
('Yukari', 20, 'Yukari', 20, 'Yukari', 20)